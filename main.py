import re
import sys

import requests

try:
    from config import API_KEY
except ImportError:
    print('You must create config.py file containing the API_KEY of the https://macaddress.io/ API.')
    exit()

URL = 'https://api.macaddress.io/v1'


def run():
    mac = valid_mac(sys.argv[1])
    while mac is None:
        error_msg = 'Given MAC Address is inappropriate. Type in another address: '
        mac = valid_mac(input(error_msg))

    run_request(mac)


def valid_mac(input_mac):
    if re.match("[0-9a-f]{2}([-:]?)[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$", input_mac.lower()):
        return input_mac
    else:
        return None


def run_request(mac_address):
    try:
        r = mac_address_get(mac_address)
        json_print_company(r)
    except KeyError:
        print('Given API_KEY is inappropriate. Check the key in the file config.py!')
        exit()
    except Exception as ex:
        print('Something went wrong! Error: {err}'.format(err=str(ex)))
        exit()


def mac_address_get(mac_address):
    payload = {
        'apiKey': API_KEY,
        'search': mac_address,
        'output': 'json'
    }

    return requests.get(URL, params=payload)


def json_print_company(json_response):
    fetched_json = json_response.json()
    requested_mac = fetched_json['macAddressDetails']['searchTerm']
    company = fetched_json['vendorDetails']['companyName']
    msg = 'MAC address: {mac} \n' \
          'Company Name: {company}'.format(mac=requested_mac,
                                           company=company)
    print(msg)


if __name__ == '__main__':
    run()
