```python
import os
import subprocess
import sys

TENSORRT_DOWNLOAD_LINK = "https://developer.nvidia.com/tensorrt-85-ga-update-2-download"
TENSORRT_INSTALL_DIR = "C:/Program Files/NVIDIA Corporation/TensorRT"

def check_system_requirements():
    # Check system requirements and compatibility with hardware
    # This is a placeholder and needs to be replaced with actual checks
    pass

def download_tensorrt():
    # Download TensorRT installer using the official download link
    subprocess.check_call(["curl", "-L", "-o", "tensorrt_installer.exe", TENSORRT_DOWNLOAD_LINK])

def install_tensorrt():
    # Install TensorRT using the downloaded installer
    subprocess.check_call(["tensorrt_installer.exe", "/S", "/D=" + TENSORRT_INSTALL_DIR])

def update_path_variable():
    # Add TensorRT installation directory to system's PATH
    path_variable = os.environ.get("PATH")
    tensorrt_path = os.path.join(TENSORRT_INSTALL_DIR, "bin")
    
    if tensorrt_path not in path_variable:
        os.environ["PATH"] = path_variable + ";" + tensorrt_path

def main():
    check_system_requirements()
    download_tensorrt()
    install_tensorrt()
    update_path_variable()

if __name__ == "__main__":
    main()
```