import requests

# myUrl = "https://jsonplaceholder.typicode.com/users"
# result = requests.get(myUrl)
# result=result.json()
# # for item in result:
# #     if(item["userId"]>4):
# #         print(f"{item["id"]} - {item["title"]}")

# for item in result:
#     print(f"{item["id"]} - {item["address"]["city"]}")

apiKey = '23432'
exchangeCurrency = input("Enter exchange currency")
foreignExchangeReciverd = input("Enter exchange reciverd")
amount = int(input("How much money do you want to exchange"))

apiUrl = f'https://v6.exchangerate-api.com/v6/{apiKey}/latest/{exchangeCurrency}'
result = requests.get(apiUrl)
result = result.json()
newAmount = amount*result["conversion_rates"][foreignExchangeReciverd]
print(f"{amount}{exchangeCurrency} = {newAmount:.2f}{foreignExchangeReciverd}")