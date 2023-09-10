# File Generator Tool

This is a simple tool for generating files of arbitrary size with random data and allows you to download them. Currently supports .xlsx and .txt files.

## Usage
- Check the deployed Streamlit version [here](https://app-filegen-5o5rfikerwjvsiuihdzb8c.streamlit.app/).
- Or set it up locally:
   ```
   git clone https://github.com/linomp/filegen-tool.git
   cd filegen-tool
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   streamlit run streamlit_app/main.py
   ```
## Roadmap
- [X] Simple streamlit-based app (loads everything in memory, slow AF)
- [ ] FastAPI-based backend to stream files chunk by chunk instead of loading it all in memory
