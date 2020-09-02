import os
import sys
import platform

unique_counter = 0
duplicate_counter = 0
lineend_counter = 0
operating_system = platform.system()
lines_seen = set()  # Holds lines already seen

filename, extention = (
    input("Filename:").split("/")[-1].split(".")
)  # Takes filename and splits into the name and extention

choice = input("Remove line ends? (Y/N):")
if choice == "Y" or choice == "y":
    removeLineEnds = True
else:
    removeLineEnds = False

file = open(filename + "." + extention)
outfile = open("{}_modified.{}".format(filename, extention), "w")
for line in open(filename + "." + extention, "r"):
    if line == "\n":
        if removeLineEnds:
            lineEnd_counter += 1
        else:
            outfile.write(line)
    elif line not in lines_seen:
        outfile.write(line)
        lines_seen.add(line)
        unique_counter += 1
    else:
        duplicate_counter += 1
outfile.close()

if operating_system == "Linux":
    os.system("clear")
if operating_system == "Windows":
    os.system("cls")

print("There were {} unique lines.".format(unique_counter))
print("Removed {} duplicate lines.".format(duplicate_counter))
if removeLineEnds:
    print("Removed {} line ends.".format(lineEnd_counter))

wait = input("Press return to continue")
