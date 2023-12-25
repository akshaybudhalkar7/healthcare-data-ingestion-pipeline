from aws_cdk import (aws_s3 as _s3, Stack, aws_ec2 as ec2, aws_rds,
                     aws_secretsmanager as secretsmanager)
from constructs import Construct


class S3Stack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # vpc = ec2.Vpc(self, "Healthcare-data-ingestion-pipeline-vpc",
        #               cidr='192.168.0.0/16',
        #               max_azs=2,
        #               subnet_configuration=[
        #                   ec2.SubnetConfiguration(name="Public",
        #                                           subnet_type=ec2.SubnetType.PUBLIC,
        #                                           cidr_mask=20),
        #                   ec2.SubnetConfiguration(
        #                       name="Private",
        #                       subnet_type=ec2.SubnetType.PRIVATE_ISOLATED,
        #                       cidr_mask=20
        #                   )
        #                   ],
        #               nat_gateways=1)

        # # Free tier-eligible instance type
        # instance_type = ec2.InstanceType.of(ec2.InstanceClass.BURSTABLE2, ec2.InstanceSize.MICRO)
        # engine_version = aws_rds.MysqlEngineVersion.VER_8_0_28
        #
        # # Create a secret for the password
        # password_secret = secretsmanager.Secret(self, "RdsPasswordSecret",
        #                                         secret_name="my-rds-password")
        #
        # # Create RDS Instance
        # rds = aws_rds.DatabaseInstance(self, "heathcaredb",
        #                                engine=aws_rds.DatabaseInstanceEngine.mysql(version=engine_version),
        #                                instance_type=instance_type,
        #                                vpc=vpc,  # Specify your VPC
        #                                vpc_subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PRIVATE_ISOLATED),
        #                                credentials=aws_rds.Credentials.from_secret(password_secret),
        #                                )

        # subnets = vpc.select_subnets(subnet_type=ec2.SubnetType.PRIVATE_ISOLATED)