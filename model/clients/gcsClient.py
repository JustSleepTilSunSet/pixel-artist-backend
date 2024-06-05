from google.auth.credentials import AnonymousCredentials
from google.cloud import storage
conn = "http://fake-gcs-server:4443"


client = storage.Client(
    credentials=AnonymousCredentials(),
    project="dummy_project",
    client_options={"api_endpoint": conn},
)
print(f"Connection with gcs established.");
def listBuckets():
    for bucket in client.list_buckets():
        print(f"Bucket: {bucket.name}\n")