from azureml.studio.core.io.data_frame_directory import save_data_frame_to_directory, DataFrameDirectory, load_data_frame_from_directory
from azureml.core import Workspace, Run, Dataset
import pandas as pd

def test_save_load_df(df, tmp_path):
    save_data_frame_to_directory(tmp_path, data=df)

web_path = 'https://raw.githubusercontent.com/microsoft/anomalydetector/master/samples/sample.csv'
df = pd.read_csv(web_path)
#
df.to_parquet("./_data.parquet")

#
# parquet = pd.read_parquet("http://github.com/sccc19/anomalydetector/blob/chansu/test_run_not_started/aml_module/_data.parquet")
# raw = DataFrameDirectory.load_raw_parquet("http://github.com/sccc19/anomalydetector/blob/chansu/test_run_not_started/aml_module/_data.parquet")
# dfd = load_data_frame_from_directory("http://github.com/sccc19/anomalydetector/blob/chansu/test_run_not_started/aml_module/_data.parquet")

parquet = pd.read_parquet("./_data.parquet")
raw = DataFrameDirectory.load_raw_parquet("./_data.parquet")
dfd = load_data_frame_from_directory("./_data.parquet")