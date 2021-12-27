import pytest
import boto3
from moto import mock_s3
from paws.s3 import download

# @mock_s3
# def test_my_model_save():
#     conn = boto3.resource('s3', region_name='us-east-1')
#     # We need to create the bucket since this is all in Moto's 'virtual' AWS account
#     conn.create_bucket(Bucket='mybucket')
#     model_instance = MyModel('steve', 'is awesome')
#     model_instance.save()
#     body = conn.Object('mybucket', 'steve').get()['Body'].read().decode("utf-8")
#     assert body == 'is awesome'

@pytest.fixture()
def mock_boto():
    """Setup boto3
    """
    mock = mock_s3()
    mock.start()

    output_str = 'Something'
    s3 = boto3.resource('s3', region_name='ap-northeast-1')
    s3.create_bucket(Bucket="gdelt-open-data", 
                     CreateBucketConfiguration={
                        #  https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Client.create_bucket
                         "LocationConstraint": "ap-northeast-1"
                     })
    s3.Bucket("gdelt-open-data").put_object(Key="events/1979.csv",Body=output_str)

    yield s3

    mock.stop()

def test_download(mock_boto, tmpdir):
    """Test s3 download function"""

    resource = mock_boto
    filepath = str(tmpdir) + "/" + "1979.csv"
    res = download(resource=resource, bucket="gdelt-open-data",
                   key="events/1979.csv", filepath=filepath)
    
    with open(filepath, 'r') as fp:
        string = fp.read()
    
    assert res == str(tmpdir) + "/" + "1979.csv"
    assert string == 'Something'