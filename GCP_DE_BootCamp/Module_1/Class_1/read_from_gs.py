# make sure to install these things before running this application
# install python in your machine
# install pip utility in your machine

# install below packages once pip utility is setup

# pip install pandas
# pip install fsspec
# pip install gcsfs

import pandas as pd
 
def read_sales_data_from_gcs(bucket_name: str, file_path: str) -> pd.DataFrame:
    """
    Reads a CSV file from Google Cloud Storage into a pandas DataFrame.

    Args:
        bucket_name (str): Name of your GCS bucket.
        file_path (str): Path to the CSV file in the bucket (e.g., 'folder/file.csv').

    Returns:
        pd.DataFrame: Data loaded from GCS.
    """
    gcs_uri = f'gs://{bucket_name}/{file_path}'
    
    # pandas can read directly with gcsfs under the hood
    df = pd.read_csv(gcs_uri, storage_options={'token': '/Users/mora/Documents/GrowDataSkills/GCP_DE_BootCamp/Module_1/Class_1/poetic-brace-478910-s4-459e58c8c820.json'})
    return df

# gs://firstbuckettest_21nov/sales_mock.csv

if __name__ == "__main__":
    # Example usage
    bucket = "firstbuckettest_21nov"
    path = "sales_mock.csv"
    df = read_sales_data_from_gcs(bucket, path)
    print(df.head())