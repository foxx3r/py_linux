#!/usr/bin/env python3
# coding: utf-8
import re
import os
import structures

list_of_groups = ["root"]

instance_of_structures = structures.inheritances
list_of_directories = {
    '/': {
        'bin': instance_of_structures.root('bin'),
        'boot': instance_of_structures.root('boot'),
        'dev': instance_of_structures.root('dev'),
        'etc': instance_of_structures.root('etc'),
        'home': instance_of_structures.root('home'),
        'lib': instance_of_structures.root('lib'),
        'media': instance_of_structures.root('media'),
        'mnt': instance_of_structures.root('mnt'),
        'opt': instance_of_structures.root('opt'),
        'proc': instance_of_structures.root('proc'),
        'root': instance_of_structures.root('root'),
        'run': instance_of_structures.root('run'),
        'sbin': instance_of_structures.root('sbin'),
        'sys': instance_of_structures.root('sys'),
        'tmp': instance_of_structures.root('tmp'),
        'usr': instance_of_structures.root('usr'),
        'var': instance_of_structures.root('var')
    }
}

'''home_directory = {
    "root": files.inheritances.root.root()
}'''

class Group(object):
    def __init__(self, name_group):
        self.name_group = name_group
    def create_group(self):
        list_of_groups.append(self.name_group)

class directory(object):
    def __init__(self, name, permissions):
        self.name = name
        self.permissions = int(permissions)
        if len(permissions) > 3:
            print()
        elif 8 or 9 in permissions:
            print()
        else:
            pass
    def create_directory(self):
        list_of_directories.append(self.name)

