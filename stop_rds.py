# import the boto3 which will use to interact  with the aws
import boto3

client = boto3.client('rds')

response = client.stop_db_instance(
    DBInstanceIdentifier=input("Enter the database name"),
    DBSnapshotIdentifier=input("Enter the snapshot name")
)
print(response)