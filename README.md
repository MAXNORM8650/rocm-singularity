
---

# Singularity/Apptainer Setup and Flash Attention Installation Guide

### Step 1: Prepare Scratch Space

```bash
mkdir -p ~/path/to/dir/cache/.singularity/cache
```

### Step 2: Set Environment Variables for Scratch Space

Set the following environment variables to use the scratch space for Singularity caching and temporary directories:

```bash
export SINGULARITY_CACHEDIR=~/path/to/dir/cache/.singularity/cache
mkdir ~/path/to/dir/cache/.singularity/tmp
export SINGULARITY_TMPDIR=~/path/to/dir/cache/.singularity/tmp
```

### Step 3: Pull the Singularity Container. More pre-build images you can find in the website of (docker)[https://hub.docker.com/u/rocm]. See some. more examples !(/conainers/README.md)[/conainers/README.md]
### One more vllm exmaple : rocm/vllm:rocm6.4.1_vllm_0.10.1_20250909
```bash
singularity pull docker://rocm/pytorch-nightly
```
Or you can also use Apptainer, the latest binary: 

```bash
apptainer pull docker://rocm/pytorch-nightly
```
### Step 4: Access the Singularity Container

After pulling the container, run the following command to access the Singularity shell:

```bash
singularity shell -B ~/:/workspace rocm-pytorch-nightly.sif
```
singularity shell -B /vast/users/hisham.cholakkal/documents:/workspace rocm64.sif
### Step 5: Create an Interactive Workspace

Once inside the container, navigate to the `/workspace` directory and list its contents:

```bash
cd /workspace
ls
```

### Step 6: Set Environment Variables for Cache Path

Set the following environment variables for cache paths and directories:

```bash
export PIP_CACHE_DIR=/workspace/cachepath/.cache
export CONDA_PKGS_DIRS=/workspace/cachepath/env/pkgs
export CONDA_ENVS_PATH=/workspace/cachepath/env
export TMPDIR=/workspace/cachepath/tmp
export TEMP_DIR=/workspace/cachepath/tmp
export UV_CACHE_DIR=/workspace/cachepath/env/uv
export TRITON_CACHE_DIR=/workspace/cachepath/.cache
export XDG_CACHE_HOME=/workspace/cachepath/.cache
export HF_HOME=/workspace/cachepath/hf
export HUGGINGFACE_HUB_CACHE=/workspace/cachepath/.cache
export PYTHONUSERBASE=/workspace/cachepath/env/pkgs
export PADDLEX_HOME=/workspace/cachepath/.paddlex
export PADDLE_HOME=/workspace/cachepath/.paddlex
export DATA_HOME=/workspace/cachepath/paddle
export PD_HOME=/workspace/cachepath/.paddlex
export PADDLENLP_HOME=/workspace/cachepath/.paddlex
export PADDLE_PDX_CACHE_HOME=/workspace/cachepath/.paddlex
export PADDLE_EXTENSION_DIR=/workspace/cachepath/.cache
export PATH="/workspace/cachepath/env/pkgs/bin:$PATH"
```

### Step 7: Create Cache Path Directory

```bash
mkdir /workspace/cachepath
```

### Step 8: Install Flash Attention

Clone the Flash Attention repository and install it:

```bash
git clone https://github.com/Dao-AILab/flash-attention.git
cd flash-attention
git checkout main_perf
FLASH_ATTENTION_TRITON_AMD_ENABLE="TRUE" python setup.py install
## if the file is not writeable
FLASH_ATTENTION_TRITON_AMD_ENABLE="TRUE" python setup.py install --prefix=/workspace/cachepath/env
```

### Step 9: Test Flash Attention

Run the following Python code to test Flash Attention:

```bash
FLASH_ATTENTION_TRITON_AMD_ENABLE="TRUE" python
import flash_attn
```

### Step 10: Running Multi-Node or Multi-GPU Training

To run Flash Attention on multiple nodes or GPUs, use the following command:

```bash
FLASH_ATTENTION_TRITON_AMD_ENABLE="TRUE" accelerate launch --config_file ./trl/accelerate_configs/zero1.yaml --num_machines 1 --num_processes 4 train_grpo.py
```

### Step 11: Troubleshooting

If you encounter any errors, run the following command to debug:

```bash
HSAKMT_DEBUG_LEVEL=3 FLASH_ATTENTION_TRITON_AMD_ENABLE="TRUE" accelerate launch --config_file ./trl/accelerate_configs/zero1.yaml --num_machines 1 --num_processes 4 train_grpo.py
```

###PYQ
```bash
"""singularity pull docker://rocm/pytorch:rocm7.0.2_ubuntu24.04_py3.12_pytorch_release_2.6.0
"""
##Setup enviroments variables
git config --global http.proxy $http_proxy
git config --global https.proxy $https_proxy
git config --global http.proxyAuthMethod 'basic'

$http_proxy
http://svc_proxy_nonrte_netgrp:jLNgeTuuCdbu9h9kesPaA4iEDrzHvXtR@172.22.13.140:3128git config --global http.proxy "$http_proxy"
git config --global https.proxy "$https_proxy"
git config --global http.proxyAuthMethod 'basic'

singularity shell -B ~/:/workspace 
export MIOPEN_USER_DB_PATH="/vast/users/hisham.cholakkal/tmp_dir/miopen_node8"
export MIOPEN_CUSTOM_CACHE_DIR=${MIOPEN_USER_DB_PATH}
rm -rf ${MIOPEN_USER_DB_PATH}
mkdir -p ${MIOPEN_USER_DB_PATH}
```

---

This guide provides all the steps needed to set up the environment, install the necessary software, and troubleshoot any issues while using Flash Attention in a Singularity container. Let me know if you need further clarification or modifications.
