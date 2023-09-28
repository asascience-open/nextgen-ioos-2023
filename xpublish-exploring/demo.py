import cf_xarray
import xarray as xr
from requests import HTTPError

from xpublish import Plugin, Rest, hookimpl


class TutorialDataset(Plugin):
    name: str = "xarray-tutorial-datasets"

    @hookimpl
    def get_datasets(self):
        tutorial_datasets = list(xr.tutorial.file_formats)
        tutorial_datasets.append('ngofs2')
        return tutorial_datasets
    
    @hookimpl
    def get_dataset(self, dataset_id: str):
        print(dataset_id)
        try:
            if dataset_id == 'ngofs2':
                ds = xr.open_dataset('nos.ngofs2.2ds.f001.20230928.t09z.nc', decode_times=False)
            else:
                ds = xr.tutorial.open_dataset(dataset_id)
                if ds.cf.coords['longitude'].dims[0] == 'longitude':
                    ds = ds.assign_coords(longitude=(((ds.longitude + 180) % 360) - 180)).sortby('longitude')
                    # TODO: Yeah this should not be assumed... but for regular grids we will viz with rioxarray so for now we will assume
                    ds = ds.rio.write_crs(4326)
            return ds
        except HTTPError:
            return None





rest = Rest({})
rest.register_plugin(TutorialDataset())

### For this tutorial, you can uncomment the following lines to activate the other plugins:

# from mean import MeanPlugin
# from lme import LmeSubsetPlugin
# rest.register_plugin(MeanPlugin())
# rest.register_plugin(LmeSubsetPlugin())

rest.serve()
