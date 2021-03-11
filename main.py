import distutils.util
import re

import requests

try:
    from config import API_KEY
except ImportError:
    print('You must create config.py file containing the API_KEY of the https://macaddress.io/ API.')
    exit()

URL = 'https://api.macaddress.io/v1'


def run():
    keep_working = True
    while keep_working is True:
        msg = 'Type the MAC Address (example: 44:38:39:ff:ef:57): '
        mac = valid_mac(input(msg))
        while mac is None:
            error_msg = 'Given MAC Address is inappropriate. Try again: '
            mac = valid_mac(input(error_msg))

        run_request(mac)
        keep_working = check_continue()


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


def check_continue():
    msg = 'Do you want to check another address? (Yes/No): '
    keep_working = valid_boolean(input(msg))
    while keep_working is None:
        keep_working = valid_boolean(input(msg))

    return keep_working


def valid_boolean(input_arg):
    try:
        return bool(distutils.util.strtobool(input_arg))
    except ValueError:
        print('Input value must be Yes or No.')
        return None


if __name__ == '__main__':
    run()
