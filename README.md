# Serverless Payment API

![AWS Lambda](https://img.shields.io/badge/AWS-Lambda-orange)
![Python](https://img.shields.io/badge/Python-3.12-blue)
![Serverless](https://img.shields.io/badge/Architecture-Serverless-green)

## Overview
This project is a serverless payment processing API built using AWS services. It processes payments via API Gateway, stores transactions in DynamoDB, and triggers notifications using Lambda and SNS.

---

## Architecture
The system uses:
- API Gateway → Receives payment requests
- AWS Lambda → Processes logic
- DynamoDB → Stores transactions
- SNS → Sends alerts for high-value transactions

---

## How to Deploy
1. Create DynamoDB table: `Payment-Transactions`
2. Deploy Lambda function using `lambda_function.py`
3. Attach IAM permissions (DynamoDB + SNS)
4. Connect API Gateway to Lambda
5. Deploy API stage

---

## API Usage

**Endpoint:**
