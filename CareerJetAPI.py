import requests
import numpy as np
from requests.exceptions import HTTPError

# Github link for more description on this API: https://github.com/careerjet/careerjet-api-client-python
projectId = "nth-honor-259919"
key = "5f414fcedee8f11f5c8116653559c13daa2dbe03"

affId = "8acafed2c2c1c95fdd17ea85633d394a"
from careerjet_api_client import CareerjetAPIClient

cj  =  CareerjetAPIClient("en_US");
result_json = cj.search({
                        'location'    : 'seattle',
                        'keywords'    : 'java&python&aws',
                        'pagesize'    : '5',
                        'affid'       : "8acafed2c2c1c95fdd17ea85633d394a",
                        'user_ip'     : '209.141.193.102',
                        'url'         : 'https://www.seekrlabs.com/jobsearch?q=python&l=london',
                        'user_agent'  : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'
                      });

print(result_json)