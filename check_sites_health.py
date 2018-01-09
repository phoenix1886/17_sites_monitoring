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
    request = requests.get(url)
    if request.status_code == 200:
        return True
    else:
        return False


def is_expiration_in_month(date_time):
    if isinstance(date_time, list):
        time_left = min(date_time) - datetime.now()
    else:
        time_left = date_time - datetime.now()
    return True if time_left.days < 31 else False


def get_domain_expiration_date(url):
    whois_obj = whois.whois(url)
    return whois_obj.expiration_date


if __name__ == '__main__':
    domains_file_path = parse_arguments()
    sites_to_check = load_urls4check(domains_file_path)
    for site_url in sites_to_check:
        print('*' * 50)
        print('Checking {}'.format(site_url))
        print('\tServer respond with 200: {}'.format(
            is_server_respond_with_200(site_url)))

        expiration_date = get_domain_expiration_date(site_url)
        print('\tExpiring in month: {}\n'.format(
            is_expiration_in_month(expiration_date)))
