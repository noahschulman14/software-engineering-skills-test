# software-engineering-skills-test

## Instructions

1. After cloning and opening this repo, run the following code:

    ``` pip install -r requirements.txt ```
2. Run the program by entering ```tool.py``` into your command line
3. The program will prompt you to enter the path of the directory that has the input file pairs, paste this into your command line when prompted
4. The output screenshot files will then be generated and placed into the "output" folder

## Description of code

I first ask for the user to input the path of their directory with the input files.

I then group the files into pairs.

Then for each of those file pairs:
1. I parse the xml file and identify the leaf elements using the xml.etree.ElementTree package.
2. I identify the bound attributes of each of the leaf elements.
3. I draw yellow rectangular outlines according to the bound values on a copy of the screenshot png image.
4. I save the modified screenshot copy to the output folder

