#!/usr/bin/python3
import subprocess

ls = subprocess.run('ls', shell=True, capture_output=True, text=True)
print(ls.stdout)
