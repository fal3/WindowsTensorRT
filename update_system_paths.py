```python
import os
import sys

def add_to_path(path):
    os.environ["PATH"] += os.pathsep + path

def main():
    cuda_path = "C:/Program Files/NVIDIA GPU Computing Toolkit/CUDA/v11.8/bin"
    python_path = "C:/Python310/"
    tensorrt_path = "C:/Program Files/NVIDIA Corporation/NvInfer"
    cudnn_path = "C:/Program Files/NVIDIA GPU Computing Toolkit/CUDA/v11.8/libnvvp"

    add_to_path(cuda_path)
    add_to_path(python_path)
    add_to_path(tensorrt_path)
    add_to_path(cudnn_path)

    print("Paths added successfully. Please restart your system for the changes to take effect.")

if __name__ == "__main__":
    main()
```