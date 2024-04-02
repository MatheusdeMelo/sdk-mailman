import boto3
import sys
import json
 
if sys.argv[1] == "s3":
    session = boto3.session.Session(profile_name=f'{sys.argv[2]}')
    s3 = session.resource('s3')
    for bucket in s3.buckets.all():
        print(bucket.name)

elif sys.argv[1] == "ec2":
    session = boto3.session.Session(profile_name=f'{sys.argv[3]}')
    ec2_client = session.client('ec2', region_name=f'{sys.argv[2]}')
    response = ec2_client.describe_instances()
    lenT = len(response['Reservations'])
    count = 0
    while count < lenT:
        lenB = len(response['Reservations'][count]['Instances'][0]['Tags'])
        for tag in response['Reservations'][count]['Instances'][0]['Tags']:
            if tag['Key'] == 'Name':
                print(tag['Value'])
        count +=1

elif sys.argv[1] == "elb":
    session = boto3.session.Session(profile_name=f'{sys.argv[3]}')
    elb_client = session.client('elbv2', region_name=f'{sys.argv[2]}')
    response = elb_client.describe_load_balancers()
    lenLB = len(response['LoadBalancers'])
    count = 0
    while count < lenLB:
        print(response['LoadBalancers'][count]['LoadBalancerName'])
        count +=1

elif sys.argv[1] == "ecs":
    session = boto3.session.Session(profile_name=f'{sys.argv[3]}')
    ecs_client = session.client('ecs', region_name=f'{sys.argv[2]}')
    response = ecs_client.list_clusters()
    count = 0
    lenC = len(response['clusterArns'])
    while count < lenC:
        split = response['clusterArns'][count].split("/")
        print(split[1])
        count +=1

elif sys.argv[1] == "rds":
    session = boto3.session.Session(profile_name=f'{sys.argv[3]}')
    rds_client = session.client('rds', region_name=f'{sys.argv[2]}')
    cluster_response = rds_client.describe_db_clusters()
    instance_response = rds_client.describe_db_instances()
    count = 0
    lenC = len(cluster_response['DBClusters'])
    lenI = len(instance_response['DBInstances'])
    while count < lenC:
        print(f'Cluster - {cluster_response['DBClusters'][count]['DBClusterIdentifier']}')
        count +=1
    while count < lenI:
        print(f'Instance - {instance_response['DBInstances'][count]['DBInstanceIdentifier']}')
        count +=1

elif sys.argv[1] == "codebuild":
    session = boto3.session.Session(profile_name=f'{sys.argv[3]}')
    codebuild_client = session.client('codebuild', region_name=f'{sys.argv[2]}')
    response = codebuild_client.list_projects()
    count = 0
    lenP = len(response['projects'])
    while count < lenP:
        print(response['projects'][count])
        count +=1

elif sys.argv[1] == "secretsmanager":
    session = boto3.session.Session(profile_name=f'{sys.argv[3]}')
    secretsmanager_client = session.client('secretsmanager', region_name=f'{sys.argv[2]}')
    response = secretsmanager_client.list_secrets()
    count = 0
    lenP = len(response['SecretList'])
    while count < lenP:
        print(response['SecretList'][count]['Name'])
        count +=1

print("Let's do it!")