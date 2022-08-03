# import the boto3 which will use to interact  with the aws
import boto3
# We will take the all imput from the end user.

# You need to enter rds as input
AWS_service= input("Enter the service name\n")

database_name=input("Enter the database name\n")

# you need to enter the snapshot name for your RDS instance
snapshot_name=input("Enter the snapshot name\n")

client = boto3.client(AWS_service)

stop_rds = client.stop_db_instance (
    DBInstanceIdentifier= database_name,
    DBSnapshotIdentifier=snapshot_name
)
print(stop_rds)

print("Your RDS has been stoped Successfully ")