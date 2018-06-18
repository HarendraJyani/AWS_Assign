import boto3, json
client = boto3.client('lambda')
eventToCallperky_error = {}
try:
	response = client.invoke(FunctionName="perky_error",InvocationType='Event',Payload = json.dumps(perky_error))
	print(response)
except Exception as e:
	print e
