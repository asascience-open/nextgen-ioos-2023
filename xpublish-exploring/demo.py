import cf_xarray
import xarray as xr
from requests import HTTPError

from xpublish import Plugin, Rest, hookimpl


class TutorialDataset(Plugin):
    name: str = "xarray-tutorial-datasets"

    @hookimpl
    def get_datasets(self):
        return list(xr.tutorial.file_formats)
    
    @hookimpl
    def get_dataset(self, dataset_id: str):
        try:
            return xr.tutorial.open_dataset(dataset_id)
        except HTTPError:
            return None





rest = Rest({})
rest.register_plugin(TutorialDataset())

from mean import MeanPlugin
from lme import LmeSubsetPlugin
rest.register_plugin(MeanPlugin())
rest.register_plugin(LmeSubsetPlugin())

rest.serve()
