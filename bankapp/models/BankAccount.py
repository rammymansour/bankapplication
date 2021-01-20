from mongoengine import *


class BankAccount(Document):
    holding = IntField(default=5000)
