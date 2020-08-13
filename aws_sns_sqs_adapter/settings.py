import os
from django.conf import settings

settings.AWS_ACCESS_KEY_ID = os.environ["AWS_ACCESS_KEY_ID"]
settings.AWS_SECRET_ACCESS_KEY = os.environ["AWS_SECRET_ACCESS_KEY"]
settings.AWS_SQS_SNS_REGION = os.environ["AWS_SQS_SNS_REGION"]
settings.AWS_SQS_SNS_ENDPOINT_URL = os.environ["AWS_SQS_SNS_ENDPOINT_URL"]
