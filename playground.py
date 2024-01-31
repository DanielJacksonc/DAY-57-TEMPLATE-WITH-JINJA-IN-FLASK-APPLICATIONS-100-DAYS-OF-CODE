import requests
name = input("What is your name? ")
# age = requests.get(url=f"https://api.agify.io/?name={name}").json()["age"]
# gender = requests.get(url=f"https://api.genderize.io?name={name}").json()["gender"]
# print(f"Hey {name},\nI think your age is {age}\nyou are a {gender}")
# # response = requests.get(url="https://api.npoint.io/4226d56e6f2454c5aa7c").json()
# # print(response)
response = requests.get(url="https://api.npoint.io/4226d56e6f2454c5aa7c").json()
print(response)