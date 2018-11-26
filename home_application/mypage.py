import models
import json


def my_page_create(self):
   _data= json.loads(self.body)
   models.User.objects.create(account=_data.get("account",None),age=_data.get("age",None))
def get(self):
   return models.User.objects.all()
def deleteU(self):
   _data = json.loads(self.body)
   return models.User.objects.get(id=_data.get("id",None)).delete();