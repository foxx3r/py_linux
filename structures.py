#!/usr/bin/python3
# coding: utf-8
import users
import colors

# HOME = main.home_directory[]
current_directory = None
class inheritances(object):
    def root(self, directory):
        root_directories = ['bin', '\tboot', '\tdev', '\tetc', '\thome\n', 'lib', '\tmedia', '\tmnt', '\topt', '\tproc\n', 'root', '\trun', '\tsbin', '\tsrv', '\tsys\n', 'tmp', '\tusr', '\tvar']
        def bin():
            pass
        def boot():
            pass
        def dev():
            pass
        def etc():
            pass
        def home():
            pass
        def lib():
            pass
        def media():
            pass
        def mnt():
            pass
        def opt():
            pass
        def proc():
            pass
        def root():
            pass
        def run():
            pass
        def sbin():
            pass
        def srv():
            pass
        def sys():
            pass
        def tmp():
            pass
        def usr():
            pass
        def var():
            pass
        for directories in root_directories:
            print(f'{colors.blue_font}{directories}{colors.final}', end='')
        try:
        	return eval(directory)
        except Exception:
        	return False
ama = inheritances()
ama.root('bin')
