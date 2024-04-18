# ICON P-Rep ICX Tracker

This repository contains a Python script designed to keep track of how much ICX a P-Rep has earned on the ICON network. 

## Usage

1. Install the required dependencies listed in `requirements.txt`.
2. Run the script with appropriate command-line arguments (start block height and optional end block height). If block height is not given the script calculates till the latest height.
3. The script will fetch IScore and P-Rep information, calculate ICX earnings, and generate a CSV report.

``` 
python3 main.py <startBlockHeight> 
```

## Requirements

- Python 3.x
- Dependencies listed in `requirements.txt`