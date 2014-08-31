from subprocess import call
import os.path
import platform
import sys

# Add any additional files you wish to clean here
FILES_TO_REMOVE = ["obj", "*.suo", "*.sdf"]


def remove_file(filename, windows):
    try:
        if windows:
            call(["del", "/F", "/Q", filename])
        else:
            call(["rm", "-rf", filename])
    except:
        pass


def main():
    print("Cleaning Directory...")
    if os.path.exists("Makefile"):
        try:
            call(["make", "clean"])
        except:
            pass
    for file in FILES_TO_REMOVE:
        remove_file(file, sys.argv[1] == "--windows")

if __name__ == "__main__":
    main()
