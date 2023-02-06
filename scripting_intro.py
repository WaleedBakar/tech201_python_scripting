# Scripting
import datetime
import os
# Shorter pieces of code that allow us to do things we would otherwise have to do manually
# Unlike programs, scripts are one file and do not need to be complied
#  API's tend to use scripts
# Scripts use less or no absraction and are not as flexiable as programs but they are much easier to use read and write.

#Scripts are almost always written in "high level" languages (easy to read) - pyhton, bash, ruby

# Why Python

# open source
# many libraries
# Easy to understand
# large community
# Language interoperability (cab talk to other languages os and software

# Why is scrippting important for DevOps?

# Automation -> of mundane tasks


# 7 Core modules

#Sys
#OS
# Subprocesses
# Math
# Random
#DateTime
#JSON


# Sys modile script

import  sys

print(sys.version)


# os module script

print(os.getcwd())

# os.mkdir("path") # make new directory
# os.chdir("path") # chnages current directory

# Subprocess module script

# Can be used to create and intract with sub procces being managed by our python interpreter

import subprocess

subprocess.run(["python", "hello_world.py"])


# Math module scripts

import math

pi = math.pi

pi_string = str(pi)
print("the value of pi is" + pi_string)

import random

randum = random.randrange(1, 10)
print(randum)

#DateTime
import datetime
whatisthedate = datetime.datetime.now()
print(whatisthedate)

# JSON module
import json
x = {
    "name": "John",
    "age": 30,
    "city": "London"
}
y = json.dumps(x)

print(y)
