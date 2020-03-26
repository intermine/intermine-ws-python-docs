"""
Tests notebooks in the given directory
"""
from os import listdir
import subprocess


def list_files(directory, extension):
    """
    Returns all files in the given directory and the given extension
    """
    return (f for f in listdir(directory) if f.endswith('.' + extension))


def main():
    """
    Prints notebooks with the status of the checking
    """
    notebooks = list(list_files('./', 'ipynb'))
    status = []
    for notebook in notebooks:
        output = subprocess.run(
                                ['jupyter', 'nbconvert',
                                '--to', 'notebook', '--inplace',
                                '--execute', notebook],
                                stdout=subprocess.DEVNULL)
        if output.returncode == 0:
            status.append("passed")
        else:
            status.append("failed")
    for (notebook, stat) in zip(notebooks, status):
        print("The build test for " + notebook + " " + stat + ".")


if __name__ == "__main__":
    main()
