import os
import json
import requests
from bs4 import BeautifulSoup


url = "https://userapi.myskcdn.net/v1/stats/service_traffic"
# url = "https://userapi.xdn.kr/v1/stats/service_traffic"
headers = {"Authorization": "Token 3ffc0d2d9927e33a8bcb6502998609b3014b548c"}
data = {'date_from':'2020-07-24', 'date_to':'2020-07-25','domain_name':'i.011st.com'}
# data = {"date_from=2020-07-14&date_to=2020-07-14&domain_name=i.011st.com&time_unit=1m"}

def main():
    # domain_name = input("Domain Name : ")
    req = requests.post(url, headers=headers, data=data)
    res = BeautifulSoup(req.text, "html.parser")
    print(type(res))
    parser(res)


def parser(res):
    json_data = json.load(res)
    print(json_data)
    # json.dump(json_data, indent=4, sort_keys=True)
    # print(json.dumps(json_data, indent=4, sort_keys=True))


if __name__ == '__main__':
    main()
