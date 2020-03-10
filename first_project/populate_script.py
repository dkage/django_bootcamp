import os
import django
import random
from faker import Faker

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')

django.setup()

from first_app.models import Topic, Webpage, AccessRecord

fake_gen = Faker()
topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']


def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t


def populate(N=5):

    for entry in range(N):

        # Get topic
        top = add_topic()

        # Create fake data
        fake_url = fake_gen.url()
        fake_date = fake_gen.date()
        fake_name = fake_gen.company()

        # Create the new data to enter db
        web_page = Webpage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0]

        # Create fake log access
        record = AccessRecord.objects.get_or_create(name=web_page, date=fake_date)[0]


if __name__ == '__main__':
    print('Populating script running!')
    populate(20)
    print('Script done.')
