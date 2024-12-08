import os
import xarray as xr
import pandas as pd
from dask.distributed import Client
class nc_operation:
    def __init__(self, file_path_pattern, index_type, start_year=2011, end_year=2018, lat_range=[60, 49], lon_range=[-120, -110], output_zarr_path="combined_data.zarr"):
        """
        """
        client = Client(n_workers=4)
        self.index_type = index_type
        self.file_path_pattern = file_path_pattern
        self.start_year = start_year
        self.end_year = end_year
        self.lat_range = lat_range
        self.lon_range = lon_range
        self.output_zarr_path = output_zarr_path

        if os.path.exists(output_zarr_path):
            print("Loading data from existing Zarr file...")
            self.data = xr.open_zarr(output_zarr_path)
        else:
            self.data = self.load_and_process_data()
            
            # Rechunking to ensure uniform chunk sizes across the dataset
            self.data = self.data.chunk({'Time': 365})
            self.data.to_zarr(output_zarr_path, mode="w", consolidated=True)

    def load_and_process_data(self):
        """
        Read all files in dir and merge together
        :return: Merged xarray Dataset
        """
        yearly_datasets = []

        for year in range(self.start_year, self.end_year + 1):
            file_path = self.file_path_pattern.replace("*", str(year))
            print(file_path)
            if os.path.exists(file_path):
                print(f"Processing file: {file_path}")

                dataset = xr.open_dataset(file_path, chunks={'Time': 365})
                
                dataset = self.day_to_date(dataset, year)
                
                dataset = dataset.assign_coords(
                Longitude=xr.where(dataset['Longitude'] > 180, dataset['Longitude'] - 360, dataset['Longitude'])
                    )
                
                dataset = dataset.sel(Latitude=slice(self.lat_range[0], self.lat_range[1]),
                                      Longitude=slice(self.lon_range[0], self.lon_range[1]))

                yearly_datasets.append(dataset)

        combined_data = xr.concat(yearly_datasets, dim="Time")
        return combined_data

    def day_to_date(self, data, year):
        """
        :param data: xarray Dataset
        :param year: year
        :return: date transformed xarray Dataset
        """
        start_date = pd.Timestamp(f"{year}-01-01")
        dates = pd.date_range(start=start_date, periods=len(data['Time']), freq='D')
        data = data.assign_coords(Time=dates)
        return data
