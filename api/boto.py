import boto3

client = boto3.client('rds')
instances = client.describe_db_instances(DBInstanceIdentifier="petitzoo-mysql")
hostrds = instances.get('DBInstances')[0].get('Endpoint').get('Address')
print (f"{hostrds}") 
