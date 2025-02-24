from django.core.management.base import BaseCommand
from news_web_app.news import hello_world

class Command(BaseCommand):
    help = "print hello world every min"

    def handle(self, *args, **kwargs):
        hello_world()


# "* * * * *  /opt/anaconda3/envs/piv_env/bin/python3.10 manage.py hello_world >> debug.log"
# "* * * * *  /opt/anaconda3/envs/piv_env/bin/python3.10 /Users/mabookair/Desktop/projects/pivony/news_web/manage.py hello_world >> /Users/mabookair/Desktop/projects/pivony/news_web/debug.log"
