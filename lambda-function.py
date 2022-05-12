import boto3
import os
from datetime import datetime, timezone
from dotenv import load_dotenv
load_dotenv()

def lambda_handler(event, context):
            
    today = datetime.now(timezone.utc)
    get_last_modified = lambda obj: int(obj['LastModified'].strftime('%s'))
    s3 = boto3.client('s3', region_name='us-east-1')
    objs = s3.list_objects_v2(Bucket='sb-dev-webs3bucket-vsj7qme3h7pf')['Contents']
    last_added = [obj['Key'] for obj in sorted(objs, key=get_last_modified)][-1] 
    objects = s3.list_objects(Bucket=os.getenv("Bucket"))
    for o in objects["Contents"]:
        if(o["Key"] == last_added):
            lastUpdatedFileDate = o["LastModified"]
            diff = (today-lastUpdatedFileDate).days
            if(diff>10):
                publishSNS(lastUpdatedFileDate)
            else:
                print("Files are present in last 10 days scan")

def publishSNS(lastUpdatedFileDate):
    sns = boto3.client('sns')
    response = sns.publish(
    TopicArn=os.getenv("TopicArn"),   
    Message=f'No Records found in last 10 days. Last record was inserted on {lastUpdatedFileDate}'
    )
    print(response)
