import requests
from concurrent.futures import ThreadPoolExecutor
import time

def post_url(args):
    ts = time.time() * 1000
    print(f'Timestamp: {int(ts)}')
    return requests.post(args[0], data=args[1])
    
form_data = {
    "foo1":"bar1",
    "foo2":"bar2"
}
list_of_urls = [("https://postman-echo.com/post",form_data)]*10


with ThreadPoolExecutor(max_workers=10) as pool:
    response_list = list(pool.map(post_url,list_of_urls))


for response in response_list:
    print(response)