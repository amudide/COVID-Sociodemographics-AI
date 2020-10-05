import requests
import json
import glob
import pandas as pd

def main():
    files = glob.glob("./data/*.txt")

    places = []

    for file in files:
        with open(file) as json_file:
            data = json.load(json_file)
            try:
                cur = []
                cur.append(file[7:-4]);
                cur.append(data['data']['attributes']['address']['physical']['address_1'])
                cur.append(data['data']['attributes']['address']['physical']['city'])
                cur.append(data['data']['attributes']['address']['physical']['state'])
                cur.append(data['data']['attributes']['address']['physical']['zip'])
                places.append(cur)
            except KeyError:
                pass

    df = pd.DataFrame(places, columns=['VA Station Number', 'Address', 'City', 'State', 'Zip'])
    df.to_csv('locations.csv', index=False)

if __name__ == "__main__":
    main()