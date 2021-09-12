# movie_project
The aim of the project is to To create a CRUD application with utilisation of supporting tools,
methodologies and technologies that encapsulate all core modules
covered during training
# ERD design
At the planning of the project i initaily made a couple database tables which i saw to be feesable for the scope of the project. As i was moving on to my risk assesment i quickly figured out that the database i wanted to make was a little bit to ambious for my skills so i had to rethink how i wanted it to look. Prior Database below:
![ERD](images/ERD.png)

Upon some advice the 'Customer_portal' table was taken out so i could reach the MVP for the scope of the project in time. This is the current ERD:
![ERD2](images/Updated ERD.png)

#Risk Assesment
My risk assesment shows the possible risk that may occur during the development of my project.This helps us to minimize any major faults or setbacks during the course of the project:
![Risk_assesment])(images/Risk2.png) 
some fo the risks and measures i identifed was:

* App breaking code getting pushed up to main branch, the measure for this was to double check all code is working accordingly and having a back up file somewhere to revert to if things do go wrong.

* Secret key being uplaoded to github, this has a high impact level on the project and could be a data breach, to control this i will have gitignore and secret keys implemented before pushing to git hub

* App Virtual machine goes down, We can try and restore this by creating a new instance of the virtual machine and cloning from github

# CI pipeline
Using a continuous integration pipeline was one of the constraints of the project, this is what we have been trying to implement through our project. The version control i used for my project was github using this was an easy and clear way of of sharing information and collabrating on software development. 

# Project Tracking 
 The project was tracked through a Kanban Trello board:
 ![Trelloboard](images/trello before.png)
 The board shows the essentials of the project and the process should be moving from left to right as the development of the app progresses through the week.
 
  With the backlog is where i stored the aspects i have yet to start, and after i start it relocates into a another card which i can then place in the completed card. This visualses what i have done and gives me context what i have to do next.

# Development
## CRUD
I set up a virtual enviroment hosted on a aws Ubuntu server, this is where i set up all my installs and requirments  for my project.
![venv](images/venv.png)
* CRUD
Whilst creating the CRUD Functinality in flask i came across many obstacles, however i ended up creating a mimimstic app that shows the users movie input, deletes it and updates it:

 This is where the user inputs a movie ID so it can relate to my second form and then the user can fill in details about the Id of the film, as you can see below 
 ![addmovie](images/homepage.png)
Here is a form of where the user can input certain details about the details of the film like film_name 
![Createmovie](images/addfilm.png)

Here the user can view all the inputs they have put in and from here users can edit, and delete the movie IDs from the database. 
![viewspage](images/movielist.png)

When the user wants to update the film list they are redirected into the update form, this shows the 

Jinja was used create my html files, so the app can actually displays on to the screen in readable format for the user to use, No CSS or  bootstrap was used this time.this could of been a section i would of implemented however i felt that other aspects of the project was more important.
## Database
In the begginnig od my project i was working on the inbuilt database sqlite, this had all he functionality i wanted it to, however towards the end, i changed to a standalone rds database on aws,this starts to use the memory from  my EC2 rather than my sqlite in build database. The database and my virtual machine are talking to each other, to do this i had to write a connection string that links the two together.
![connection_string](images/dadatbase.png)
As you can see my connection string is hidden if this case and i pushed into github anyone would of been able to work out the location of my db and my username and password. To counter this i used th os getenv method, this hides confidential code. Then all i have to do is export my 'DATABASE_URI' and my 'SECRET_KEY' then the db is more secure.
# Testing 
Testing was an essential part of the app, this made sure that the app was running the way it is intended. However this is the side of the project i encountred a lot of errors with so the testing was not at a place i would of liked. Under reveision the testing had breadcrumbs leading to the start of the project.

Aligned with the trello board and time i had lef the decsion was to try and reach the MVP of the scope. Below is the start of the testing as i was tesing to make sure the redirects on each page was working correctly, and showing as intended. 

## Intergration testing
Integration trsting would of been added by setting up a Jenkins VM this would then be able to test and build my project automusley through a freestyle project cloned down from github.

## Future improements
* creating a more relatable db model that emcompases boththe models well
* implementing a cinema location if the user wants to go and see the film in  a specfic venu
* Jenkins and 