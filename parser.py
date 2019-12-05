import re
import json

def parse_image_name(imageName):
    return re.search('\'(.+?)\'',imageName)

def parse_container_id(containerId):
    trimmedContainerList = re.search(': (.+?)>', str(containerId)).group().replace(":","").replace(">","").replace(" ","")
    return trimmedContainerList


##TODO ---- need to define the following methods
def parse_dict_to_json(dictItem):
    return ''

def parse_string_to_json(stringItem):
    return ''