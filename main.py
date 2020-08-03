import os
import json
import requests
from exporter import save_to_file
from chk_prometheusAPI import chk_data
from flask import Flask, render_template, request, redirect, send_file


url = "https://userapi.myskcdn.net/v1/stats/service_traffic"
# url = "https://userapi.xdn.kr/v1/stats/service_traffic"
headers = {"Authorization": "Token 1bf0c39780a9f3f3643ed88681ea1bd448eaa9d2"}
# data = {'date_from': '2020-07-26',
#         'date_to': '2020-07-27', 'domain_name': 'i.011st.com'}
# data = {"date_from=2020-07-14&date_to=2020-07-14&domain_name=i.011st.com&time_unit=1m"}

app = Flask("SuperScrapper")

db = {}


@app.route("/")  # placeholder
def potato():
    return render_template("index.html")


@app.route("/report")
def report():
    domain_name = request.args.get('domain')
    date_from = request.args.get('date_from')
    date_to = request.args.get('date_to')

    if domain_name:
        domain_name = domain_name.lower()

        print(domain_name)

        data = parser(domain_name, date_from, date_to)
        db[domain_name] = data
    else:
        return redirect("/")
    return render_template("report.html",
                           domain_name=domain_name,
                           data=data
                           )


@app.route("/export")
def export():
    try:
        domain = request.args.get('domain')
        date_from = request.args.get('date_from')
        date_to = request.args.get('date_to')
        if not domain:   
            raise Exception()
        domain = domain.lower()
        save_to_file(domain, date_from, date_to)
        return send_file(f"{domain}?date_from=?date_to.csv")
    except:
        return redirect("/")


def parser(domain_name, date_from, date_to):
    domain_stat = []
    data = {'date_from': f'{date_from}',
            'date_to': f'{date_to}', 'domain_name': f'{domain_name}', 'time_unit': '1m'}

    req = requests.post(url, headers=headers, data=data).json()

    json_data = json.dumps(req)
    j_file = open(f"{domain_name}.json", "w")
    j_file.write(json_data)

    with open(f"{domain_name}.json") as json_file:
        json_data = json.load(json_file)

    # with statement
    with open(f"{domain_name}.json", 'w') as out_file:
        json.dump(json_data, out_file, indent=4, sort_keys=True)

    with open(f'{domain_name}.json') as data_file:
        data = json.load(data_file)

    for i in range(len(data['transfer_bps'])):
        time = json.dumps(data['transfer_bps'][i]['time'])
        traffic = json.dumps(data['transfer_bps'][i][f'{domain_name}'])
        transfer = json.dumps(data['transfer_byte'][i][f'{domain_name}'])
        reqcount = json.dumps(data['request_count'][i][f'{domain_name}'])
        # print(json.dumps(data['transfer_bps'][i]['i.011st.com']))
        i += 1
        stat = {
            "time": time,
            "traffic": traffic,
            "transfer": transfer,
            "reqcount": reqcount
        }
        domain_stat.append(stat)

    return domain_stat


if __name__ == '__main__':
    # main()
    app.run(host="0.0.0.0", port=2750)
