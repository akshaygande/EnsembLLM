<<<<<<< HEAD
# Ensemble_LLM
=======
# EnsembleLLM

## ⚠️ Model Weights Not Included in GitHub

This repository does **not** include the merged model weights (`merged_folder/`) due to their large size and licensing restrictions.

### How to Download the Merged Model

The merged model is hosted on the Hugging Face Hub and can be downloaded directly.

**Hugging Face Model Repo:**
https://huggingface.co/Akshaygande/EnsembleLLM

#### Step-by-Step Instructions

1. **Install Git LFS (if not already installed):**
   ```bash
   git lfs install
   ```

2. **Clone the model repository into your project directory:**
   ```bash
   git clone https://huggingface.co/Akshaygande/EnsembleLLM merged_folder
   ```
   This will create a `merged_folder` with all necessary model files.

3. **Run the main application:**
   ```bash
   python3 app.py
   ```
   (Make sure to set `model_path = "merged_folder"` in your code or configuration.)

#### Alternative: Use huggingface_hub in Python

You can also use the `huggingface_hub` Python library to download the model programmatically:

```python
from huggingface_hub import snapshot_download
snapshot_download(repo_id="Akshaygande/EnsembleLLM", local_dir="merged_folder")
```

---

## Hugging Face Credentials

The model is public, so no authentication is required for download. If you wish to upload or modify the model, you will need your own Hugging Face account and access token.

---

## Project Setup

1. Clone this repository:
   ```bash
   git clone <this-repo-url>
   cd MMajor
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Download the merged model as described above.
4. Run the application:
   ```bash
   python3 app.py
   ```

---

For any issues, please open an issue on GitHub or contact the maintainer. 
>>>>>>> 2d9ee0e (Initial commit: code, config, and instructions (excluding large model files))
