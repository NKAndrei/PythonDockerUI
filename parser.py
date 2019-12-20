from __future__ import print_function
import sys
import re
import json

def parse_image_name(imageName):
    return re.search('\'(.+?)\'',imageName)

def parse_container_id(containerId):
    trimmedContainerList = re.search(': (.+?)>', str(containerId)).group().replace(":","").replace(">","").replace(" ","")
    return trimmedContainerList

def parse_dict_to_string(dictItem):
    return json.dumps(dictItem)

def parse_string_to_dict(stringItem):
    return json.loads(stringItem)

def parse_elements_to_response(nameItem, stringItem, messageItem):
    print(type(stringItem), file=sys.stderr)
    if stringItem == '':
        return {"name" : nameItem, "value" : "empty", "message" : messageItem}
    if isinstance(stringItem, bytes):
        stringItem=stringItem.decode()
        return {"name" : nameItem, "value" : str(stringItem), "message" : messageItem}
    elif type(stringItem) is not str:
        stringItem = json.dumps(stringItem)
    if "{" in stringItem[0]:
        stringPayload = "{" + '"name"' + ":" + "\"" + nameItem + "\"" +  "," + '"value"' + ":" + stringItem + "," + '"message"' + ":" + "\"" + messageItem + "\"" + "}"
    else:
        stringPayload = "{" + '"name"' + ":" + "\"" + nameItem + "\"" +  "," + '"value"' + ":" + "\"" + stringItem + "\"" + "," + '"message"' + ":" + "\"" + messageItem + "\"" + "}"

    return json.loads(stringPayload)