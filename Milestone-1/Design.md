
# Milestone 1. Project Plan Complete - Design


## PROJECT INFO

* [Software Project Plan - ElbowSpace ](Index.md)

* Other Roles - [Requirements.md](Requirements.md)
, [Design.md](Design.md)
, [Code.md](Code.md)
, [Test.md](Test.md)

* File: Milestone-1/Design.md

* URL: https://github.com/ElBowSpace/ElBowSpaceProject/blob/master/Milestone-1/Design.md

* Git Repo: https://github.com/ElBowSpace/ElBowSpaceProject




### Milestone 1. Project Plan Complete



Role: Designer - Design

Goal: Technology selection

* Select Development Tools
* Infrastructure - Frameworks & Tools
* Setup Guide
* Create "Hello World"
* Decide on App deployment



## ElbowSpace - Technology selection

Selecting the correct technology is the first important technical decision on any project.
ElbowSpace is a web service that will support both desktop and mobile web clients.
The technology to be used should be optimized for rapid web development.

### Technology Alternatives

Existing Commercial Product 

Before starting any project it is important to understand the competitive landscape.  
Are there any commercial products available that could be used instead of building a new
software. Building software will be at least ten times more expensive that buying an
existing product.

There are some competitive products in the market but there is nothing that will satisfy 
the client needs.  We will be building software to create the ElbowSpace application.
It is important to the client to own the intellectual property so that the application can be
sold to another business.

Web Development Framework

There are several web development frameworks available that will all meet the project needs.
Strong consideration was given to the following frameworks.

* ASP.net - Microsoft web development 
* Ruby on Rails - Strong developer community
* Python with Django - Strong developer community, security, popularity
* Node with React and Mongo DB - Thriving community and very popular


### Select Development Tools

Criteria for Technology Selection

* Fitness of the tool for the job
* Experience of the development team with the technology
* Components that can be leverage from previous work
* Professional opinion and popularity
* Productivity benchmarks
* Security concerns
* Community of users and developers
* Existing commercial apps that use the technology
* Proof of concept (building a simple app)

After careful consideration a decision was made to create ElbowSpace using the Django
web framework which is written in the Python programming language.

Here are the most important considerations that support this decision:

* The software team does not have enough experience with web frameworks. 
For that reason the software team chose to follow Mark Seaman's steps in the case at some moment assistance
is required.
* The developer team has moderate experience with Python, this could eliminate the need to experiment 
with other programming languages the developer team is not familiar with.
* The new software is very similar to several existing products that have already been
completed, allowing for extensive leverage opportunities.
* Python is growing in popularity and widespread market adoption and Django is the most
popular web framework written in Python.
* Due to the growing popularity of Python and Django, numerous tutorials and forums are 
available on the internet.
* JavaScript is also a good choice (with Node, React, Mongo DB), but the dev team did not
have adequate experience and would need to climb a steep learning curve.
* Django provides first class solutions for Security, Object Relational Mapping, and 
View templates that create amazing productivity.


### Infrastructure - Frameworks & Tools

Framework

    Python 
    Django 
    Virtual Environment
    
Web hosting

    Python Anywhere
    
Dev Tools

    Pycharm Professional  
    Sublime Text           Personal choice
    Brackets 
    
Github

    Git for version control
   
Python Anywhere

    Account:  elbeauspace
    Web URL:  https://elbeauspace.pythonanywhere.com
    

### Setup Guides

* [Tutorial Documents](https://github.com/Mark-Seaman/Mark-Seaman.github.io/blob/master/BookBuilder/docs/Index.md) - 


### Create "Hello World"

* [Hello World](../docs/HelloWorld.md) - This simple app ensures that all of the development 
tools are installed and properly configured.  All developers will do this before any other 
work is done with the code.
* [Code Repo](https://github.com/Mark-Seaman/Book-Builder) - 
Source code is located in "test/hello" directory.


### Decide on App deployment

Alternative Hosting Services

* AWS - Powerful, high-priced, complex initial setup
* Heroku - Turn key solution for Django apps
* Digital Ocean - Simple yet powerful (Shrinking World uses this)
* Python Anywhere - Free accounts available, optimized for Django
* Bluehost - Supports PHP but not Django

ElbowSpace will be using Python Anywhere to do free hosting.  Tutorial documents will show
all developers how to setup and configure a web app.

=======

