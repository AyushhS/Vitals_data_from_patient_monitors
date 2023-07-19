# Importing libraries 
print('Importing libraries - ')

from libraries import *
from utilities import *


print('Done.')

welcomeMessage()

def main():
    while True:
        print('> ', end='')
        a = []
        try:
            a = processInput()
        except KeyboardInterrupt:
            break

        if len(a) == 0:
            continue

        if len(a) == 1:
            path = a[0]
            if path.lower() == '--help':
                helpFunction()
                continue
        
            if path.lower() == '--quit':
                break

            if path == '':
                continue
            
            imageProcess(path)

        elif len(a) == 2:
            path = a[0]
            argument = a[1]

            if argument == '':
                imageProcess(path)
            elif argument == '-cp':
                croppedImageProcess(path, 'output' + '-cropped.jpeg') 
            elif argument == '-cph':
                croppedImageProcessWithGraph(path, 'output' + '-cropped.jpeg') # graph does not work, debug this
            elif argument == '-f':
                folderProcess(path)
            elif argument == '-cf':
                croppedImageFolderProcess(path, 'output')
            else:
                argumentErrorPrompt()

        else:
            argumentErrorPrompt()

if __name__ == '__main__':
    main()

# TODO - handle more input errors like wrong file/folder names
