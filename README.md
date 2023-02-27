# Samantha Voice Assistant

**BROKEN, STILL IN PROGRESS, PLEASE BE PATIENT WITH ME AS THIS IS PLANNED TO TAKE A LONG TIME**

All of the Samantha code for her Voice Assistant! A fully functional (Kind of, Still a WIP) voice assistant with many commands! This Version has Machine Learning in progress. I have made all of this. This is all my hard work and I care about it a lot. Please use with care. Any modifications to code on main branches should be approved by me. 

## Machine Learning Portion
***
The part of the machine learning in this branch takes any input you give it to learn and develop its own more human output. I also plan to have it learn from your input to come up with its own output. This is still in the works and is not yet implemented. Much of this branch is broken and will not work. I am working on it and will update it when I can. Please be patient with me as this will take quite a while to complete. This is my first time working with Machine Learning and I am still learning. I will update this README when I have more information on the progress of the machine learning portion of this project.

## Installation
***
Install dependencies with ```pip install -r requirements.txt``` in the main folder (There has been problems with requirement installation, Requirements are as follows: google, playsound, pyttsx3, requests, and textblob. I would suggest using [Anaconda](https://www.anaconda.com/products/distribution "Anaconda Home") for the installation and running of the program)
<br /><br />
Before running her you will want to use ```python3 checkvoices.py``` to check what voices are on your system. As this is still in the testing phase the Final voice is not yet availible. you will want to select one of the voices from the ones generated and it will edit voice.txt to run the voice you select.

## Running the Program
***
Before running her you will want to use ```python3 checkvoices.py``` to check what voices are on your system and select one for use. As this is still in the testing phase the Final voice is not yet availible. you will want to select one of the voices from the ones generated and it will edit voice.txt to run the voice you select.
<br /><br />
To Run the voice assistant run ```python3 main.py``` or use one of the executable files (**WIP, EXECUTABLES NOT YET AVAILABLE**) made for your operating system.

## Using the Program
***
**Throughout her use Keep your eyes on your terminal, there are intervals where she will be processing and cannot hear you. The terminal tells you when she is not listening and is processing.** 
<br /><br />
You can start the command proccess by using her wakeup word! "Sam" will wake her up and have her listen for commands. There is a gap between the wakeup word and the command input so remember to watch the terminal The Program has a specific list of commands you can use. It will try to guess what command you meant if the command you use is not in the list and is similar to one that is in the list.
<br /><br />
**COMMAND LIST:**
* end - shuts down the program
* flip - flips a coin
* joke - tells a joke
* roll - rolls a dice based on a specified number
* timer - sets a timer for a specified time
* time - tells the time
* add - adds multiple numbers
* subtract - subracts multiple numbers
* multiply - multiplies multiple numbers
* divide - divides multiple numbers
* search - searches google for a prompt
* image - searches google images for a prompt
* app - opens an app on your computer

![Code Size](https://img.shields.io/github/languages/code-size/SpectraDevTeam/SamanthaVA_ML) ![]()