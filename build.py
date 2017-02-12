from model import *

db.connect()


db.drop_tables([SuperSprinter], safe=True)
db.create_tables([SuperSprinter], safe=True)
SuperSprinter.create(title="Handle New Application",story="Automate the process of incoming applications",acceptance_criteria="For new applicant the system assigns the missing info",business_value=1000,estimation=4,status="Done")
SuperSprinter.create(title="Find Possible Interview Date",story="Automate the process of scheduling interviews",acceptance_criteria="Assigns interview date where no date for all applicants",business_value=1500,estimation=3,status="Planning")
