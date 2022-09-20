# coding=utf-8

###########################################################################
Name : Moonton Account Checker #
# File           : python2.py               #

# Author         : kiel. 
# Github : anurankiel
# Python version : 2.7 OR 3.7++


###########################################################################
import os, sys, hashlib, json
try:
from concurrent.futures import ThreadPoolExecutor 
except ImportError:
if sys.version_info.major != 2:
os.system('pip install futures')
exit('Please restart this tools')
else:
os.system('pip2 install futures')
exit('Please restart this tools')
try:
