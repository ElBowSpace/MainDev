# Elbow Space Project

## PROJECT INFO
* Software Project Plan - ElbowSpace
* Other Roles - [Requirements.md](Requirements.md)
, [Design.md](Design.md)
, [Code.md](Code.md)
, [Test.md](Test.md)

# Milestone 1. - Desig

* File: Milestone-1/Design.md
* URL: https://github.com/ElBowSpace/ElBowSpaceProject/blob/master/docs/plan/Milestone-1/Design.md
* Git Repo: https://github.com/ElBowSpace/ElBowSpaceProject

### Milestone 1. Project Plan Complete
Role: Designer - Design
Goal: Technology selection
* Select Development Tools
* Infrastructure - Frameworks & Tools
* Decide on App deployment


# Milestone 2. Technology Proven - Design

* File: Milestone-2/Design.md
* URL: https://github.com/ElBowSpace/ElBowSpaceProject/blob/master/docs/plan/Milestone-2/Design.md
* Documents: Documents/swplan/BookBuilder
* Git Repo: Mark-Seaman.github.io


### Milestone 2. Technology Proven
Role: Designer - Design
Goal: Software Architecture
## ElBow Space - Software Architecture
### Design Around User Stories
User Stories

* User - C R U D
* Story - C R U D
* Emotes - C R U D
* Image - C R U D

### Design Architecture
* Apps = Data + Views
* The design for the app requires designing the data models
and the Views that will be implemented.

### Milestone 4. Functionality Complete

Role: Designer - Stephen Provost

Goal: Component Design - API; Dataflow Diagram

* Implement Data Models
* Implement Developmental Functionality

### Milestone 3. Core Features Implemented


Role: Designer - Design

Goal: Component Design - API

* Prototype - development spike of core functionality
* Implement data models
* Implement views
* Implement URL routes

### Data Schema
https://github.com/ElBowSpace/ElBowSpaceProject/tree/master/docs/artifacts/wireframes_and_flowcharts/milestone-4

Represents how data flow occurs in our app.

### Data Schema
#### Not Yet Implemented
<!-- * This diagram shows the key data models and how they fit together. -->
<!-- * The boxes represent data classes and database tables -->
<!-- * The arrows represent object references and database joins -->

<!-- ![](img/Book_Data.png) -->



### Data models

Data Classes and database tables

* User
    * id
    * connection
    * first_name
    * last_name
    * email
    * password
    * active
  
* Post
    * id
    * reply
    * body
    * time_stamp
    * image
    * user.id*

“*” makes a link to another table.  This is implemented 
by a foreign key relationship between the two tables.  

Example: Books have Authors so the Book data model has
a ForeignKeyField that points to the Author Model class.



### App Views
#### Not Yet Implemented
<!--
* Users
    * Register Author
    * Register Reader
    * User Admin
* Books
    * Create Book
    * List Books
    * Edit Book
    * Read Book
* Chapters
    * New Chapter
    * Edit Chapter
    * Read Chapter
-->

### Phases Of Implementation
#### Not Yet Implemented
<!--
* 3 - Core features
    * Streamline and improve UX
    * Deal with Errors
* 4 - Functionality complete
    * Build out logging
    * Fix errors
    * Performance
    * Usability testing and improvements
* 5 - Code Complete
    * Fix all defects
    * Implement 100% test coverage
-->

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


### Selecting Development Tools
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
    Sublime Text           
    Personal choice
    Brackets 
    
Github

    Git for version control
   
Python Anywhere

    Account:  elbeauspace
    Web URL:  https://elbeauspace.pythonanywhere.com
    

### Deciding on App deployment
Alternative Hosting Services

* AWS - Powerful, high-priced, complex initial setup
* Heroku - Turn key solution for Django apps
* Digital Ocean - Simple yet powerful (Shrinking World uses this)
* Python Anywhere - Free accounts available, optimized for Django
* Bluehost - Supports PHP but not Django

ElbowSpace will be using Python Anywhere to do free hosting.  Tutorial documents will show
all developers how to setup and configure a web app.

=======
Each team member is required to complete the survey for each milestone.  Tools will act as
a reminder.

#### Milestone #2 Team Survey

    Kevin - (x/3 credits)
        _x__ participated in team meetings
        _x__ was cooperative
        _x__ delivered contribution
        
    Stephen - (x/3 credits)
        _x__ participated in team meetings
        _x__ was cooperative
        _x__ delivered contribution
        
    Angel - (x/3 credits)
        _x__ participated in team meetings
        _x__ was cooperative
        _x__ delivered contribution
        
    Ben - (x/3 credits)
        _x__ participated in team meetings
        _x__ was cooperative
        _x__ delivered contribution
        
    * You must add a note for missing credits
