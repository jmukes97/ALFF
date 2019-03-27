# ALFF
Apex Legends Friend Finder. As or right now there is a fully functional registration and login system. 
to run you need pyhton3 installed along with pip3. use pip3 to install django then run:

'python3 manage.py runserver'

The current version of the project is being hosted at 

http://52.15.54.193/

## Project directory map (Only includes interesting files)

**ALFF** (This is the settings folder. Most of the project wide settings are in here)
	settings.py (various settings)
	urls.py (defines Urls for the project)

**webapp** (COntains the actuall application)
	static (Static files go in here. js css jpg etc)
	templates (html only)
	models.py (Defines how the database will be set up. Objects will be defined here)
	views.py ( defines a set of python functions that will run once a url recieves a request)
	
**db.sqlite3** (Please dont touch with sql or anything. If the database needs to be modified use models.py)

**manage.py** (Used for creating more webapps or running the server)
