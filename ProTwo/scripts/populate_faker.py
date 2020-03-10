from faker import Faker
import django
import random
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProTwo.settings')
django.setup()

from ..AppTwo.models import User

fake_gen = Faker()

