import requests
import json
equation=input("enter your equation: ")
result="'https://newton.now.sh/api/v2//simplify/"+equation
data=requests.get(result).json()
print("operation for given equation:",data['operation'])
print("expression for given equation:",data['expression'])
print("result of given equation:",data['result'])
