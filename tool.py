import xml.etree.ElementTree as ET
import pprint as p


tree = ET.parse('/Users/noah/Desktop/software-engineering/skills-test/Programming-Assignment-Data/com.apalon.ringtones.xml')
root = tree.getroot()

# The root.iter() method recursively iterates through all the sub-elements of root
# To find the leaf elements, just save the elements with no children (length 0) to a list
def find_leaves(root):
    leaves = [] 
    for element in root.iter():
        if len(element) == 0:
            leaves.append(element)
    return leaves

leaves = find_leaves(root)

# Parse the bounds attribute of each of the leaf elements into a list of tuples so Pillow can use the bounds
bounds = []
for leaf in leaves:
    bound = leaf.attrib["bounds"].strip('[]').split('][')
    bound_list = []
    for coordinate in bound:
        split = coordinate.split(",")
        bound_list.append((int(split[0]), int(split[1])))
        
    bounds.append(bound_list)


# TODO: need to iterate over those parsed bounds and create a yellow rectangle for each of them on the image
# TODO: need to figure out taking the files in as pairs, and going through all those pairs and the output and shazz

            


