```python
import os
import subprocess
import sys

def check_system_requirements():
    # Check system requirements here
    pass

def download_software(download_link):
    subprocess.call(['curl', download_link, '-o', 'cuda_installer.exe'])

def install_software():
    subprocess.call(['cuda_installer.exe', '/S'])

def update_path_variable(installation_directory):
    os.environ['PATH'] += os.pathsep + installation_directory

def main():
    check_system_requirements()

    cuda_download_link = 'https://developer.nvidia.com/cuda-11.8.0-download-archive'
    download_software(cuda_download_link)

    install_software()

    cuda_installation_directory = 'C:\\Program Files\\NVIDIA GPU Computing Toolkit\\CUDA\\v11.8\\bin'
    update_path_variable(cuda_installation_directory)

if __name__ == "__main__":
    main()
```