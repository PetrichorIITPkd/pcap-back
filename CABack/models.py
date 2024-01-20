import random
import string


from django.db import models
from django.contrib.auth import get_user_model

User=get_user_model()

class CAProfile(models.Model):
    fullname = models.TextField()
    email = models.EmailField(primary_key = True)
    phone = models.CharField(max_length = 15)
    college = models.TextField()
    year = models.IntegerField()
    CA = models.CharField(max_length=6, unique=True)

    @staticmethod
    def _random_CACode():
        all_letters = string.ascii_lowercase + string.digits
        cacode = ''
        for _ in range(6):
            cacode += random.choice(all_letters)
        return cacode

    def generate_ca_code(self):
        ca = self._random_CACode()
        try:
            self.objects.get(ca)
            self.generate_ca_code() 
            # crossing recursion limit is too improbable, 
            # if you are reading it when petrichor actaully became famous 
            # enchanteddev and alonot apologise.
        except self.DoesNotExist:
            self.CA = ca