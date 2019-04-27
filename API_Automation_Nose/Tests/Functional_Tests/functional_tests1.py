import requests
import json
from API_Automation_Nose.Lib.Rest_library import Request_maker

# For a simple Get Request with no query strings, the server should respond with a status code between 200-299
def response_code_test():
    output_response =Request_maker.request_maker(endpoint_url='/', request_method='get')
    # assert output_response['status_code>= 200 and response.status_code <= 299, 'Response code is not between 200 to 299 which we expect'
    print(output_response)
    assert output_response['exit_status_code'] >= 200 and output_response['exit_status_code'] <=299, 'Response code is not between 200 to 299 which we expect'

# If we request a status code using the request_status_code query string, the same status code must be returned by server
def response_code_passing_test():
    dict1 = {
        'requested_response_code': 400
    }
    output_response = Request_maker.request_maker(endpoint_url='/', request_method='get', params = dict1)
    if output_response['exit_status_code'] ==200:
        if 'Message' in output_response and output_response['Message'] =='Unauthorised Request':
            print('Unauthorised request due to requested response code is 400')
        assert output_response['exit_status_code'] ==dict1['requested_response_code'] and output_response['exit_status_code'] != 400, 'Requested response code not equas to what server has sent'
    else:
        raise AssertionError



def sleep_query_test():
    dict1 ={
        'please_wait_for' :3
    }
    output_response = Request_maker.request_maker(endpoint_url='/', request_method='get', params = dict1)
    if 'Message' in output_response:
        if output_response['exit_status_code'] == 400 and output_response['Message'] == "Wait time of more than 10 seconds can not be expected":
            print("passed")
        else:
            raise AssertionError

# Server reply validation : 4 Keys with correct names
def keys_present_test():
    output_response = Request_maker.request_maker(endpoint_url='/', request_method='get')
    # print(type(response.text))
    # print(response.text)
    length = len(output_response.keys())
    print(length)
    is_pass = False

    if 'your_ip' in output_response['response_dict'] and 'randomvalue1' in output_response['response_dict'] and 'randomvalue2' in output_response['response_dict'] and 'randomvalue3' in output_response['response_dict']:
        is_pass = True
    assert is_pass, "The server responded with less than 4 keys in the response JSON"


def key_check_test():
    output_response = Request_maker.request_maker(endpoint_url='/', request_method='get')
    # print(dict1)
    is_pass= False
    if 'randomvalue1' in output_response['response_dict'] and 'randomvalue2' in output_response['response_dict'] and 'randomvalue3' in output_response['response_dict']:
        if (output_response['response_dict']['randomvalue1'] is True or output_response['response_dict']['randomvalue1'] is False) and (len(str(output_response['response_dict']['randomvalue2'])) == 2) and (len(output_response['response_dict']['randomvalue3']) ==10):
            is_pass = True
    assert is_pass, "Invalid values of the 3 keys Found"


