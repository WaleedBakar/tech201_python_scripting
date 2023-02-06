import os
import subprocess

# Python doesnst actually run shell commands
# instead we can use oython to run shell script files

script_dir = os.path.dirname(__file__)

script_absolute_path = os.path.join(script_dir + "/script.sh")

subprocess.call(["sh", script_absoulte_path])