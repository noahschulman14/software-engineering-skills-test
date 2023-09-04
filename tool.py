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

p.pprint(leaves)
print()

# Then iterate through all the leaves, make a list of their bound attributes
for leaf in leaves:
    print(leaf.attrib["bounds"])

            


