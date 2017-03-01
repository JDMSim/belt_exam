from __future__ import unicode_literals
from django.db import models
from datetime import datetime
import re, bcrypt


class RegistrationManager(models.Manager):
    def Register(self, name, uname,  pword, c_pword):
        error_list = []
        today = datetime.now()
        # name valication
        if len(name) < 1:
            error_list.append ('First name cannont be empty')

        #username validation
        if len(uname) < 1:
            error_list.append('Username cannont be empty')
            if self.filter(email = email):
                error_list.append('Username already exists')

        #Password validation
        if len(pword) < 8:
            error_list.append('Password must at least be 8 characters long')

        if not pword == c_pword:
            error_list.append('Password does not match')

        if len(error_list) < 1:
            en_pword = pword.encode()
            hashed_pw = bcrypt.hashpw(en_pword, bcrypt.gensalt())
            self.create(name = name, username = uname, password = hashed_pw)
            userData = self.filter(name = name)
            context = {'status': 1, 'response': userData[0]}
            return context
        else:
            context={'status': 0,'response': error_list}
            return context

    def login(self, postData):
        login_error = []
        if len(postData['uname']) < 1 or len(postData['pword']) < 1:
            login_error.append('Please enter username and password')
            context = {'status':0, 'response':login_error}
            return context
        else:
            userData = self.filter(username = postData['uname'])
            if not userData:
                login_error.append('Esername does not exists')
                context = {'status': 0, 'response': login_error}
                return context
            else:
                if bcrypt.hashpw(postData['pword'].encode(), userData[0].password.encode()) == userData[0].password:
                    context = {'status': 1, 'response': userData[0]}
                    return context
                else:
                    login_error.append('The password is incorrect')
                    context ={'status': 0, 'response': login_error}
                    return context


class User(models.Model):
    name = models.CharField(max_length = 100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length = 100)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = RegistrationManager()
# Create your models here.
