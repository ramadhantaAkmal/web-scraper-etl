import os
import datetime
from minio import Minio
from minio.error import S3Error
from dotenv import load_dotenv

load_dotenv()

current_date = datetime.date.today()

access_key = os.getenv('MINIO_ACCESS_KEY')
secret_key = os.getenv('MINIO_SECRET_KEY')
minio_endpoint = os.getenv('MINIO_ENDPOINT')
bucket_name = os.getenv('BUCKET_NAME')
object_name = f"jobs-result-{current_date}.json"
file_path = f"/opt/airflow/lib/jobs-result-weekly/jobs-result-{current_date}.json"
    
def upload_file_to_minio():
    """
    Uploads a file to a MinIO bucket.
    """
    try:
        # Create a client with the MinIO server playground, its access key
        # and secret key.
        client = Minio(
            minio_endpoint,
            access_key=access_key,
            secret_key=secret_key,
            secure=False 
        )

        # Make the bucket if it doesn't exist.
        found = client.bucket_exists(bucket_name)
        if not found:
            client.make_bucket(bucket_name)
            print(f"Bucket '{bucket_name}' created successfully.")
        else:
            print(f"Bucket '{bucket_name}' already exists.")

        # Upload the file.
        client.fput_object(
            bucket_name,
            object_name,
            file_path,
        )
        print(f"'{file_path}' is successfully uploaded as '{object_name}' to bucket '{bucket_name}'.")

    except S3Error as e:
        print(f"Error uploading file: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

upload_file_to_minio()