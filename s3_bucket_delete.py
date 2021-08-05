import boto3

#create an s3 client
BUCKET_NAME = 'bob10-5972-priv-boto'

region = 'ap-northeast-2'
session = boto3.Session(profile_name='jayjeon')
s3 = session.client(
    service_name = 's3',
    region_name=region
)

client = boto3.client('s3')

response = client.list_objects(Bucket = BUCKET_NAME)

for content in response['Contents']:
    obj_dic = client.get_object(Bucket = BUCKET_NAME, Key = content['Key'])
    print(content['Key'], obj_dic['LastModified'])

response = client.delete_objects(Bucket = BUCKET_NAME, Delete = {'Objects': [{'Key': 'test.txt'}]})


response = client.list_objects(Bucket = BUCKET_NAME)

for content in response['Contents']:
    obj_dic = client.get_object(Bucket = BUCKET_NAME, Key = content['Key'])
    print(content['Key'], obj_dic['LastModified'])


response = client.list_object_versions(Bucket = BUCKET_NAME)
for content in response['Versions']:
    print(content['Key'])

'''
bucket = s3.bucket(BUCKET_NAME)
bucket.object_versions.delete()
'''

response = client.delete_bucket(Bucket= BUCKET_NAME)

