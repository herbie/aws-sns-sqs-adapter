# AWS SNS/SQS Adapter

This Adapter is based on Django and provides a way to publish messages to AWS SNS/SQS. 

The default configuration creates a single SNS Topic on which a single SQS Queue subscribes for new messages.

An example [SQS consumer](example_consumer) is also available.

It is meant to be used with [Herbie](https://github.com/herbie/herbie).

## Getting started

#### Using with Herbie

The package already provides a Django app that just needs to be registered in the main Django app using Herbie.

1. Add the package to the project _requirements.txt_

CHANGE LATER WHEN PUBLISHED
```
    git+https://github.com/herbie/aws-sns-sqs-adapter@packaging
```

2. Update the requirements
```
    pip install -r requirements.txt -U
```

3. Add the adapter App to Django Installed Apllications:

```
INSTALLED_APPS = [
    ...
    'aws_sns_sqs_adapter.apps.HerbieGooglePubsubAdapterConfig',
    ...
]
```

4. Run command to create the SNS/SQS Topics/Queues according to the schemas available. 
This command will create 1 SNS Topic and 1 SQS Queue per schema available; the queue will subscribe to the respective created topic.

```
python manage.py init_sns_sqs
```

An example Django application using this adapter can be found at the [Herbie Sandbox](https://github.com/herbie/sandbox) repository.
