#!/bin/bash

# Ensure conda is initialized
source /usr/local/miniconda/etc/profile.d/conda.sh

# Create conda environment in workspace folder
conda create --prefix ./venv python=3.10 -y

# Install packages in the local conda environment
conda run --prefix ./venv pip install --upgrade pip
conda run --prefix ./venv pip install -r requirements.txt
