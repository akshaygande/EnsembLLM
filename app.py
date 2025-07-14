import streamlit as st
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Set wide mode for Streamlit layout
st.set_page_config(layout="wide")

# Load the merged model and tokenizer
@st.cache_resource
def load_model():
    model_path = r"C:\Users\LENOVO\Downloads\MMajor\merged_folder"
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    model = AutoModelForCausalLM.from_pretrained(model_path, torch_dtype=torch.float16).to("cpu")
    return model, tokenizer

model, tokenizer = load_model()

# Generator function for streaming responses from the model
def model_response_generator(prompt: str, max_length: int = 1000) -> str:
    inputs = tokenizer(prompt, return_tensors="pt", padding=True, truncation=True)
    # Ensure attention mask is passed to the model
    inputs['attention_mask'] = inputs.get('attention_mask', torch.ones(inputs['input_ids'].shape))  
    inputs['pad_token_id'] = tokenizer.pad_token_id  # Ensure pad_token_id is set
    
    outputs = model.generate(inputs["input_ids"], attention_mask=inputs["attention_mask"], max_length=max_length, do_sample=True)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

# Page title
st.title("🤖 MergeLLM: Powered by Merged Models")

# Initialize session state variables
if "messages" not in st.session_state:
    st.session_state.messages = []

# Clear chat history functionality
if st.button("Clear Chat History"):
    st.session_state.messages = []

# Display chat messages
for message in st.session_state.messages:
    if message["role"] == "user":
        with st.chat_message("user"):
            st.markdown(f'<div class="chat-box user-message">{message["content"]}</div>', unsafe_allow_html=True)
    else:
        with st.chat_message("assistant"):
            st.markdown(f'<div class="chat-box assistant-message">{message["content"]}</div>', unsafe_allow_html=True)

# Chat input functionality
if prompt := st.chat_input("How can I assist you?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(f'<div class="chat-box user-message">{prompt}</div>', unsafe_allow_html=True)

    # Generate response from the model
    with st.chat_message("assistant"):
        response = model_response_generator(prompt)
        st.markdown(f'<div class="chat-box assistant-message">{response}</div>', unsafe_allow_html=True)
        st.session_state.messages.append({"role": "assistant", "content": response})
