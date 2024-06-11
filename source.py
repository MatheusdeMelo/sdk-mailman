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
        if 'Tags' in response['Reservations'][count]['Instances'][0]:
            for tag in response['Reservations'][count]['Instances'][0]['Tags']:
                if tag['Key'] == 'Name':
                    print(f"{count+1}- {tag['Value']} <-> {response['Reservations'][count]['Instances'][0]['InstanceType']}@{response['Reservations'][count]['Instances'][0]['State']['Name']}")
        else:
            print(f"{count+1}- null <-> {response['Reservations'][count]['Instances'][0]['InstanceType']}@{response['Reservations'][count]['Instances'][0]['State']['Name']}")
        count +=1

elif sys.argv[1] == "elb":
    session = boto3.session.Session(profile_name=f'{sys.argv[3]}')
    elb_client = session.client('elbv2', region_name=f'{sys.argv[2]}')
    response = elb_client.describe_load_balancers()
    lenLB = len(response['LoadBalancers'])
    count = 0
    while count < lenLB:
        print(f"{count+1}- {response['LoadBalancers'][count]['LoadBalancerName']} <-> {response['LoadBalancers'][count]['DNSName']}@{response['LoadBalancers'][count]['Type']}")
        count +=1

elif sys.argv[1] == "ecs":
    session = boto3.session.Session(profile_name=f'{sys.argv[3]}')
    ecs_client = session.client('ecs', region_name=f'{sys.argv[2]}')
    response = ecs_client.list_clusters()
    count = 0
    lenC = len(response['clusterArns'])
    while count < lenC:
        split = response['clusterArns'][count].split("/")
        print(f"{count+1}- {split[1]}")
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
        print(f'Cluster - {cluster_response['DBClusters'][count]['DBClusterIdentifier']} > {cluster_response['DBClusters'][count]['Engine']}@{cluster_response['DBClusters'][count]['EngineVersion']} ')
        count +=1
    while count < lenI:
        print(f'Instance - {instance_response['DBInstances'][count]['DBInstanceIdentifier']} > {instance_response['DBInstances'][count]['Engine']}@{instance_response['DBInstances'][count]['EngineVersion']}')
        count +=1

elif sys.argv[1] == "codebuild":
    session = boto3.session.Session(profile_name=f'{sys.argv[3]}')
    codebuild_client = session.client('codebuild', region_name=f'{sys.argv[2]}')
    search = codebuild_client.list_projects()
    count = 0
    lenP = len(search['projects'])
    while count < lenP:
        response = codebuild_client.batch_get_projects(names=[search['projects'][count]])
        print(f"{count+1}- {response['projects'][0]['name']} <-> {response['projects'][0]['source']['location']}")
        count +=1

elif sys.argv[1] == "secretsmanager":
    session = boto3.session.Session(profile_name=f'{sys.argv[3]}')
    secretsmanager_client = session.client('secretsmanager', region_name=f'{sys.argv[2]}')
    response = secretsmanager_client.list_secrets()
    count = 0
    lenP = len(response['SecretList'])
    while count < lenP:
        print(f"{count+1}- {response['SecretList'][count]['Name']}")
        count +=1

elif sys.argv[1] == "route53":
    session = boto3.session.Session(profile_name=f'{sys.argv[3]}')
    route53_client = session.client('route53', region_name=f'{sys.argv[2]}')
    response = route53_client.list_hosted_zones_by_name()
    count = 0
    lenHZ = len(response['HostedZones'])
    while count < lenHZ:
        print(f"{count+1}- {response['HostedZones'][count]['Name']}")
        count +=1

elif sys.argv[1] == "cloudfront":
    session = boto3.session.Session(profile_name=f'{sys.argv[3]}')
    cloudfront_client = session.client('cloudfront', region_name=f'{sys.argv[2]}')
    response = cloudfront_client.list_distributions()
    count = 0
    lenD = len(response['DistributionList']['Items'])
    while count < lenD:
        print(f'{count+1}- {response['DistributionList']['Items'][count]['Id']} - {response['DistributionList']['Items'][count]['DomainName']}')
        count +=1

elif sys.argv[1] == "lambda":
    session = boto3.session.Session(profile_name=f'{sys.argv[3]}')
    lambda_client = session.client('lambda', region_name=f'{sys.argv[2]}')
    response = lambda_client.list_functions()
    count = 0
    lenF = len(response['Functions'])
    while count < lenF:
        print(f'{count+1}- {response['Functions'][count]['FunctionName']} - {response['Functions'][count]['Runtime']}')
        count +=1

elif sys.argv[1] == "iam":
    session = boto3.session.Session(profile_name=f'{sys.argv[3]}')
    iam_client = session.client('iam', region_name=f'{sys.argv[2]}')
    response = iam_client.list_users()
    count = 0
    lenI = len(response['Users'])
    while count < lenI:
        print(f"{count+1}- {response['Users'][count]['UserName']}")
        count +=1

elif sys.argv[1] == "ecr":
    session = boto3.session.Session(profile_name=f'{sys.argv[3]}')
    ecr_client = session.client('ecr', region_name=f'{sys.argv[2]}')
    response = ecr_client.describe_repositories()
    count = 0
    lenR = len(response['repositories'])
    while count < lenR:
        print(f'{count+1}- {response['repositories'][count]['repositoryName']} - {response['repositories'][count]['repositoryUri']}')
        count +=1

elif sys.argv[1] == "acm":
    session = boto3.session.Session(profile_name=f'{sys.argv[3]}')
    acm_client = session.client('acm', region_name=f'{sys.argv[2]}')
    response = acm_client.list_certificates()
    count = 0
    lenC = len(response['CertificateSummaryList'])
    while count < lenC:
        print(f'{count+1}- {response['CertificateSummaryList'][count]['DomainName']}')
        count +=1

elif sys.argv[1] == "elasticache":
    session = boto3.session.Session(profile_name=f'{sys.argv[3]}')
    elasticache_client = session.client('elasticache', region_name=f'{sys.argv[2]}')
    response = elasticache_client.describe_cache_clusters()
    count = 0
    lenC = len(response['CacheClusters'])
    while count < lenC:
        print(f'{count+1}- {response['CacheClusters'][count]['CacheClusterId']} <-> {response['CacheClusters'][count]['Engine']}@{response['CacheClusters'][count]['EngineVersion']}')
        count +=1

elif sys.argv[1] == "waf":
    session = boto3.session.Session(profile_name=f'{sys.argv[3]}')
    waf_client = session.client('wafv2', region_name=f'{sys.argv[2]}')
    response = waf_client.list_web_acls(Scope='REGIONAL')
    count = 0
    lenW = len(response['WebACLs'])
    while count < lenW:
        print(f'{count+1}- {response['WebACLs'][count]['Id']} <-> {response['WebACLs'][count]['Name']}')
        count +=1

elif sys.argv[1] == "codedeploy":
    session = boto3.session.Session(profile_name=f'{sys.argv[3]}')
    codedeploy_client = session.client('codedeploy', region_name=f'{sys.argv[2]}')
    response = codedeploy_client.list_applications()
    count = 0
    lenA = len(response['applications'])
    while count < lenA:
        print(f'{count+1}- {response['applications'][count]}')
        count +=1

elif sys.argv[1] == "sqs":
    session = boto3.session.Session(profile_name=f'{sys.argv[3]}')
    sqs_client = session.client('sqs', region_name=f'{sys.argv[2]}')
    response = sqs_client.list_queues()
    #print(f'Show me the response: {response['QueueUrls'][0].split("/")[4]}')
    count = 0
    lenQ = len(response['QueueUrls'])
    while count < lenQ:
        print(f'{count+1}- {response['QueueUrls'][count].split("/")[4]} <-> {response['QueueUrls'][count]}')
        count +=1

print("\nLet's do it!")