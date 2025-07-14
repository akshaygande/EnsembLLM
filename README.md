# EnsembleLLM

**EnsembleLLM** is a toolkit and demo application for merging, evaluating, and serving large language models (LLMs) using advanced model merging techniques. This repository provides the code, configuration, and instructions to reproduce, deploy, and interact with your own merged LLMs—without including the large model weights directly.

---

## 🚨 Model Weights Not Included

Due to their size and licensing, **model weights are not included in this repository**.  
Instead, you can easily download the merged model from the Hugging Face Hub (see below).

---

## 📦 Features

- **Model Merging**: Combine multiple LLMs using advanced methods (TIES, linear, SLERP, etc.) via [mergekit](https://github.com/arcee-ai/mergekit).
- **Streamlit Demo**: Interactive web UI for chatting with your merged model.
- **Reproducible Configurations**: All merge parameters and recipes are versioned.
- **Hugging Face Integration**: Download or upload models via the Hugging Face Hub.
- **Extensible**: Add new merge methods, evaluation tasks, or model architectures.

---

## 🚀 Quickstart

### 1. Clone the Repository

```bash
git clone https://github.com/akshaygande/EnsembLLM.git
cd EnsembLLM
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Download the Merged Model

The merged model is hosted on Hugging Face Hub:

- **Model Repo:** [Akshaygande/EnsembleLLM](https://huggingface.co/Akshaygande/EnsembleLLM)

#### Option A: Using Git LFS

```bash
git lfs install
git clone https://huggingface.co/Akshaygande/EnsembleLLM merged_folder
```

#### Option B: Using Python

```python
from huggingface_hub import snapshot_download
snapshot_download(repo_id="Akshaygande/EnsembleLLM", local_dir="merged_folder")
```

### 4. Run the Application

```bash
python3 app.py
```

- The Streamlit app will launch in your browser.
- Ensure `model_path = "merged_folder"` in your code/config.

---

## 📝 Project Structure

```
EnsembLLM/
│
├── app.py                # Streamlit web app for chat demo
├── config.yaml           # Example merge configuration
├── requirements.txt      # Python dependencies
├── merged_folder/        # (Ignored) Downloaded or generated model weights
├── mergekit/             # Model merging toolkit (submodule or vendored)
│   ├── mergekit/         # Core library code
│   ├── examples/         # Example merge configs
│   ├── docs/             # Documentation
│   └── tests/            # Unit tests
└── README.md             # This file
```

---

## ⚙️ Configuration

- **`config.yaml`**: Example merge configuration for [mergekit](https://github.com/arcee-ai/mergekit).
- **`requirements.txt`**: Minimal dependencies (Streamlit, Transformers, Torch, etc.).
- **`.gitignore`**: Excludes large model files, virtual environments, and OS-specific files.

---

## 🛠️ Model Merging & Reproducibility

- To reproduce or customize the merged model, use the configs and scripts in `mergekit/`.
- See [mergekit documentation](mergekit/README.md) for advanced usage, custom merge methods, and evaluation.

---

## 🔐 Hugging Face Credentials

- **Downloading**: The model is public—no authentication required.
- **Uploading/Modifying**: You need your own Hugging Face account and access token.

---

## 🧑‍💻 Contributing

Contributions are welcome!  
Please see the [mergekit/CLA.md](mergekit/CLA.md) and [mergekit/LICENSE](mergekit/LICENSE) for licensing and contributor terms.

---

## 📄 License

- **Code**: See [mergekit/LICENSE](mergekit/LICENSE) (Business Source License 1.1).
- **Model Weights**: Subject to the original model licenses and Hugging Face terms.

---

## ❓ Support & Issues

- For questions, open an [issue](https://github.com/akshaygande/EnsembLLM/issues) or contact the maintainer.
- For mergekit-specific issues, see [arcee-ai/mergekit](https://github.com/arcee-ai/mergekit).

---

## 📚 References

- [mergekit Documentation](mergekit/README.md)
- [Hugging Face Hub](https://huggingface.co/docs/hub/index)
- [Streamlit Documentation](https://docs.streamlit.io/)

---

**Ready to get started?**  
Clone, install, download the model, and run the app! 
