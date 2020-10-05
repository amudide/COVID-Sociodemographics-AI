import requests
import json

def main():
    counter = 0
    with open('healthcenters.txt') as json_file:
        data = json.load(json_file)
        for center in data['data']:
            print(counter)
            base = "https://sandbox-api.va.gov/services/va_facilities/v0/facilities/" + center
            header = {"apikey": "DY2MFD54SbcBhBKkqDwbUzg3fH4SKreZ"}
            res = requests.get(base, headers=header)
            file = "data/" + center + ".txt"
            open(file, 'wb').write(res.content)
            counter += 1

if __name__ == "__main__":
    main()