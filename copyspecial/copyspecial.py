#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them

def abspath(dir_name):
  path_list = []
  dir_list = os.listdir(dir_name)
  for x in dir_list:
    match = re.search(r'\w+__\w+__\.\w+',x)
    if match:
      path = os.path.join(dir_name,match.group()) 
      path_list.append(os.path.abspath(path))
  return path_list
      
 



def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]

  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)

  # +++your code here+++
  # Call your functions
  if todir != '':
    dest_abspath = os.path.abspath(todir)
    os.makedirs(dest_abspath)
    for name in args:
      src_list = abspath(name)
      for item in src_list:
        shutil.copy(item,dest_abspath)
  

  if tozip != '':
    for name in args:
      src_list = abspath(name)
      cmd = 'zip -j '+tozip+' '
      for name in src_list:
        cmd = cmd+' '+name
	(status,output) = commands.getstatusoutput(cmd)
	if status:
	  sys.stderr.write('error  ')
  else:
    for name in args:
      for item in abspath(name): print item
  
if __name__ == "__main__":
  main()
