# Dataset Integration Script

This script (`dataset_integration.py`) automatically downloads and organizes datasets from Kaggle and GitHub for use with the Falcon LLM project.

## Features

- Downloads Kaggle datasets using the Kaggle API
- Clones GitHub repositories containing datasets
- Automatically extracts zip files from Kaggle downloads
- Organizes all datasets in a structured directory layout
- Includes placeholder integration points for GenArtist multimodal support

## Prerequisites

### System Requirements
- Python 3.6+
- Git installed and available in PATH
- Kaggle CLI tool installed and configured

### Kaggle Setup
1. Install the Kaggle CLI: `pip install kaggle`
2. Create a Kaggle account and generate API credentials
3. Place your `kaggle.json` file in `~/.kaggle/` or set `KAGGLE_CONFIG_DIR` environment variable
4. Ensure proper permissions: `chmod 600 ~/.kaggle/kaggle.json`

## Usage

```bash
python dataset_integration.py
```

## Datasets

### Kaggle Datasets
- `seancalvert1/moredocs` - Document processing dataset
- `seancalvert1/identity` - Identity verification dataset

### GitHub Repositories
- `UniData-pro/Synthetic-Passports-Dataset` - Synthetic passport data for document analysis
- `QuickSign/docxpand` - Document expansion and processing tools

## Directory Structure

After running the script, datasets will be organized as follows:

```
datasets/
├── moredocs/                    # From seancalvert1/moredocs
│   ├── [extracted files]
├── identity/                    # From seancalvert1/identity  
│   ├── [extracted files]
├── Synthetic-Passports-Dataset/ # Cloned GitHub repo
│   ├── README.md
│   └── [repo files]
└── docxpand/                    # Cloned GitHub repo
    ├── README.md
    └── [repo files]
```

## GenArtist Integration

The script includes placeholder code for integrating with GenArtist for multimodal AI capabilities:

- Text-to-image generation
- Image-to-image processing  
- Image-to-video conversion

To customize for your pipeline, modify the integration section in the `main()` function.

## Notes

- The `datasets/` directory is automatically added to `.gitignore` to prevent large dataset files from being committed
- ZIP files from Kaggle downloads are automatically extracted and the original archives are removed
- GitHub repositories are only cloned if they don't already exist locally
- All operations include verbose logging for debugging

## Error Handling

The script will exit with an error if:
- Kaggle credentials are not properly configured
- Network connectivity issues prevent downloads
- Insufficient disk space for datasets
- Missing system dependencies (git, unzip)

## Customization

To add additional datasets:

1. **Kaggle datasets**: Add to the `kaggle_datasets` list in the format `"username/dataset-name"`
2. **GitHub repositories**: Add full clone URLs to the `github_datasets` list

Example:
```python
kaggle_datasets = [
    "seancalvert1/moredocs",
    "seancalvert1/identity", 
    "your-username/your-dataset"  # Add new Kaggle dataset
]

github_datasets = [
    "https://github.com/UniData-pro/Synthetic-Passports-Dataset.git",
    "https://github.com/QuickSign/docxpand.git",
    "https://github.com/your-org/your-repo.git"  # Add new GitHub repo
]
```