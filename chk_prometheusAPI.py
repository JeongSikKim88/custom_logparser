# from json_parser import parser
import json
import csv

# domain_stat = {'domain_name': domain_name, 'data': []}

# stat = {
#     "time": time,
#     "traffic": traffic,
#     "transfer": transfer,
#     "reqcount": reqcount
# }


def chk_data(domain_name, date_from, date_to):

    domain_stat = {'domain_name': domain_name, 'data': []}

    with open(f'{domain_name}.json') as data_file:
        data = json.load(data_file)

    i = 0
    for i in range(len(data['transfer_bps'])):
        time = json.dumps(data['transfer_bps'][i]['time'])
        traffic = json.dumps(data['transfer_bps'][i]['i.011st.com'])
        transfer = json.dumps(data['transfer_byte'][i]['i.011st.com'])
        reqcount = json.dumps(data['request_count'][i]['i.011st.com'])
        # print(json.dumps(data['transfer_bps'][i]['i.011st.com']))
        i += 1
        stat =  {
            "time": time,
            "traffic": traffic,
            "transfer": transfer,
            "reqcount": reqcount
        }
        domain_stat['data'].append(stat)
    write_data(domain_stat, domain_name)


def chk_transfer(domain_name):
    with open(f'{domain_name}.json') as data_file:
        data = json.load(data_file)

    i = 0
    sum = 0
    for i in range(0, 287):

        print(json.dumps(data['transfer_byte'][i]['i.011st.com']))
        i += 1


def chk_reqcount(domain_name):
    with open(f'{domain_name}.json') as data_file:
        data = json.load(data_file)

    i = 0
    sum = 0
    for i in range(0, 287):

        print(json.dumps(data['request_count'][i]['i.011st.com']))
        i += 1


def write_data(domain_stat, domain_name):
    file = open(f"{domain_name}.csv", mode="w")
    writer = csv.writer(file)
    writer.writerow(["time", "traffic", "transfer", "reqcount"])
    for item in domain_stat["data"]:
        writer.writerow(list(item.values()))
