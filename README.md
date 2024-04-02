# SDK MAILMAN
Show resources in AWS accounts to facilitate troubleshooting.

### Available Services
- **S3** (Buckets)
- **EC2** (Instances)
- **ELB** (Load balancers)
- **ECS** (Containers)
- **RDS** (Instances and Clusters)
- **CodeBuild** (Projects)
- **SecretsManager** (Secrets)

### How to use
To run locally you need to config [AWS profiles](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html) and install [Python SDK](https://github.com/boto/boto3).

#### Command structure
```bash
$ python file_name.py service profile
$ python file_name.py service region profile
```