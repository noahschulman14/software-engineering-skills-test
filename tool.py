import xml.etree.ElementTree as ET
from PIL import Image, ImageDraw
import os

# Take in location of xml/png file pair directory
directory = input("Enter path for input files directory: ")

file_pairs = {}
for file_name in os.listdir(directory):
    # ignore hidden files/directories
    if file_name.startswith('.'):
        continue
    # split the full file name into the file name and file extension
    name, extension = os.path.splitext(file_name)
    # If the file name is already in the pair dictionary, append this file to the pair list
    if name in file_pairs:
        file_pairs[name].append(file_name)
    # Else, create a new dictionary entry for this file name, make the value a list with the file name
    else:
        file_pairs[name] = [file_name]


# Iterate through each of the file pairs
for pairs in file_pairs.keys():
    pair_values = file_pairs[pairs]
    for file in pair_values:
        # Identify which of the files in the pair is the xml/png
        if file.endswith(".xml"):
            xml = directory + "/" + file
        else:
            png = directory + "/" + file

    # Parse the xml file
    tree = ET.parse(xml)
    root = tree.getroot()
    
    # The root.iter() method recursively iterates through all the sub-elements of root
    # To find the leaf elements, just save the elements with no children (length 0) to a list
    leaves = [] 
    for element in root.iter():
        if len(element) == 0:
            leaves.append(element)

    # Parse the bounds attribute of each of the leaf elements into a list of tuples so Pillow can use the bounds
    bounds = []
    for leaf in leaves:
        bound = leaf.attrib["bounds"].strip('[]').split('][')
        bound_list = []
        for coordinate in bound:
            split = coordinate.split(",")
            bound_list.append((int(split[0]), int(split[1])))
        bounds.append(bound_list)

    # apply yellow rectangles for each of the leaf bounds to the png

    image = Image.open(png)
    draw = ImageDraw.Draw(image)
    for bound in bounds:
        draw.rectangle(bound, outline="yellow", width = 5)


    # Save the modified image to output directory
    image.save(f"./output/{pairs}-output.png")

