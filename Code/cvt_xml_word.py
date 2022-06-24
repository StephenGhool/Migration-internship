# convert xml to word

import json 
import xmltodict

# returning dict keys as list
def getList(dict):
    return dict.keys()

# Function to return dict of xml file
# Can be used to extract particular segments of the xml file
def xml_to_dict(xml_file):
    # opening xml file and converting to dictionary
    with open(xml_file,encoding="utf8") as xml_file:
        data_dict = xmltodict.parse(xml_file.read())
    xml_file.close()
    return data_dict

# Function to convert dict to json 
def dict_to_json(data_dict):
    # generate the object using json.dumps()
    # corresponding to json data

    json_data = json.dumps(data_dict)
        
    # Write the json data to output
    # json file
    with open("data.json", "w") as json_file:
        json_file.write(json_data)
        json_file.close()
    return json_data

# Functions checks to see if we can acquire images from the xml file
def get_image(context):
    
    return

def main():
    xml_file = "123_plan.xml"
    data_dict = xml_to_dict(xml_file)
    # Extraction of key data from data_dict
    mediawiki = data_dict['mediawiki']
    json_data = dict_to_json(data_dict)

    # output
    print("Page content:",mediawiki['page']['revision']['text']['#text']) # this prints the main content
    print("Page content data type:",type(mediawiki['page']['revision']['text']['#text']))
if __name__=="__main__":
    main()
