import json

with open(r"C:\Users\user\Desktop\json_data_file.json", "r") as f:
    data = f.read()  # output will be in a string format
    required_info_dict = json.loads(data)