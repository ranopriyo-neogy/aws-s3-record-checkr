## About

This project has a lambda function that will generate notification for S3 Bucket that has no records inserted in last 10 days.

## Steps:

1. Clone the project
2. Provide `TopicArn` and `Bucket` as inputs in `.env` file.
3. Execute `sh create_package_attributes.sh` to generate `lambda_function.zip` package.
4. Create a Lambda function with Python 3.9 runtime in AWS console.
5. Create IAM Roles to provide `Read Only Access` to S3 and attach it to the lambda function
6. Create IAM Roles to publish events to SNS Topic and attach it to the lambda function
7. Upload the `.zip` package in the lambda function
8. Create a Rule to execute the lambda function on schedule [AWS Docs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/RunLambdaSchedule.html#schedule-create-rule)

## Developer

- [Ranopriyo Neogy](https://github.com/ranopriyo-neogy)
