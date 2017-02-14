from peewee import *


with open('username.txt', 'r') as myfile:
    data = myfile.read()
    db = PostgresqlDatabase('aracz', user='aracz')


class SuperSprinter(Model):
    title = TextField(null=False)
    story = TextField(null=False)
    acceptance_criteria = TextField(null=False)
    business_value = IntegerField(null=False)
    estimation = FloatField(null=False)
    status = CharField(null=False)

    class Meta:
        database = db