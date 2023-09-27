# XPublish Exploring Setup

## Using Mamba

In many cases, conda times out while trying to create this environment. In that case, install [Micromamba](https://mamba.readthedocs.io/en/latest/micromamba-installation.html) first and then run these commands.

```bash
micromamba env create -f environment.yaml
micromamba activate xpublish-exploring
```

## Using conda

> Note: This method may time out

Create the environment and activate: 

```bash
conda env create -f environment.yaml
conda activate xpublish-exploring
```

## Starting the Server

Execute `demo.py` and you should see similar output indicating success:

`Uvicorn running on http://0.0.0.0:9000 (Press CTRL+C to quit)`

After seeing this message, you can then navigate to this address in your browser:

http://localhost:9000/docs

Here you should see a web page that allows you to inspect and test the available endpoints from Xpublish.

# XPublish Tutorial

## Exploring available datasets

Navigate to http://localhost:9000/datasets to return a list of available datasets running on your xpublish host. These are defined in the `TutorialsDataset` plugin class in `demo.py`.

Inspect one of those datasets by appending the dataset name to the URL. For example, http://localhost:9000/datasets/air_temperature/

This returns an xarray model view of that dataset.

## Calculating the mean value

XPublish's plugin system allows custom operations to be run against the data on the server. In the example `mean.py`, a custom plugin has been defined that allows the mean of a specific variable to be calculated. The power of this ecosystem is that any dataset in xpublish is interoperable with any sensible plugin.

For the end-user, you can choose which variable to calculate using the URL syntax `/[dataset]/[variable]/mean`. For example, http://localhost:9000/datasets/air_temperature/air/mean

## Working with Large Marine Environment (LME) regions

Another custom plugin is defined in `lme.py`. You can access this plugin at http://localhost:9000/lme/

