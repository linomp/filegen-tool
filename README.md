﻿# File Generator App

This is a simple Streamlit app that generates files with random data and allows you to download them. Currently supports .xlsx and .txt files.

**Check the live version [here](https://app-filegen-5o5rfikerwjvsiuihdzb8c.streamlit.app/).**

## Prerequisites

- Python 3.6 or later
- pip (Python package installer)

## Getting Started

1. Clone the repository:

   ```sh
   git clone https://github.com/yourusername/file-generator-app.git
   cd file-generator-app

2. Set up & activate a virtual environment
    ```
    # On macOS and Linux
    python3 -m venv venv
    source venv/bin/activate
    
    # On Windows
    python -m venv venv
    .\venv\Scripts\activate
    ```
3. Install the required packages:
    ```
    pip install -r requirements.txt
    ```
4. Run the app:
    ```
    streamlit run main.py
    ```

## Testing
With the virtual environment activated, run the following command:
```commandline
pytest
```
