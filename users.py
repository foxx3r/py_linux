#!/usr/bin/env python3
# coding: utf-8
import re

list_of_users = ['root']

class User(object):
    def __init__(self, name_user):
        user_root = "root"
        self.name_user = name_user
    def create_user(self, method):
        if method == 'useradd':
            list_of_users.append(self.name_user)
        if method == 'adduser':
            print( \
                'Adding user \'{0}\' ...\n \
                Adding new group \'{0}\' (1005) ...\n \
                Adding new user \'{0}\' (1005) with group \'{0}\' ...\n \
                Creating home directory \'/home/{0}\' ...\n \
                Copying files from \'/etc/skel\' ...\n \
                  '.format(self.name_user))
            password = str(input('New password: '))
            confirm_password = str(input('Retype new password: '))
            if password == confirm_password:
                print( \
                      'passwd: password updated succesfully\n \
                      Changing the user information for one')
            else:
                print( \
                      "Sorry, passwords do not match.\n \
                      passwd: Authentication token manipulation error\n \
                      passwd: password unchanged")
    def delete_user(self, user_to_del):
        if user_to_del not in list_of_users:
            print('userdel: user \'{0}\' does not exist'.format(user_to_del))
        elif user_to_del in list_of_users:
            index_of_user = list_of_users.index(user_to_del)
            del list_of_users[index_of_user]
