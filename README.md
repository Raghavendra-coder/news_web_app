Project URL: https://latestnewswebapp.pythonanywhere.com/
(Suggested to go for this URL first)

2. Loom video URL : part-1 : https://www.loom.com/share/7da41fe3a2f44debb504225365e5627f?sid=b64fff90-73fd-4771-94de-3136f8443e1a
                    part-2 : https://www.loom.com/share/859fd640c0dd4df5b11fc7811c9ab221





Steps to install the project on the local machine -
1. Clone the project in a local machine. (git clone https://github.com/Raghavendra-coder/news_web_app.git)
2. Create a virtual environment for Python 3.10(use pip or conda, I have used conda for local and pip in server).
3. Activate the v-env.
4. Install the requirements.txt in the project folder. (pip install -r requirements.txt)
5. Migrate the database (python manaage.py migrate) in the main directory(news_web).
6. Run the server (python manage.py runserver)
7. Open the base URL(http://127.0.0.1:8000/)
8. For testing the API run (python manage.py test) it will give the status OK in the end means the API did run successfully!

Everything mentioned is added in the project, Logger, unit-test, Docker, async(using celery and Redis server for local, for deployment docker server)
