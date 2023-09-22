# nextgen-ioos-2023

Repository to support 2023 IOOS Annual Meeting breakout session on xpublish and kerchunk workflows.

## Cloning this Repository

*You must have a local version of Git installed for this to work.*

Navigate to the directory where you want the project to be, then run this command:

`cd my-project-dir/`
`git clone https://github.com/asascience-open/nextgen-ioos-2023.git`

## Setting up your Python environment

Choose one of the following methods to set up your Python environment.

### Installation with Virtual Environment

*You must have Python and venv installed for this to work.*

Create your local virtual environment and install dependencies:

```
cd nextgen-ioos-2023/binder
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Installation with Anaconda

*You must have conda installed for this to work.*

```
cd nextgen-ioos-2023/binder
conda env create -f binder/environment.yml
conda activate nextgen-notebooks
```