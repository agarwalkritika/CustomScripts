import requests
import json
from API_Automation_Nose.Data import env


def authoriser(func1):
    def urls_test(*args, **kwargs):
        # print ("Inside wrapper")
        response = requests.post(url=env.required_info_dict["auth-url1"], data=json.dumps(env.required_info_dict["payload"]))
        # print(response.content)
        returned_dict = json.loads(response.content)
        # print(returned_dict)
        value = returned_dict['auth_key']
        # print(value)
        headers ={
            'x-auth-token': value
        }
        kwargs['headers'] = headers
        output = func1(*args, **kwargs)
        return output
    return urls_test