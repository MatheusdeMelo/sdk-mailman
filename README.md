# SDK MAILMAN
Show resources in AWS accounts to facilitate troubleshooting.

### Available Services
- **S3** (Buckets)
- **EC2** (Instances: Identifiers, Types and States)
- **ELB** (Load balancers: Identifiers, DNS and Types)
- **ECS** (Containers)
- **RDS** (Instances and Clusters)
- **CodeBuild** (Projects)
- **SecretsManager** (Secrets)
- **Route53** (Hosted Zones)
- **Cloudfront** (Ids and Domain Names)
- **Lambda** (Functions and Runtime Languages)
- **IAM** (Users)
- **ECR** (Repositories)
- **ACM** (Domain Names)
- **Elasticache** (Clusters and Engines)
- **WAF** (Web ACLs)
- **CodeDeploy** (Applications)
- **SQS** (Queue Urls)

### How to use
To run locally you need to config [AWS profiles](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html) and install [Python SDK](https://github.com/boto/boto3).

#### Command structure
```bash
$ python file_name.py service profile
$ python file_name.py service region profile
```

The first option to S3 service and second command option to others services. 
