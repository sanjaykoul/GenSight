#!/bin/bash

# Create conda environment named 'venv'
conda create -n venv python=3.10 -y

# Activate the environment and install packages
source activate venv
pip install --upgrade pip
pip install -r requirements.txt
