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

elif sys.argv[1] == "route53":
    session = boto3.session.Session(profile_name=f'{sys.argv[3]}')
    route53_client = session.client('route53', region_name=f'{sys.argv[2]}')
    response = route53_client.list_hosted_zones_by_name()
    count = 0
    lenHZ = len(response['HostedZones'])
    while count < lenHZ:
        print(response['HostedZones'][count]['Name'])
        count +=1

elif sys.argv[1] == "cloudfront":
    session = boto3.session.Session(profile_name=f'{sys.argv[3]}')
    cloudfront_client = session.client('cloudfront', region_name=f'{sys.argv[2]}')
    response = cloudfront_client.list_distributions()
    count = 0
    lenD = len(response['DistributionList']['Items'])
    while count < lenD:
        print(f'{response['DistributionList']['Items'][count]['Id']} - {response['DistributionList']['Items'][count]['DomainName']}')
        count +=1

elif sys.argv[1] == "lambda":
    session = boto3.session.Session(profile_name=f'{sys.argv[3]}')
    lambda_client = session.client('lambda', region_name=f'{sys.argv[2]}')
    response = lambda_client.list_functions()
    count = 0
    lenF = len(response['Functions'])
    while count < lenF:
        print(f'{response['Functions'][count]['FunctionName']} - {response['Functions'][count]['Runtime']}')
        count +=1

elif sys.argv[1] == "iam":
    session = boto3.session.Session(profile_name=f'{sys.argv[3]}')
    iam_client = session.client('iam', region_name=f'{sys.argv[2]}')
    response = iam_client.list_users()
    count = 0
    lenI = len(response['Users'])
    while count < lenI:
        print(response['Users'][count]['UserName'])
        count +=1

elif sys.argv[1] == "ecr":
    session = boto3.session.Session(profile_name=f'{sys.argv[3]}')
    ecr_client = session.client('ecr', region_name=f'{sys.argv[2]}')
    response = ecr_client.describe_repositories()
    count = 0
    lenR = len(response['repositories'])
    while count < lenR:
        print(f'{response['repositories'][count]['repositoryName']} - {response['repositories'][count]['repositoryUri']}')
        count +=1

print("\nLet's do it!")