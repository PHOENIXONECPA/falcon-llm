#!/usr/bin/env python3
"""
Falcon-LLM Integration Setup Script

This script sets up a workspace for integrating Falcon-LLM with GenArtist
and adds PDF/XLS generation capabilities.
"""

import os
import subprocess
import sys
import platform

FALCON_REPO = "https://github.com/PHOENIXONECPA/falcon-llm.git"  # Use your fork URL if needed
GENARTIST_REPO = "https://github.com/PHOENIXONECPA/img2imgpro.git"  # Example; replace with your GenArtist repo
WORKDIR = "falcon_genartist_workspace"

def run(cmd, cwd=None):
    """Execute a shell command with error handling."""
    print(f"Running: {cmd}")
    try:
        subprocess.check_call(cmd, shell=True, cwd=cwd)
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {cmd}")
        print(f"Exit code: {e.returncode}")
        raise

def ensure_venv(venv_dir):
    """Create virtual environment if it doesn't exist and return activation script path."""
    if not os.path.exists(venv_dir):
        run(f"{sys.executable} -m venv {venv_dir}")
    print(f"Virtual environment created/verified: {venv_dir}")
    
    # Cross-platform activation script path
    if platform.system() == "Windows":
        activate_script = os.path.join(venv_dir, "Scripts", "activate")
        pip_executable = os.path.join(venv_dir, "Scripts", "pip")
    else:
        activate_script = os.path.join(venv_dir, "bin", "activate")
        pip_executable = os.path.join(venv_dir, "bin", "pip")
    
    return activate_script, pip_executable

def main():
    """Main setup function."""
    print("Setting up Falcon-LLM + GenArtist integration workspace...")
    
    # Create workspace directory
    os.makedirs(WORKDIR, exist_ok=True)
    os.chdir(WORKDIR)
    print(f"Working in directory: {os.getcwd()}")

    # Clone Falcon-LLM if not present
    if not os.path.exists("falcon-llm"):
        print("Cloning Falcon-LLM repository...")
        run(f"git clone {FALCON_REPO} falcon-llm")
    else:
        print("Falcon-LLM repository already exists")

    # Clone GenArtist if not present
    if not os.path.exists("genartist"):
        print("Cloning GenArtist repository...")
        try:
            run(f"git clone {GENARTIST_REPO} genartist")
        except subprocess.CalledProcessError:
            print("Warning: Could not clone GenArtist repository. Creating placeholder...")
            os.makedirs("genartist", exist_ok=True)
            # Create a placeholder main.py for GenArtist
            genartist_placeholder = '''
def generate(prompt):
    """Placeholder GenArtist function."""
    print(f"GenArtist placeholder: would generate image for '{prompt}'")
    return f"placeholder_image_{hash(prompt)}.png"

def main():
    return {"generate": generate}
'''
            with open("genartist/main.py", "w") as f:
                f.write(genartist_placeholder)
    else:
        print("GenArtist repository already exists")

    # Create and activate virtual environment
    venv_dir = "venv"
    activate_script, pip_executable = ensure_venv(venv_dir)
    
    # Install requirements for Falcon-LLM
    if os.path.exists("falcon-llm/requirements.txt"):
        print("Installing Falcon-LLM requirements...")
        try:
            run(f"{pip_executable} install -r falcon-llm/requirements.txt")
        except subprocess.CalledProcessError:
            print("Warning: Failed to install some Falcon-LLM requirements.")
            print("This might be due to network issues or CUDA dependencies.")
            print("The integration script will still work with fallback functionality.")
    else:
        print("Warning: falcon-llm/requirements.txt not found")

    # Install PDF/XLS libraries
    print("Installing PDF/XLS generation libraries...")
    try:
        run(f"{pip_executable} install reportlab openpyxl pandas PyPDF2")
    except subprocess.CalledProcessError:
        print("Warning: Failed to install some PDF/XLS libraries.")
        print("You may need to install them manually: pip install reportlab openpyxl pandas PyPDF2")

    # Scaffold integration code
    print("Creating integration script...")
    integration_code = '''#!/usr/bin/env python3
"""
Falcon-LLM + GenArtist Integration Module

This module provides integration between Falcon-LLM, GenArtist, and document generation.
"""

import sys
import os

# Add paths to the repositories
sys.path.append("falcon-llm")
sys.path.append("genartist")

try:
    from main import main as falcon_main
except ImportError:
    print("Warning: Could not import falcon_main. Make sure falcon-llm is properly set up.")
    falcon_main = None

try:
    from main import main as genartist_main
except ImportError:
    print("Warning: Could not import genartist_main. Using placeholder.")
    class PlaceholderGenArtist:
        @staticmethod
        def generate(prompt):
            return f"placeholder_image_{hash(prompt)}.png"
    
    genartist_main = PlaceholderGenArtist()

def generate_image(prompt):
    """Generate an image using GenArtist."""
    if hasattr(genartist_main, 'generate'):
        return genartist_main.generate(prompt)
    else:
        print(f"GenArtist placeholder: would generate image for '{prompt}'")
        return f"placeholder_image_{hash(prompt)}.png"

def generate_pdf(data, filename):
    """Generate a PDF document using reportlab."""
    try:
        from reportlab.pdfgen import canvas
        c = canvas.Canvas(filename)
        c.drawString(100, 750, str(data))
        c.save()
        print(f"PDF generated: {filename}")
    except ImportError:
        print("Error: reportlab not installed. Run: pip install reportlab")

def generate_xls(data, filename):
    """Generate an Excel file using pandas and openpyxl."""
    try:
        import pandas as pd
        if isinstance(data, list):
            df = pd.DataFrame(data)
        else:
            df = pd.DataFrame([{"data": str(data)}])
        df.to_excel(filename, index=False)
        print(f"Excel file generated: {filename}")
    except ImportError:
        print("Error: pandas or openpyxl not installed. Run: pip install pandas openpyxl")

def run_llm_task(prompt):
    """Run a text generation task using Falcon-LLM."""
    if falcon_main:
        # This would need to be adapted based on the actual Falcon-LLM API
        print(f"Falcon-LLM processing: {prompt}")
        return f"LLM response to: {prompt}"
    else:
        print(f"Falcon-LLM placeholder: would process '{prompt}'")
        return f"Placeholder response to: {prompt}"

def main():
    """Main integration testing function."""
    print("=== Falcon-LLM + GenArtist Integration Test ===")
    
    print("\\nTesting Falcon-LLM text generation:")
    llm_result = run_llm_task("Hello world!")
    print(f"Result: {llm_result}")

    print("\\nTesting GenArtist image generation:")
    img = generate_image("A futuristic city skyline")
    print(f"Generated image: {img}")

    print("\\nTesting PDF generation:")
    generate_pdf("Hello PDF from Falcon-LLM Integration!", "test.pdf")

    print("\\nTesting Excel generation:")
    test_data = [
        {"prompt": "Hello world!", "response": llm_result},
        {"prompt": "Image generation", "response": img}
    ]
    generate_xls(test_data, "test.xlsx")

    print("\\n=== Integration test complete! ===")

if __name__ == "__main__":
    main()
'''

    with open("integrate.py", "w") as f:
        f.write(integration_code)

    print("\n" + "="*50)
    print("Setup complete!")
    print("="*50)
    print(f"Workspace created in: {os.getcwd()}")
    print("\nTo run integration tests:")
    if platform.system() == "Windows":
        print(f"  {activate_script} && python integrate.py")
    else:
        print(f"  source {activate_script} && python integrate.py")
    
    print("\nTo activate the virtual environment:")
    if platform.system() == "Windows":
        print(f"  {activate_script}")
    else:
        print(f"  source {activate_script}")

if __name__ == "__main__":
    main()