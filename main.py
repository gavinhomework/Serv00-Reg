name: Run Python Script

on:
  push:
    branches:
      - main
  workflow_dispatch:

jobs:
  run-script:
    runs-on: ubuntu-latest

    steps:
    # Step 1: Check out code
    - name: Checkout code
      uses: actions/checkout@v3

    # Step 2: Set up Python
    - name: Setup Python
      uses: actions/setup-python@v4
      with:
        python-version: "3.10"

    # Step 3: Install dependencies
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt

    # Step 4: Run the script
    - name: Run script
      env:
        EMAIL: "test@example.com"  # Replace with a valid email or use GitHub Secrets
      run: python script.py
