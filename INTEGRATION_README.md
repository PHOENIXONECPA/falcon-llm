# Falcon-LLM Integration Setup

This directory contains tools for setting up a comprehensive workspace that integrates Falcon-LLM with GenArtist and document generation capabilities.

## Quick Start

Run the integration setup script to create a complete workspace:

```bash
python setup_integration.py
```

This will:
1. Create a workspace directory (`falcon_genartist_workspace`)
2. Clone the Falcon-LLM and GenArtist repositories
3. Set up a virtual environment
4. Install required dependencies
5. Create an integration script (`integrate.py`)

## What Gets Created

### Directory Structure
```
falcon_genartist_workspace/
├── falcon-llm/          # Cloned Falcon-LLM repository
├── genartist/           # Cloned GenArtist repository (or placeholder)
├── venv/                # Python virtual environment
└── integrate.py         # Integration script
```

### Integration Script Features

The `integrate.py` script provides:

- **Text Generation**: Interface to Falcon-LLM for text generation
- **Image Generation**: Interface to GenArtist for image generation  
- **PDF Generation**: Create PDF documents using ReportLab
- **Excel Generation**: Create Excel files using pandas and openpyxl
- **Fallback Functionality**: Works even if some dependencies aren't available

## Usage

After running the setup script:

```bash
cd falcon_genartist_workspace

# Activate the virtual environment
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate     # Windows

# Run the integration test
python integrate.py
```

## Falcon-LLM Module

The repository also includes a `falcon_llm.py` module that provides a simplified API for using Falcon-LLM:

```python
from falcon_llm import FalconLLM

# Initialize the model
llm = FalconLLM()
if llm.initialize():
    # Generate text
    response = llm.generate("What is the meaning of life?")
    print(response)
```

## Dependencies

The setup script will attempt to install:

- Falcon-LLM dependencies (PyTorch, transformers, etc.)
- Document generation libraries (reportlab, openpyxl, pandas, PyPDF2)

If some dependencies fail to install (e.g., due to network issues or CUDA requirements), the integration script will still work with placeholder functionality.

## Customization

You can modify the repository URLs in `setup_integration.py`:

```python
FALCON_REPO = "https://github.com/PHOENIXONECPA/falcon-llm.git"
GENARTIST_REPO = "https://github.com/PHOENIXONECPA/img2imgpro.git"  # Replace with your repo
```

## Troubleshooting

### CUDA Dependencies
If you encounter issues with PyTorch/CUDA dependencies, you may need to install them manually based on your system configuration.

### Network Issues
If repository cloning fails, check your network connection and repository URLs.

### Missing Dependencies
The integration script is designed to work with missing dependencies by providing placeholder functionality. Install missing packages manually as needed.