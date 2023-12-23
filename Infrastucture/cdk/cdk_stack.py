from aws_cdk import (aws_s3 as _s3, Stack, aws_ec2 as ec2)
from constructs import Construct


class S3Stack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        vpc = ec2.Vpc(self, "Healthcare-data-ingestion-pipeline-vpc",
                      cidr='192.168.0.0/16',
                      max_azs=2,
                      subnet_configurations=[
                          ec2.SubnetConfiguration(name="Public",
                                                  subnet_type=ec2.SubnetType.PUBLIC,
                                                  cidr_mask=20)
                      ])


