# movie_project
The aim of the project is to To create a CRUD application with utilisation of supporting tools,
methodologies and technologies that encapsulate all core modules
covered during training
# ERD design
At the planning of the project i initaily made a couple database tables which i saw to be feesable for the scope of the project. As i was moving on to my risk assesment i quickly figured out that the database i wanted to make was a little bit to ambious for my skills so i had to rethink how i wanted it to look. Prior Database below:
![ERD] ()

Upon some advice the 'Customer_portal' table was taken out so i could reach the MVP for the scope of the project in time. This is the current ERD:
![ERD2]()

#Risk Assesment
My risk assesment shows the possible risk that may occur during the development of my project.This helps us to minimize any major faults or setbacks during the course of the project:
![Risk_assesment])()
some fo the risks and measures i identifed was:

* App breaking code getting pushed up to main branch, the measure for this was to double check all code is working accordingly and having a back up file somewhere to revert to if things do go wrong.

* Secret key being uplaoded to github, this has a high impact level on the project and could be a data breach, to control this i will have gitignore and secret keys implemented before pushing to git hub

* App Virtual machine goes down, We can try and restore this by creating a new instance of the virtual machine and cloning from github

# CI pipeline
Using a continuous integration pipeline was one of the constraints of the project, this is what we have been trying to implement through our project. The version control i used for my project was github