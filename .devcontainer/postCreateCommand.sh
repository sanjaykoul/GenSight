#!/bin/bash

# Ensure conda is initialized
source /opt/conda/etc/profile.d/conda.sh

# Create conda environment named 'venv' if it doesn't exist
if ! conda info --envs | grep -q "^venv"; then
    conda create -n venv python=3.10 -y
fi

# Install packages in the 'venv' environment
conda run -n venv pip install --upgrade pip
conda run -n venv pip install -r requirements.txt
