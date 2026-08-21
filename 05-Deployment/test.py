import requests

url = 'http://localhost:9696/predict'

customer_1 = {
   "gender":"female",
   "seniorcitizen": 0,
   "partner":"yes",
   "dependents":"no",
   "phoneservice":"no",
   "multiplelines":"no_phone_service",
   "internetservice":"dsl",
   "onlinesecurity":"no",
   "onlinebackup":"yes",
   "deviceprotection":"no",
   "techsupport":"no",
   "streamingtv":"no",
   "streamingmovies":"no",
   "contract":"month-to-month",
   "paperlessbilling":"yes",
   "paymentmethod":"electronic_check",
   "tenure": 24,
   "monthlycharges": 29.85,
   "totalcharges": (24 *29.85)
}


customer_2 = {
   "gender":"female",
   "seniorcitizen": 0,
   "partner":"yes",
   "dependents":"no",
   "phoneservice":"no",
   "multiplelines":"no_phone_service",
   "internetservice":"dsl",
   "onlinesecurity":"no",
   "onlinebackup":"yes",
   "deviceprotection":"no",
   "techsupport":"no",
   "streamingtv":"no",
   "streamingmovies":"no",
   "contract":"month-to-month",
   "paperlessbilling":"yes",
   "paymentmethod":"electronic_check",
   "tenure": 1,
   "monthlycharges": 29.85,
   "totalcharges": 29.85
}

response = requests.post(url, json=customer_1).json()

response

if response['churn'] == True:
    print('sending promo email to', 'asdx-123d')
else:
    print(f'Customer not churning: do not send promo email')

