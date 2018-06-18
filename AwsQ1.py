import boto3

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    objPath = {'Bucket' : 'harrytransfer1','Key' : event['Records'][0]['s3']['object']['key']}
    s3.copy_object(Bucket = 'harrytransfer2',Key = event['Records'][0]['s3']['object']['key'], CopySource = objPath)
    
