from aws_cdk import App
from cdk.cdk_stack import S3Stack

app = App()

S3Stack(app, "dev-heathcare-data-ingestion-pipeline")

app.synth()