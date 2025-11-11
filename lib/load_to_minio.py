import os
from minio import Minio
from dotenv import load_dotenv

load_dotenv()

access_key = os.getenv('MINIO_ACCESS_KEY')
secret_key = os.getenv('MINIO_SECRET_KEY')

client = Minio("localhost:9000", access_key, secret_key, secure=False)
    
def load_file(client: Minio):
    
    
if client.bucket_exists("job-results"):
    print("my-bucket exists")
else:
    client.make_bucket("job-results")