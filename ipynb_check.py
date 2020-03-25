from os import listdir
import subprocess
 
def list_files(directory, extension):
    return (f for f in listdir(directory) if f.endswith('.' + extension))

def main():
    notebooks = list(list_files('./', 'ipynb'))
    status = []
    for notebook in notebooks:
    	output = subprocess.run(['jupyter', 'nbconvert', '--to', 'notebook', '--inplace', '--execute', notebook], stdout=subprocess.DEVNULL)
    	if(output.returncode==0):
    		status.append("passed")
    	else:
    		status.append("failed")
    for i in range(0,len(status)):
    	print("The build test for " + notebooks[i] + " " + status[i] + ".")

if __name__ == "__main__":
    main()