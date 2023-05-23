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
    'the CLI. example - \n')
    print('\t<image_path> -cp\n')
    print('-v = if the file is a video. The output would be a csv',
    'file containing the vitals of the image in csv file')
    print('-cv = if the file is a video. The output would be', 
    'video with cropped patient monitors in it, along with a csv file.')

def argumentErrorPrompt():
    print('Error: Incorrect arguments supplied. Please retry with the correct', 
    'arguments.')
    print('For help, type --help.')
    print('To exit the program, type --quit or press Ctrl + C.')

def imageProcess(path):
    print('i')

def croppedImageProcess(path):
    print('ci')

def videoProcess(path):
    print('v')

def croppedvideoProcess(path):
    print('cv')