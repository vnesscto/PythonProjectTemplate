import xml.etree.ElementTree as ET

# this module contains functions for reading data from .xml files and .properties files


# this function returns the value of the tag node_name from "../resources/config_settings.xml"
def get_data(node_name):
    # root = ET.parse("../resources/config_settings.xml").getroot()
    # return root.find(".//" + node_name).text
    return get_data_from_xml(node_name)


# this function returns the value of the tag node_name from the .xml file xml_file_path
def get_data_from_xml(node_name, xml_file_path: str = "../resources/config_settings.xml"):
    root = ET.parse(xml_file_path).getroot()
    return root.find(".//" + node_name).text


# this function returns a dictionary containing all the key,value pairs from the given . properties file
# assuming the file does not contain midline comments
def get_property_dictionary(properties_file_path: str = "../resources/elements_repo.properties") -> dict:
    props = {}
    # f = open("../resources/elements_repo.properties", "r")
    f = open(properties_file_path, "r")
    for line in f:
        if line and not line.startswith('#'):
            key_value = line.split('=', 1)
            key = key_value[0].strip()
            value = key_value[1].strip()
            props[key] = value
    f.close()
    return props


# this function returns the value of the given key from the given .properties file
def get_property_value(property_key, properties_file_path: str = "../resources/elements_repo.properties"):
    props = get_property_dictionary(properties_file_path)
    return props.get(property_key)
