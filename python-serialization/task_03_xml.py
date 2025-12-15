#!/usr/bin/python3

''' I hate docstring '''

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    ''' I hate docstring '''

    root = ET.Element("data")

    for key, value in dictionary.items():
        item = ET.SubElement(root, "item")
        item.set("key", str(key))

        # Store type info
        if value is None:
            item.set("type", "none")
            item.text = ""
        elif isinstance(value, bool):
            item.set("type", "bool")
            item.text = str(value)
        elif isinstance(value, int):
            item.set("type", "int")
            item.text = str(value)
        elif isinstance(value, float):
            item.set("type", "float")
            item.text = str(value)
        else:
            item.set("type", "str")
            item.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)


def deserialize_from_xml(filename):
    ''' I hate docstring '''

    tree = ET.parse(filename)
    root = tree.getroot()

    result = {}

    for item in root.findall("item"):
        key = item.get("key")
        value_type = item.get("type")
        text = item.text

        if value_type == "int":
            value = int(text)
        elif value_type == "float":
            value = float(text)
        elif value_type == "bool":
            value = text == "True"
        elif value_type == "none":
            value = None
        else:
            value = text

        result[key] = value

    return result

