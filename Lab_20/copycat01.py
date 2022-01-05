#!/usr/bin/env python3

# import additional code to complete our task
import shutil
import os

def main():
    # move into the working directory
    os.chdir("/home/student/2022-01-04-Python/")

    # copy the fileA to fileB
    shutil.copy("Lab_20/sdn_network.txt", "Lab_20/sdn.network.txt.copy")

    #copy the entire directoryA to directoryB
    shutil.copytree("Lab_20/", "Lab_20_backup/")

if __name__ == "__main__":
    main()
