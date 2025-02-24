Steps to install the project in local machine -
1. Clone the project in local machine. (git clone https://github.com/Raghavendra-coder/news_web_app.git)
2. Create virtual environment for python 3.10(use pip or conda, I have used conda in local and pip in server).
3. Activate the v-env.
4. Install the requirements.txt in project folder. (pip install -r requirements.txt)
5. Migrate the database (python manaage.py migrate) in the main directory(news_web).
6. Run the server (python manage.py runserver)
7. Open the base url(http://127.0.0.1:8000/)
8. For testing the API run (python manage.py test) it will give status OK in the end means API did run successfully !

Evrything mentioned is added in the project, Logger, unit-test, Docker, asyn(using celery and redis server for local, for deployment docker server)
