import requests
import json
from API_Automation_Nose.Lib.Rest_library import Request_maker

# Check if server handles inappropriate status code
def passing_string_status_test():

    dict1 = {
        'requested_response_code': 20
    }
    output_response = Request_maker.request_maker(endpoint_url='/', request_method='get', params=dict1)
    if 'message' in output_response:
        # assert invalid['Message'] =='Invalid status code requested'
        assert output_response['message'] !='Internal server error'
    if output_response['exit_status_code'] == 400:
        if 'Message' in output_response and output_response['Message'] == 'Unauthorised Request':
            raise AssertionError

def sleep_checking_test():
    dict1 = {
        'please_wait_for': -1
    }
    output_response = Request_maker.request_maker(endpoint_url='/', request_method='get', params=dict1)
    # print(invalid)
    if 'message' in output_response:
        assert output_response['message'] !='Internal server error'
    if 'Message' in output_response and output_response['Message'] =='Unauthorised Request':
        raise AssertionError

