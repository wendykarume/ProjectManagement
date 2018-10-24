# Project Management System
## Introduction.
##### Managing Projects For you.

## Getting Started.
###### Operating System - Ubuntu Linux 18.04 - Bionic Beaver
###### Python Version - 3.6

### Open terminal/bash and input:

#### Prerequisites & Setup:

###### If git is not yet installed.
    sudo apt-get install git

Otherwise,

    https://github.com/wendykarume/project_schedule_system.git

###### Extract the application from the github repository.

    cd project_schedule_system/ProjectManagement/

###### Access the application and it's contents.
[All the terminal commands are to be done while in this directory]

###### ZoneZero/

#### Application Setup:

###### Install pip in order to install various requirements needed by the application.
    sudo apt-get install virtualenv

###### Use pip to install a virtual environment for running the application.
    sudo apt-get install python3-pip

###### Create a new virtual environment that will be used to run the application without tampering with your system's various installed modules.
    virtualenv venv

###### Activate your virtual environment.
    . venv/bin/activate

###### Install all the requirements needed to run the application found in the requirements.txt file.
    pip install -r requirements.txt

###### Run the application.
    `python run.py`
