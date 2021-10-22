import os
def cwd():
    cwd = os.getcwd()
    print(f"The current working directory is {cwd}")
    print("The directory contains the following files:")
    for file in os.listdir(cwd):
        print(file)
def run():
    print("Processing...")
    cwd()

run()