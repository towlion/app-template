import os
import uuid

import boto3
from botocore.config import Config


def get_s3_client():
    return boto3.client(
        "s3",
        endpoint_url=os.getenv("S3_ENDPOINT", "http://minio:9000"),
        aws_access_key_id=os.getenv("S3_ACCESS_KEY", "minioadmin"),
        aws_secret_access_key=os.getenv("S3_SECRET_KEY", "minioadmin"),
        config=Config(signature_version="s3v4"),
        region_name="us-east-1",
    )


BUCKET = os.getenv("S3_BUCKET", "app-uploads")


def ensure_bucket():
    client = get_s3_client()
    try:
        client.head_bucket(Bucket=BUCKET)
    except Exception:
        client.create_bucket(Bucket=BUCKET)


def upload_file(data: bytes, filename: str, content_type: str) -> str:
    client = get_s3_client()
    key = f"{uuid.uuid4().hex}/{filename}"
    client.put_object(Bucket=BUCKET, Key=key, Body=data, ContentType=content_type)
    return key


def get_presigned_url(key: str, expires: int = 3600) -> str:
    client = get_s3_client()
    return client.generate_presigned_url(
        "get_object",
        Params={"Bucket": BUCKET, "Key": key},
        ExpiresIn=expires,
    )


def delete_file(key: str):
    client = get_s3_client()
    client.delete_object(Bucket=BUCKET, Key=key)
