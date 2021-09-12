# movie_project
The aim of the project is to To create a CRUD application with utilisation of supporting tools,
methodologies and technologies that encapsulate all core modules
covered during training
# ERD design
At the planning of the project i initaily made a couple database tables which i saw to be feesable for the scope of the project. As i was moving on to my risk assesment i quickly figured out that the database i wanted to make was a little bit to ambious for my skills so i had to rethink how i wanted it to look. Prior Database below:
![ERD](images/ERD.png)

Upon some advice the 'Customer_portal' table was taken out so i could reach the MVP for the scope of the project in time. This is the current ERD:
![ERD2]()

#Risk Assesment
My risk assesment shows the possible risk that may occur during the development of my project.This helps us to minimize any major faults or setbacks during the course of the project:
![Risk_assesment])()git 
some fo the risks and measures i identifed was:

* App breaking code getting pushed up to main branch, the measure for this was to double check all code is working accordingly and having a back up file somewhere to revert to if things do go wrong.

* Secret key being uplaoded to github, this has a high impact level on the project and could be a data breach, to control this i will have gitignore and secret keys implemented before pushing to git hub

* App Virtual machine goes down, We can try and restore this by creating a new instance of the virtual machine and cloning from github

# CI pipeline
Using a continuous integration pipeline was one of the constraints of the project, this is what we have been trying to implement through our project. The version control i used for my project was github using this was an easy and clear way of of sharing information and collabrating on software development. 

# Project Tracking 
 The project was tracked through a Kanban Trello board:
 ![Trello board]()
 The board shows the essentials of the project and the process should be moving from left to right as the development of the app progresses through the week. With the backlog is where i stored the aspects i have yet to start, and after i start it relocates into a another card which i can then place in the completed card. This visualses what i have done and gives me context what i have to do next.

# Development
* CRUD
Whilst creating the CRUD Functinality in flask i came across many obstacles, however i ended up creating a mimimstic app that shows the users movie input, deletes it and updates it:
![Readfile ]()

I set up a virtual enviroment hosted on a aws Ubuntu server, this is where i set up all my installs and requirments  for my project.
 * Front end(Jinja)
 This is where the user inputs a movie ID so it can relate to my second form and then the user can fill in details about the Id of the film, as you can see below 
 ![addmovie]()
Here is a form of where the user can input certain details about the details of the film like film_name ![Createmovie]()

Here the user can view all the inputs they have put in and from here users can edit, and delete the movie IDs from the database. ![viewspage]()

# Testing 
Testing was an essential part of the app, this made sure that the app was running the way it is intended. However this is the side of the project i encountred a lot of errors with so the testing was not at a place i would of liked. Under reveision the testing had breadcrumbs leading to the start of the project. Aligned with the trello board and time i had lef the deciosn was to try and reach the MVP of the scope. Below is the start of the testing as i was tesing to make sure the redirects on each page was working correctly, and showing as intended. 