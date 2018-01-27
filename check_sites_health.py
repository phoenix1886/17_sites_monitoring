import whois
import requests
from datetime import datetime
import argparse


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('path', help='Path to domains file')
    args = parser.parse_args()
    return args.path


def load_urls4check(path):
    urls = []
    with open(path, 'r') as file:
        for line in file:
            urls.append(line.rstrip())
    return urls


def is_server_respond_with_200(url):
    response = requests.get(url)
    return response.ok


def is_expiration_in_month(expiration_datetime):
    if isinstance(expiration_datetime, list):
        time_left = min(expiration_datetime) - datetime.now()
    else:
        time_left = expiration_datetime - datetime.now()
    return time_left.days < 31


def get_domain_expiration_date(url):
    whois_obj = whois.whois(url)
    return whois_obj.expiration_date


def print_domain_info(site_url, is_response_ok, expires_in_month):
        print('*' * 50)
        print('Checking {}'.format(site_url))
        print('\tServer respond with 200: {}'.format(is_response_ok))
        print('\tExpiring in month: {}\n'.format(expires_in_month))


if __name__ == '__main__':
    domains_file_path = parse_arguments()
    sites_to_check = load_urls4check(domains_file_path)
    for site_url in sites_to_check:
        is_response_ok = is_server_respond_with_200(site_url)
        expiration_datetime = get_domain_expiration_date(site_url)
        print_domain_info(
            site_url,
            is_response_ok,
            is_expiration_in_month(expiration_datetime)
        )
