from faker import Faker
import django
import random
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProTwo.settings')
django.setup()

from AppTwo.models import User

fake_gen = Faker()

x = 0
while x < 10:
    x = x + 1

    # Create fake entries
    fake_name = fake_gen.first_name()
    fake_surname = fake_gen.last_name()
    fake_email = fake_gen.email()

    User.objects.get_or_create(first_name=fake_name, last_name=fake_surname, email=fake_email)

