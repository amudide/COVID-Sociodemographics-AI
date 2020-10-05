import requests

def main():
    base = "https://sandbox-api.va.gov/services/va_facilities/v0/ids?type=health"
    header = {"apikey": "DY2MFD54SbcBhBKkqDwbUzg3fH4SKreZ"}

    #res = requests.get("")
    res = requests.get(base, headers=header)
    print(res.text)
    open('healthcenters.txt', 'wb').write(res.content)

if __name__ == "__main__":
    main()