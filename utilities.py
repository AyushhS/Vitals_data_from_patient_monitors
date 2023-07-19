from imageProcessing import segmentation
from monitorProcessing import main_func1
from libraries import *

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
    print('\t<image_path/folder_path> -cp\n')
    print('-cph = if the file is an image. The output would also',
    'have a cropped patient monitor, a heart rate monitor in a plot', 
    'along with output of the vital signs in',
    'the CLI.')
    print('-f = if a folder containing the image is given. The output would be a csv',
    'file containing the vitals of the image in csv file')
    print('-cf = if a folder containing the image is given. The output would be a csv',
    'file containing the vitals of the image in csv file, and a folder containing all ', 
    'the cropped images.')

def argumentErrorPrompt():
    print('Error: Incorrect arguments supplied. Please retry with the correct', 
    'arguments. make sure that all the paths are enclosed with \"\" or \'\'.')
    print('For help, type --help.')
    print('To exit the program, type --quit or press Ctrl + C.')

# def segmentation(imagepath):
#     image = processImage(imagepath)
#     image = deskewImage(image)
#     image = pad(image)
#     coordinates = giveCoordinates(image)
#     croppedImage = croppingSegmentatedImages(coordinates, image)
#     return croppedImage

# def inference(image_path:str) -> dict:
#     croppedImage = segmentation(image_path)
#     result = main_func1(croppedImage)
#     return result

def processImage(imagePath):
    image = cv2.imread(imagePath)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return image

def imageProcess(inputpath):
    image = processImage(inputpath)
    croppedImage = segmentation(image)

    result = main_func1(croppedImage, False)
    print(result)

def croppedImageProcess(inputpath, outputpath):
    image = processImage(inputpath)
    croppedImage = segmentation(image)
    cv2.imwrite(outputpath, croppedImage)

    result = main_func1(croppedImage, False)
    print(result)

def croppedImageProcessWithGraph(inputpath, outputpath):
    image = processImage(inputpath)
    croppedImage = segmentation(image)
    cv2.imwrite(outputpath, croppedImage)

    result = main_func1(croppedImage, True)
    print(result)

def folderProcess(inputfolder):
    files = os.listdir(inputfolder)
    results = []
    
    for file in files:
        image = processImage(inputfolder + '/' + file)
        croppedImage = segmentation(image)

        result = main_func1(croppedImage, False)
        result['picture'] = file
        results.append(result)

    df = pd.DataFrame(results)
    df = df.set_index('picture')
    df.to_csv('vitals.csv')

def croppedImageFolderProcess(inputfolder, outputfolder):
    files = os.listdir(inputfolder)
    results = []

    if not os.path.isdir(outputfolder):
        os.mkdir(outputfolder)
    
    for file in files:
        image = processImage(inputfolder + '/' + file)
        croppedImage = segmentation(image)
        cv2.imwrite(outputfolder + '/' + file.split('.')[0] + '-cropped.' + file.split('.')[1], croppedImage)

        result = main_func1(croppedImage, False)
        result['picture'] = file
        results.append(result)

    df = pd.DataFrame(results)
    df = df.set_index('picture')
    df.to_csv('vitals.csv')