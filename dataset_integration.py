import os
import subprocess

# Dataset sources
kaggle_datasets = [
    "seancalvert1/moredocs",
    "seancalvert1/identity"
]
github_datasets = [
    "https://github.com/UniData-pro/Synthetic-Passports-Dataset.git",
    "https://github.com/QuickSign/docxpand.git"
]

DATASETS_DIR = "datasets"

def run(cmd, cwd=None):
    print(f"Running: {cmd}")
    subprocess.check_call(cmd, shell=True, cwd=cwd)

def download_kaggle_dataset(dataset, out_dir):
    run(f"kaggle datasets download -d {dataset} -p {out_dir}")
    # Unzip all zip files in the output directory
    for fname in os.listdir(out_dir):
        if fname.endswith(".zip"):
            run(f"unzip -o {fname}", cwd=out_dir)

def clone_github_repo(repo_url, out_dir):
    repo_name = repo_url.split('/')[-1].replace('.git', '')
    repo_path = os.path.join(out_dir, repo_name)
    if not os.path.exists(repo_path):
        run(f"git clone {repo_url} {repo_path}")

def main():
    os.makedirs(DATASETS_DIR, exist_ok=True)

    # Download Kaggle datasets
    for dataset in kaggle_datasets:
        dataset_dir = os.path.join(DATASETS_DIR, dataset.split('/')[1])
        os.makedirs(dataset_dir, exist_ok=True)
        download_kaggle_dataset(dataset, dataset_dir)

    # Clone GitHub datasets
    for repo in github_datasets:
        clone_github_repo(repo, DATASETS_DIR)

    print("All datasets downloaded and organized.")

    # Stub: Integrate with GenArtist (customize these for your actual pipeline)
    print("Integrating datasets into GenArtist...")
    print("TODO: Add code for multimodal support (text-to-image, image-to-image, image-to-video)")
    # Example:
    # genartist.add_dataset(os.path.join(DATASETS_DIR, "moredocs"))
    # genartist.enable_text_to_image()
    # genartist.enable_image_to_image()
    # genartist.enable_image_to_video()

    print("Integration script complete.")

if __name__ == "__main__":
    main()