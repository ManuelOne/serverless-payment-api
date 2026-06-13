import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Payment-Transactions')

def lambda_handler(event, context):
    notification = json.loads(event['body'])

    print(f"Processing payment: {notification}")

    amount = notification.get('amount', 0)

    if amount <= 0:
        raise Exception("Invalid amount")

    sender = notification.get('sender', 'Unknown')
    recipient = notification.get('recipient', 'Unknown')

    table.put_item(
        Item={
            'TransactionID': notification['reference'],
            'Timestamp': notification['timestamp'],
            'Sender': sender,
            'Recipient': recipient,
            'Amount': str(amount),
            'Status': 'Completed'
        }
    )

    print(f"Payment of NGN {amount:,.2f} processed successfully")

    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': 'Payment processed successfully'
        })
    }