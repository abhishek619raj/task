API VIEW

LOGIN
path('user/login/', login),
on login token is created use it in postman as token to get access.

CREATE_USER
path('user/create_user/', create_user),
you can create user with this url this user can be admin or Guest depent apon your choise.

LOGOUT
path('user/logout/', Logout.as_view()),
delete the token created at the time of login.

MOVIE CRUD (for Admin)
path('user/movie/(<movie_id>[0-9]+)',views.MovieView.as_view()),
here in this the user created above will be act as admin he can edi update and delete movie.

MOVIE GET (for Guest)
no authorization anyone can see movie this is for Guest
path('user/movie/',views.MovieView.as_view()),
user with login can see all the moview created by admin.
the json file which you have send me saprately i didnt use that i am not familiar with Mysql although i have use mysql database




for more details check super admin django panel
username:abhishek
pass:abhi261290






########HOW TO DEPLOY ON HEROKU############## 
- Copy the project seperately
- Go to 'Getting Started on Heroku with Python'
- Create an Heroku account
- install pipenv
- Install git ( check git --version)
- Install Heroku CLI
- Login heroku
- Create a virtual enviroment
- Run manage.py not gonna run - pip freeze nothing installing
- Check which version django,requests you have and install it
- Run manage.py and then stop it
- Go to django heroku
- Create a Procfile and
- Install django-heroku
- Add stuff to settings.py file (goto doc on website)
- Install guincorn
- pip freeze > requirements.txt
- heroku create attreyaweb (to create an app on heroku)
- git status git commands (git push heroku master)
- Open up the website
- Admin panel not working. heroku run bash. Migrations





Python Movie Searching Algorithm
i was trying to do it using regres but it will take time so i did simple Algorithm (movieseacrh.py)


in this code i read the json file what you have provided me and search for movie name only for now

for example please see (screenshot/movieseacrh)
Charlies Angels is user input
after that info will come

git clone https://2612@bitbucket.org/2612/movie.git

open repo



and about requirements.txt i have actually create this project inside my env (moslty related to Datascience to you may able to see many library)
but for this project i use 2,3 dependancy
such as django2.1,drf,mark-filter,..
hasing also i have used for password bycryt 