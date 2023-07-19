from libraries import *

def deskewImage(image):
    imageGrayscale = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    angle = determine_skew(imageGrayscale)
    deskewedImage = rotate(image, angle)
    deskewedImage = cv2.resize(deskewedImage, (1280,720))
    return deskewedImage

def rotate(image, angle):
    old_width, old_height = image.shape[:2]
    angle_radian = math.radians(angle)
    width = abs(np.sin(angle_radian) * old_height) + abs(np.cos(angle_radian) * old_width)
    height = abs(np.sin(angle_radian) * old_width) + abs(np.cos(angle_radian) * old_height)

    image_center = tuple(np.array(image.shape[1::-1]) / 2)
    rot_mat = cv2.getRotationMatrix2D(image_center, angle, 1.0)
    rot_mat[1, 2] += (width - old_width) / 2
    rot_mat[0, 2] += (height - old_height) / 2
    return cv2.warpAffine(image, rot_mat, (int(round(height)), int(round(width))), borderValue=(255,255,255))

# Padding

def pad(img):
    height, width = img.shape[:2]
    new_width = width + 600
    new_height = height + 338
    new_img = 255 * np.ones((new_height, new_width, 3), dtype="uint8")
    start_row = 169
    start_col = 300
    new_img[start_row:start_row + height, start_col:start_col + width, :] = img
    original_size = (1280, 720)
    img_resized = cv2.resize(new_img, original_size, interpolation=cv2.INTER_CUBIC)
    return img_resized

def giveCoordinates(image):
    image = cv2.resize(image, (380, 380))
    expandedImage = np.expand_dims(image, axis=0)
    coordinates = segmentationModel.predict(expandedImage)
    coordinates = coordinates[0].astype(int)
    return coordinates

def croppingSegmentatedImages(coordinates, image):
    x1, y1, x2, y2, x3, y3, x4, y4 = coordinates
    top_left_x = min([x1,x2,x3,x4])
    top_left_y = min([y1,y2,y3,y4]) 
    bot_right_x = max([x1,x2,x3,x4]) + 20
    bot_right_y = max([y1,y2,y3,y4]) 
    
    height, width = image.shape[:2]
    new_width = width + 20
    new_height = height
    new_img = 255 * np.ones((new_height, new_width, 3), dtype="uint8")
    start_row = 0
    start_col = 10
    new_img[start_row:start_row + height, start_col:start_col + width, :] = image

    croppedImage = new_img[top_left_y:bot_right_y, top_left_x:bot_right_x]
    croppedImage = cv2.resize(croppedImage, (1280, 720))
    return croppedImage


def segmentation(image):
    image = deskewImage(image)
    image = pad(image)
    coordinates = giveCoordinates(image)
    croppedImage = croppingSegmentatedImages(coordinates, image)
    return croppedImage