import csv


def save_to_file(domain):
    file = open(f"{domain}.csv", mode="w")
    writer = csv.writer(file)
    writer.writerow(["time", "traffic", "transfer", "reqcount"])
    # for item in domain:
    #     writer.writerow(list(item.values()))
    # return
