import requests
import json

def main():
    counter = 0
    num_bad = 0
    with open('healthcenters.txt') as json_file:
        data1 = json.load(json_file)
        for center in data1['data']:
            print(counter)
            base = "https://sandbox-api.va.gov/services/va_facilities/v0/facilities/" + center
            header = {"apikey": "DY2MFD54SbcBhBKkqDwbUzg3fH4SKreZ"}

            file = "data/" + center + ".txt"
            with open(file) as json_file:
                data = json.load(json_file)
                
                if ("message" in data):
                    if data["message"] == "API rate limit exceeded":
                        num_bad += 1
                        res = requests.get(base, headers=header)
                        open(file, 'wb').write(res.content)

            #res = requests.get(base, headers=header)
            #open(file, 'wb').write(res.content)
            counter += 1
    print(num_bad)
    print(counter)

if __name__ == "__main__":
    main()