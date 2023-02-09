# CPS491S23-Team09
University of Dayton CPS 491 Team09 Capstone IRoomba Control 

Capstone II Proposal

University of Dayton

Department of Computer Science

CPS 490 - Fall 2022

+ Dr. Nick Stiffler (2022 - )
+ Dr. Phu Phung (2018 - 2021)


# Project Topic
Robotics Web server hosted by Raspberry Pi

# Team members


1. Amanda Bolden, boldena2@udayton.edu
2. Alejandro Ruiz, ruiza9@udayton.edu
3. Christopher Eustace, eustacec2@udayton.edu



# Company Mentors

Dr.Nicholas Stiffler, University of Dayton Professor;


University of Dayton

300 College Park Dayton OH 45409

## Project homepage

https://github.com/Mastery01/CPS491S23-Team09


# Overview

For CPS 491 Capstone II we will be creating a web interface that will be hosted by a Raspberry PI.
We are creating this to help the robotics department with their in class demonstrations with the
iRobot Roomba without having to interject code. In doing so at the end of this project there will be
a web interface that will act as a simple control on a server with game like functionality on
order to generate interest in robotics.

![Overview Architecture](https://iili.io/Hoh0kQV.md.png "A overview of a proposed 4-layer Architecture")

Figure 1. - A Sample of Overview Architecture of the proposed project.

# Project Context and Scope
This Robotics web interface will be used within the University of Dayton Robotics Lab run by Dr.Nicholas Stiffler.
The motivation behind this project is to increase undergraduates students interest in robotics. As this project will
be used within the University of Dayton CPS 499 Robotics class. The students in the CPS 499 Robotics class will interact
with the web interface in order to program the Roomba robots

## Public Facing Website
Just a demo page for a Bitbucket homepage.
To be updated with your team and CPS 490 Messenger demo.
We will keep this page updated each sptint during the Spring semster.
A video demo will be included.
[Team10Website](https://Mastery01.github.io/CPS491S23-Team09)
![Team 10 Website](https://iili.io/HohkPh7.md.png "Team 9 Public Website")

# High-level Requirements

1. Users will be able to log in to the web page
2. Users will be able to interact with a web page that will connect to the robot
3. Web page will have buttons that users can use to control the Roomba
4. Users will be able to control the Roomba using arrow buttons on a website
5. Users will be able to conduct a simple wall following by controlling the Roomba using arrow keys on the web page

# Technology
You also need to mention if there are any technical support and preferences from the company and if they provide an existing version of the application.
For this project we will be using multiple development tools
The main component of this project is the web interface. Since we are creating a web interface that will be used by students. We will be implementing a login use case
so that only students within the CPS 499 Robotics class will be able to access the web page. We will also be implementing a database to store the students username and passwords
in order to do validation checks. To do this we will be programming in HTML, Javascript, and Python, for testing we will be using a Raspberry PI and the Roomba iRobot.
We will do all of our development within Google Cloud Shell and will use MongoDb for our database. We will use Bitbucket.io as our remote repository. Version control is how we will make sure that our local and remote
repository are connected to each other and our work is saving.

## Hardware
1. Raspberry PI
2. Roomba iRobot

![Hardware](https://iili.io/Hoh13Zl.md.png "An image of an Raspberry PI")
![Hardware](https://iili.io/Hoh1NcX.md.png "An image of an Roomba")

## Programming Languages
1. HTML (Front-end)
2. Javascript (Front-end)
3. Python (Back-end)

# Deployment environments
1. Google Cloud Shell
2. MongoDb


# Impacts

Setting up a server with the Raspberry Pi to run demonstrations with the iRobot without injecting code. This will help us create a simple control on a server with a game-like functionality.  
Raspberry pi:
-	Low costing
-	Nearly all the software is open source
-	Uses Linux and python 
-	Makes the technology behind computers seem more accessible
-	Connects Roomba to server
iRobot Roomba:
-	Backend Hardware
-	Pi can Connect remotely over Wi-Fi network from the computer

# Project Management

For this project we will be using a Scrum approach. We will be using Trello, Slack, and Bitbucket for project management. Below are the links to our
Trello and bitbucket.
1. Trello: https://trello.com/b/ZLegHB04/cps-491-capstone
2. Github: https://github.com/Mastery01/CPS491S23-Team09

![Spring 2022 Timeline](https://capstones-cs-udayton.bitbucket.io/imgs/cps491timeline.png "Spring 2022 Timeline")

Below is an image of our teams timeline from our Trello Board (with tasks).
![Trello Board](https://iili.io/Ho8Sj3l.md.png "Team 10 Trello Board")

Below is an image of our teams temporary gnatt chart. 
![Gnatt Chart](https://iili.io/Ho8SX44.md.png "Team 10 Temporary Gnatt Chart")

Below is an image of our temas slack channel which we will be using for the semester for team communiations. 
![Slack image](https://iili.io/Ho84qoF.md.png "Team 10 Slack")

Below is an image of our teams Trello board timeline (Gantt chart) with sprint cycles but without tasks for Spring 2022:
![Spring 2022 Timeline on Trello](https://capstones-cs-udayton.bitbucket.io/imgs/trello.png "Spring 2022 Timeline")


# Company Support

Based on our discussions with the Dr.Nicholas Stiffler professor at the University of Dayton Robotics lab. We will have check in's with
Dr.Stiffler twice a week. We will communicate with him via email, slack, and in person at the University of Dayton. Our client will support
our team by meeting with us to provide requirements for their project. Allow us to ask questions in order to gain more information about the project
or any problems we might have during the semester. The close proximity of our client puts us in the unique position to be able to ask questions
and meet in person more than the average client that is at a different location.
