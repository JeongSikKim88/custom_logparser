import os
import json
import requests
from bs4 import BeautifulSoup


url = "https://userapi.myskcdn.net/v1/stats/service_traffic"
# url = "https://userapi.xdn.kr/v1/stats/service_traffic"
headers = {"Authorization": "Token 3ffc0d2d9927e33a8bcb6502998609b3014b548c"}
data = {'date_from': '2020-07-26',
        'date_to': '2020-07-27', 'domain_name': 'i.011st.com'}
# data = {"date_from=2020-07-14&date_to=2020-07-14&domain_name=i.011st.com&time_unit=1m"}


def main():
    # domain_name = input("Domain Name : ")
    req = requests.post(url, headers=headers, data=data).json()
    # res = BeautifulSoup(req.text, "html.parser")
    # print(req.json())
    print(type(req))
    parser(req)


def parser(req):
    json_data = json.dumps(req)
    f = open("./test.json", "w")
    f.write(json_data)

    with open('test.json') as json_file:
        json_data = json.load(json_file)

    # with statement
    with open('test.json', 'w') as out_file:
        json.dump(json_data, out_file, indent=4, sort_keys=True)
        print(json.dumps(json_data, indent=4, sort_keys=True))


if __name__ == '__main__':
    main()
