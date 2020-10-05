import requests
import json
import glob
import pandas as pd

def main():
    files = glob.glob("./data/*.txt")

    important = []

    for file in files:
        with open(file) as json_file:
            data = json.load(json_file)
            try:
                cur = []
                cur.append(file[7:-4]);
                #cur.append(data['data']['attributes']['address']['physical']['address_1'])
                #cur.append(data['data']['attributes']['address']['physical']['city'])
                #cur.append(data['data']['attributes']['address']['physical']['state'])
                #cur.append(data['data']['attributes']['address']['physical']['zip'])
                cur.append(data['data']['attributes']['services']['health'])
                cur.append(data['data']['attributes']['satisfaction']['health'])
                cur.append(data['data']['attributes']['wait_times']['health'])

                if (file[7:-4] == "vha_402"):
                    print(cur)
                important.append(cur)
            except KeyError:
                pass

    df = pd.DataFrame(important, columns=['VA Station Number', 'Services', 'Satisfaction', 'Wait Times'])
    df.to_csv('api-important.csv', index=False)

if __name__ == "__main__":
    main()