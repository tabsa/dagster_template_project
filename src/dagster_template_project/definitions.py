from dagster import Definitions, define_asset_job
from src.dagster_template_project.defs.assets import sample_asset, processed_data

# Define the jobs to be part of the dagster dev
sample_asset_job = define_asset_job("sample_asset_job", selection="sample_asset")
processed_data_job = define_asset_job("processed_data_job", selection="processed_data")

defs = Definitions(
    assets=[sample_asset, processed_data], jobs=[sample_asset_job, processed_data_job]
)
