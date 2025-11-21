# Python Environment Setup Notes

## Conda Environment
- Created with: `conda create -n trading python=3.12`
- Activated with: `conda activate trading`

## Core Packages Installed
- lightgbm (verified with `python -c "import lightgbm; print('LightGBM OK')"`)
- fastapi, "uvicorn[standard]", python-dotenv, requests, streamlit
- ccxt, alpaca-trade-api

## Export Environment
- `conda env export --no-builds > environment.yml`

