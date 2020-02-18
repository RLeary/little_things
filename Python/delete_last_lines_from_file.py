# deletes the last 3 lines of a given file
# used for ADCS log parser, saves manually deleting them, as it 
# stops saving when the program stops, not always on a full line

import sys

if len(sys.argv) > 2:
    print("Error: Only input one filename")
    exit()
elif len(sys.argv) < 2:
    print("Error: enter a filename")
    exit()

FILE = sys.argv[-1]

try:
    read_file = open(FILE, 'r')
except FileExistsError:
        print("Input does not exist")

lines = read_file.readlines()

read_file.close()

del lines[-3:]

try:
    write_file = open(FILE, 'w')
    try:
        write_file.writelines(lines)
    finally:
        write_file.close()
except IOError:
    print("Error in writing to file")

# Batch file for running log parser: 
"""
@echo off
set /p inputfilename="Enter Input Filename: "

python "..\release\64bit\delete_last_line.py" %inputfilename%
CALL "..\release\64bit\Magnetometer Functional Check.exe" %inputfilename%

pause
"""