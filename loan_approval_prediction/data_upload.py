from dagshub import get_repo_bucket_client
# Get a boto3.client object
s3 = get_repo_bucket_client("bhaskarmulik27/kaggle_playground")

# Upload file
s3.upload_file(
    Bucket="kaggle_playground",  # name of the repo
    Filename="data/test.csv",  # local path of file to upload
    Key="data/test.csv.csv",  # remote path where to upload the file
)

s3.upload_file(
    Bucket = "kaggle_playground",
    Filename = "data/train.csv",
    Key = "data/train.csv"
)