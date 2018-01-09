# Sites Monitoring Utility
The script monitors the sites for response code status and expiration date.
It checks whether site is expiring in month, and whether http response status is 200.

To run the script python3.5 is requierd.
Side packages are listed in requirements.txt. To install packages run the following command in shell:
```bash
pip install -r requirements.txt
```

The script takes one positional argument:
* path - the path to file, containing urls of sites for monitoring

## Example of file content
```
https://lenta.ru
https://www.championat.com
https://devman.org
https://yandex.ru
```

# How to run the script
```
$ python check_sites_health.py './sites.txt' 
**************************************************
Checking https://lenta.ru
	Server respond with 200: True
	Expiring in month: False

**************************************************
Checking https://www.championat.com
	Server respond with 200: True
	Expiring in month: False

**************************************************
Checking https://devman.org
	Server respond with 200: True
	Expiring in month: False

**************************************************
Checking https://yandex.ru
	Server respond with 200: True
	Expiring in month: False

```

# Project Goals
The code is written for educational purposes. Training course for web-developers - DEVMAN.org
