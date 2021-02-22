# AWS Serverless Application Model (AWS SAM) example

This project implements an AWS Serverless Application Model service which calculates and displays results for
calculating a Fibonacci number F(n) with the value of n provided by the user.

# Structure

- The algorithm and lambda handler sources are under `src/`
- The unit testes for the algorithms and the integration tests for the API's can be found under `tests/`
- the template for generating AWS resources can be found in `template.yaml`

# Preparing your environment

- Running & verifying the algorithms requires a recent version of python with the dependencies from `requirements.txt`
  installed.
- Deploying & verifying the API's locally requires installing both AWS SAM CLI and docker.
- Deploying the serverless application to AWS requires installing AWS SAM CLI and creating an AIM user with
  Administrator Permissions.

Installing AWS SAM
CLI: https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html

# Verifying the algorithms

- Run the unit tests located under `tests/unit/` to verify the correctness of the algorithms

# Deploying & verifying the API's locally

- Start a local instance of the AWS Serverless App on http://127.0.0.1:3000/  using `sam local start-api`
- Run the integration tests under `tests/integration/` to test the locally deployed API's

# Deploying to AWS & Verifying the API's remotely

- Deploy the serverless application to AWS using `sam deploy --guided`
- Set the environment variable API_BASE_URL to the output of the ApiBaseUrl shown after running the previous step
  example: https://xxxxxxxxx.execute-api.eu-central-1.amazonaSETws.com/Prod/
- Run the integration tests under `tests/integration/` with the above environment variable set to test the remotely
  deployed API's

# Cleanup / Notes

- The AWS SAM CLI creates a new AWS clouformation stack for this application that you can easily delete from the AWS
  CloudFormation web console (https://console.aws.amazon.com/cloudformation).