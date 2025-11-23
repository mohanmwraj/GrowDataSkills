# Make sure to do below mentioned steps

# pip install google-cloud-storage
# export GOOGLE_APPLICATION_CREDENTIALS="/path/to/your-service-account.json"

import os
from google.cloud import storage

def list_buckets(project_id: str):
    """
    Fetches and prints all bucket names in the specified project.
    """

    client = storage.Client(project=project_id)
    
    print(f"Buckets in project {project_id}:")
    for bucket in client.list_buckets():
        print(f" - {bucket.name}")

if __name__ == "__main__":

    project = "poetic-brace-478910-s4"
    list_buckets(project)