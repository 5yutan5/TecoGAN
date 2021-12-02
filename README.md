# TecoGAN with Conda

This repository is originally fork of [TecoGan](https://github.com/thunil/TecoGAN).
You can easily build an environment with tis repo.
This repo support for Windows 10.

## Requirements

- Windows 10
- [Conda latest](https://docs.conda.io/en/latest/miniconda.html)

## Installation

1. Install CUDA==11.2.2  
    [Download page](https://developer.nvidia.com/cuda-11.2.2-download-archive?target_os=Windows&target_arch=x86_64&target_version=10&target_type=exenetwork).
1. Install cuDNN==8.1  
    You need to register membership before install cuDNN.  
    [Download page](https://developer.nvidia.com/cudnn).
1. Install miniconda  
    [Download page](https://docs.conda.io/en/latest/miniconda.html).
    You need to install 

1. Create virtual environment  

    ```Shell
    
    conda create -n tecogan python=3.7 -y
    conda activate tecogan
    ```
