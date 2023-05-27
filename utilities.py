from imageProcessing import segmentation

def processInput():
    s = input()
    s2 = s.split()
    cond = False
    i = 0
    while(i < len(s2)):
        if (cond and i >= 1):
            cond = ~cond
            s2[i - 1] = s2[i - 1] + ' ' + s2[i]
            i = i - 1
            s2.remove(s2[i + 1]) 
        for j in range(0, len(s2[i])):
            if (s2[i][j] == '\'' or s2[i][j] == '\"'):
                cond = ~cond
                continue
        i += 1
    for j in range(0, len(s2)):
        s2[j] = s2[j].replace('\'', '')
        s2[j] = s2[j].replace('\"', '')
    return s2

def welcomeMessage():
    print('VITAL DATA FROM PATIENT MONITORS PROJECT')
    print('A project used to find vital information from images/videos of patient', 
    'monitors. Developed by Team19, IIT Bhubaneswar as a part of Inter IIT ',
    'Tech meet 2022.')
    print('\nEnter the adress/link of image to be processed.')
    print('Enter --help for more options')
    print('Enter --quit or press Ctrl + C to quit the application. ')

def helpFunction():
    print('Copy paste the link/path of the patient monitor image you',  
    'want the vitals to be detected.')
    print('Enter --help for more options')
    print('Enter --quit or press Ctrl + C to quit the application.')
    print('additional arguments after path - \n')
    print('-cp = if the file is an image. The output would also',
    'have a cropped patient monitor along with output of the vital signs in',
    'the CLI. example (This example is to be used for all the arguments) - \n')
    print('\t<image_path> -cp <output_path>\n')
    print('-v = if the file is a video. The output would be a csv',
    'file containing the vitals of the image in csv file')
    print('-cv = if the file is a video. The output would be', 
    'video with cropped patient monitors in it, along with a csv file.')

def argumentErrorPrompt():
    print('Error: Incorrect arguments supplied. Please retry with the correct', 
    'arguments.')
    print('For help, type --help.')
    print('To exit the program, type --quit or press Ctrl + C.')

def imageProcess(inputpath, outputpath):
    print('i')

def croppedImageProcess(inputpath, outputpath):
    segmentation(inputpath, outputpath)

def videoProcess(inputpath, outputpath):
    print('v')

def croppedvideoProcess(inputpath, outputpath):
    print('cv')