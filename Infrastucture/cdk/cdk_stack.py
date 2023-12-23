from aws_cdk import (aws_s3 as _s3, Stack, aws_ec2 as ec2, aws_rds )
from constructs import Construct


class S3Stack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        vpc = ec2.Vpc(self, "Healthcare-data-ingestion-pipeline-vpc",
                      cidr='192.168.0.0/16',
                      max_azs=2,
                      subnet_configuration=[
                          ec2.SubnetConfiguration(name="Public",
                                                  subnet_type=ec2.SubnetType.PUBLIC,
                                                  cidr_mask=20),
                          ec2.SubnetConfiguration(
                              name="Private",
                              subnet_type=ec2.SubnetType.PRIVATE_ISOLATED,
                              cidr_mask=20
                          )
                          ],
                      nat_gateways=1)

        # Free tier-eligible instance type
        instance_type = ec2.InstanceType.of(ec2.InstanceClass.BURSTABLE2, ec2.InstanceSize.MICRO)

        # Create RDS Instance
        rds = aws_rds.DatabaseInstance(self, "heathcaredb",
                                       engine=aws_rds.DatabaseInstanceEngine.SQL_SERVER_EE,
                                       instance_type=instance_type,
                                       master_username="admin",
                                       master_user_password="akshay123",
                                       vpc=vpc,  # Specify your VPC
                                       vpc_placement={"subnet_type": ec2.SubnetType.PUBLIC}
                                       )
