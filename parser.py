from __future__ import print_function
import sys
import re
import json

def parse_image_name(image_name):
    match = re.search('\'(.+?)\'',image_name).group()
    match = match.rstrip('\'').lstrip('\'')
    return match

def parse_container_id(containder_id):
    trimmedContainerList = re.search(': (.+?)>', str(containder_id)).group().replace(":","").replace(">","").replace(" ","")
    return trimmedContainerList

def parse_dict_to_string(dict_item):
    return json.dumps(dict_item)

def parse_string_to_dict(string_item):
    return json.loads(string_item)

def parse_elements_to_response(name_item, string_item, message_item):
    print(type(string_item), file=sys.stderr)
    if string_item == '':
        return {"name" : name_item, "value" : "empty", "message" : message_item}
    if isinstance(string_item, bytes):
        string_item=string_item.decode()
        return {"name" : name_item, "value" : str(string_item), "message" : message_item}
    elif type(string_item) is not str:
        string_item = json.dumps(string_item)
    if "{" in string_item[0]:
        string_payload = "{" + '"name"' + ":" + "\"" + name_item + "\"" +  "," + '"value"' + ":" + string_item + "," + '"message"' + ":" + "\"" + message_item + "\"" + "}"
    else:
        string_payload = "{" + '"name"' + ":" + "\"" + name_item + "\"" +  "," + '"value"' + ":" + "\"" + string_item + "\"" + "," + '"message"' + ":" + "\"" + message_item + "\"" + "}"

    return json.loads(string_payload)