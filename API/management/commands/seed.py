from API.models import Employee
from faker import Factory
from django.db import transaction
from django.core.management.base import BaseCommand

from faker import Faker
fake = Faker()


NUM_POSTS = 10


class Command(BaseCommand):
    help = "Setup test articles for the demo website"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        fake = Factory.create("en_AU")
        Employee.objects.all().delete()
        for i in range(NUM_POSTS):
            print("Creating post", i)
            Employee.objects.create(
                name=fake.name(),
                dob=fake.date(),
                phone=fake.phone_number(),
                company=fake.company(),
                address=fake.city()
            )
