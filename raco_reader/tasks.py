from datetime import datetime

from django.contrib.auth.models import User

from main.models import Post
from raco_reader.celery import app
from main.oauth import oauth

@app.task
def print_stuff():
    print("background task")

@app.task
def store_notifications():
    #for each user in the model
    all_users = User.objects.all()
    for user in all_users:
        try:
            last_post = user.post_set.order_by("-modification_date")
            token = user.oauth2token
            resp = oauth.raco.get('/v2/jo/avisos/?format=json', token=token.to_token())
            profile = resp.json()
            for note in profile['results']:
                if (last_post and datetime.strptime(note['data_modificacio'], "%Y-%m-%dT%H:%M:%S") <= last_post[0].modification_date):
                    continue
                model = Post(title=note['titol'],
                             subject=note['codi_assig'],
                             modification_date=note['data_modificacio'],
                             text=note['text'],
                             user = user)
                print(model.title)
                model.save()
        except Exception as inst:
            print(type(inst))
            print(inst.args)

