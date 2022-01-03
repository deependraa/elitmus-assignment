# elitmus-assignment
To set up project for running on you local host:
make sure python is installed on you Machine
download the repo and open it in your ID ex: VScode
go to terminal and type this with the same directory as where you have cloned the project: python -m venv path
      ex:python -m venv e:/web_development/Elitmus assignment
After that activate the virtual environment that you have just make by directing to tha evvironment file 
      ex: cd e:/web_development/Elitmus assignment/venv/Scripts/activate.bat
      This will activate you virtual environment and you command line should look like this
      Ex: (venv) E:\web_development\Elitmus assignment>
After this install all the reqirement which are in requirement.txt file of main folder, I will just give you a direct comment to install all the dependencies:
      asgiref==3.4.1
    dj-database-url==0.5.0
    Django==4.0
    django-filter==21.1
    django-storages==1.12.3
    gunicorn==20.1.0
    Pillow==9.0.0
    psycopg2==2.9.3
    sqlparse==0.4.2
    tzdata==2021.5
    whitenoise==5.3.0
    
    type this : pip install django django-filter django-storages Pillow psycopg2
    
Install postgresql on you machine and set up password and then open pgadmin which you will get after installing postgresql 
In pgadmin make a new database with name of Elitmus assignment and in connection/Host type localhostremember and leave same as it is and click save

Now go to setting.py file which you will find in assignment folder of the main directory and in their go to data base section and edit it as:

    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'Elitmus assignment',
        'USER': 'postgres',
        'PASSWORD': 'Password whcih you have made',
        'HOST': 'localhost',
        'PORT': '5432',

    }
  }
  
  
  
 Now just run some final commands :
 1)python manage.py collectstaic
 2)python manage.py makemigrations
 3)python manage.py runserver
 
And this will run the project on the port as: http://127.0.0.1:8000/

You can find the live project here at: https://elitmusdeependra.herokuapp.com/ 
but it might give a connection error of TCP IP due to static files or i might have resolved that problem till date you open the project
I would recommend to run the project on localhost to get look in to admin section

of you want to go to the admin section onec your server id live on local host just type :
    http://127.0.0.1:8000/admin
    and type user name and password as :
    username :deependra_elitmus@gmail.com
    password : deependra_elitmus
    if this username and password does not work for you the make new superuser ny going back to terminal where you enviroment is activated and type:
    python manage.py createsuperuser, and follow the instructions and go back to admin panel and login with the id pass you created
    
    
