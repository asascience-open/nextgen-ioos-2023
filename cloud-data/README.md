# Installation Instructions

## Installation with Virtual Environment

*You must have Python and venv installed for this to work.*

Create your local virtual environment and install dependencies:

```
cd nextgen-ioos-2023/binder
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Installation with Anaconda

*You must have conda installed for this to work.*

```
cd nextgen-ioos-2023/binder
conda env create -f binder/environment.yml
conda activate nextgen-notebooks
```