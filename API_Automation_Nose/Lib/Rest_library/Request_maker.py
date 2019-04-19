import requests
import json
from API_Automation_Nose.Data import env
from API_Automation_Nose.Lib.Rest_library import Authorizer

@Authorizer.authoriser
def request_maker( endpoint_url, request_method,payload = {}, params = {}, headers={}):
    supported_urls = ['/']
    supported_method_type = ['get', 'post']
    if endpoint_url not in supported_urls:
        raise AssertionError('url is not correct')
    if request_method not in supported_method_type:
        raise AssertionError("request type is incorrect")
    url = env.required_info_dict["address"] + endpoint_url

    if request_method == 'get':
        res = requests.get(url = url, params = params, headers = headers)
    elif request_method == 'post':
        res = requests.post(url = url, data = payload, headers =headers)

    final_response_dict = {
        'exit_status_code' : res.status_code,
        'response_dict': json.loads(res.content)
    }
    return final_response_dict

if __name__ == '__main__':
    output_response = request_maker(endpoint_url= '/' , request_method= 'get')
    print(output_response)


