from src.algorithms.fibonacci import calculate


def lambda_handler(event, context):
    try:
        n = event['queryStringParameters']['n']

        print(f"Calculating fibonacci for n={n}")
        result = calculate(int(n))

        return {
            "statusCode": 200,
            "body": result,
        }

    except ValueError as error:
        return {
            "statusCode": 400,
            "body": "Bad request: " + str(error),
        }
