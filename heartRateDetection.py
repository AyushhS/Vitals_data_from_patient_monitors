# Heart Rate Graph Detetction
# - Detect the HR graph in the image by first masking
#   the image for green colour and then finding the contours 
#   and determining the contour with the largest perimeter and then plotting it.
# - If the graph is not found through the above method then 
#   it uses neurokit2 library to simulate the graph using HR values 

def heart_rate_graph_detection(image,heart_rate_value):
  def normal_detect(vis2):
    # Convert the image to grayscale
    gray = rgb2gray(vis2)
    # Get the ECG signal from the grayscale image
    signal = np.mean(gray, axis=0)
    for i in range(len(signal) - 1, 0, -1):
      if signal[i] == 0.0:
        signal = np.delete(signal, i)
    # Plot the ECG signal
    plt.figure(figsize = (25, 5))
    plt.plot(signal,color='green')
    plt.title('Digitized ECG Signal')
    plt.ylabel('Amplitude (mV)')
    plt.show()
  
  def using_neurokit2(heart_rate_value):
    if heart_rate_value == -1:
      # print('yes')
      signal = np.zeros((400), dtype=int)
      plt.figure(figsize = (25, 5))
      plt.plot(signal,color='green')
      plt.title('Digitized ECG Signal')
      plt.ylabel('Amplitude (mV)')
      plt.show()
      return
    simulated_ecg = nk.ecg_simulate(duration=7, sampling_rate=1000, heart_rate=heart_rate_value,method="simple")
    nk.signal_plot(simulated_ecg, sampling_rate=1000,color='green')
  # Load the input image
  # image = cv2.imread("/content/hcgnagpur_icu_mon--401_2022_10_23_15_30_2.jpeg")
  h1, w1, c = image.shape
  # cv2_imshow(image)
  hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

  # lower bound and upper bound for Green color
  lower_bound = np.array([45, 50, 50])	 
  upper_bound = np.array([75, 255, 255])

  # find the colors within the boundaries
  mask = cv2.inRange(hsv, lower_bound, upper_bound)

  #define kernel size  
  kernel = np.ones((7,7),np.uint8)

  # Remove unnecessary noise from mask

  mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
  mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
  # Segment only the detected region
  segmented_img = cv2.bitwise_and(image, image, mask=mask)
  # Convert the image to grayscale
  gray = cv2.cvtColor(segmented_img, cv2.COLOR_BGR2GRAY)
  # blurred = cv2.GaussianBlur(gray, (5, 5), 0)

  # Threshold the image to create a binary image
  _, thresholded = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY)
  # cv2_imshow(thresholded)

  # h, w = thresholded.shape[:2]

  # Drop top and bottom area of image with black parts.
  # thresholded= thresholded[100:h-100, :]
  h, w = thresholded.shape[:2]

  # Find contours in the binary image
  contours, _ = cv2.findContours(thresholded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
  contours = [cv2.approxPolyDP(cnt, 3, True) for cnt in contours]

  # Draw all contours
  vis = np.zeros((h, w, 3), np.uint8)
  cv2.drawContours( vis, contours, -1, (128,255,255), 3, cv2.LINE_AA)

  # Draw the contour with maximum perimeter (omitting the first contour which is outer boundary of image
  # Not necessary in this case
  vis2 = np.zeros((h, w, 3), np.uint8)
  perimeter=[]
  for cnt in contours[1:]:
      perimeter.append(cv2.arcLength(cnt,True))
  # print(perimeter)
  # print (max(perimeter))
  maxindex= perimeter.index(max(perimeter))
  # print (maxindex)

  cv2.drawContours( vis2, contours, maxindex+1 , (0,255,0), -1)
  gray = cv2.cvtColor(vis2, cv2.COLOR_BGR2GRAY)
  _, threshold = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
  contours, _ = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

  # Select the largest contour
  contour = max(contours, key=cv2.contourArea)
  x, y, w, h = cv2.boundingRect(contour)
  if (w/w1)>0.4:
    normal_detect(vis2)
  else:
    using_neurokit2(heart_rate_value)