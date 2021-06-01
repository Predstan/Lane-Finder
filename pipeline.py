#importing some useful packages
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2
import math





def grayscale(img):
    """
    Applies the Grayscale transform
    This will return an image with only one color channel
    but NOTE: to see the returned image as grayscale
    (assuming your grayscaled image is called 'gray')
    you should call plt.imshow(gray, cmap='gray')
    """
    return cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    # Or use BGR2GRAY if you read an image with cv2.imread()
    # return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
def canny(img, low_threshold, high_threshold):
    """Applies the Canny transform"""
    return cv2.Canny(img, low_threshold, high_threshold)

def gaussian_blur(img, kernel_size):
    """Applies a Gaussian Noise kernel"""
    return cv2.GaussianBlur(img, (kernel_size, kernel_size), 0)

def region_of_interest(img, vertices):
    """
    Applies an image mask.
    
    Only keeps the region of the image defined by the polygon
    formed from `vertices`. The rest of the image is set to black.
    `vertices` should be a numpy array of integer points.
    """
    #defining a blank mask to start with
    mask = np.zeros_like(img)   
    
    #defining a 3 channel or 1 channel color to fill the mask with depending on the input image
    if len(img.shape) > 2:
        channel_count = img.shape[2]  # i.e. 3 or 4 depending on your image
        ignore_mask_color = (255,) * channel_count
    else:
        ignore_mask_color = 255
        
    #filling pixels inside the polygon defined by "vertices" with the fill color    
    cv2.fillPoly(mask, vertices, ignore_mask_color)
    
    #returning the image only where mask pixels are nonzero
    masked_image = cv2.bitwise_and(img, mask)
    return masked_image


def draw_lines(img, lines, color=[250, 0, 0], thickness=8):
    """
    
    This function draws `lines` with `color` and `thickness`.    
    Lines are drawn on the image inplace (mutates the image).
    """
    for line in lines:
        for x1,y1,x2,y2 in line:
            cv2.line(img, (x1, y1), (x2, y2), color, thickness)

def hough_lines(img, rho, theta, threshold, min_line_len, max_line_gap):
    """
    `img` should be the output of a Canny transform.
        
    Returns an image with hough lines drawn.
    """
    lines = cv2.HoughLinesP(img, rho, theta, threshold, np.array([]), minLineLength=min_line_len, maxLineGap=max_line_gap)
    return lines

# Python 3 has support for cool math symbols.

def weighted_img(img, initial_img, α=0.8, β=1., γ=0.):
    """
    `img` is the output of the hough_lines(), An image with lines drawn on it.
    Should be a blank image (all black) with lines drawn on it.
    
    `initial_img` should be the image before any processing.
    
    The result image is computed as follows:
    
    initial_img * α + img * β + γ
    NOTE: initial_img and img must be the same shape!
    """
    return cv2.addWeighted(initial_img, α, img, β, γ)




class line():
    """
    Defining a line Class. A line will have a coordinate, slope and an intercept
    where y = Mx + b
    """
    def __init__(self, coordinate):
        x1, y1, x2, y2 = coordinate
        self.coordinates = coordinate
        self.slope = (y2 - y1) / (x2 - x1 + np.finfo(float).eps)
        self.b_line = y1 - self.slope * x1


def get_slope(coordinate):
    """
    Return slope and coordinates given the coordinates
    """
    x1, y1, x2, y2 = coordinate
    slope = (y2 - y1) / (x2 - x1 + np.finfo(float).eps)
    b_line = y1 - slope * x1
    return slope, b_line


def get_lanes(lines, img):
    """
    Returns infered lanes given the Hough transformed lines and the original image
    """
    

#     # convert to grayscale
#     im = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

#     # perform gaussian blur
#     im = gaussian_blur(im, 17)

#     # perform edge detection
#     im = canny(im, 50, 80)

#     # perform hough transform
#     _, lines = hough_lines(img=im,
#                        rho=2,
#                        theta=np.pi / 180,
#                        threshold=1,
#                        min_line_len=15,
#                        max_line_gap=5)
    left_lane = []
    right_lane = []
    
    for l in lines:
        l = l[0]
        slope, bias = get_slope(l)
        if 0.5 <= np.abs(slope) <= 2:
            if slope < 0:
                left_lane.append(line(l))
            elif slope > 0:
                right_lane.append(line(l))
            
            
    left_bias = np.median([l.b_line for l in left_lane]).astype(int)
    left_slope = np.median([l.slope for l in left_lane])
    x1, y1 = 0, left_bias
    x2, y2 = -np.int32(np.round(left_bias / left_slope)), 0
    left_lane = (x1, y1, x2, y2)
    
    right_bias = np.median([l.b_line for l in right_lane]).astype(int)
    right_slope = np.median([l.slope for l in right_lane])
    x1, y1 = 0, right_bias
    x2, y2 = np.int32(np.round((img.shape[0] - right_bias) / right_slope)), img.shape[0]
    right_lane = (x1, y1, x2, y2)
    
    return right_lane, left_lane



def fetchline(image, canny_threshold = (50,80 ), 
              kernel_size=17,hough_threshold= 1 , min_line_len = 15, max_line_gap= 5,
              theta = np.pi/180, rho=2, straight = False):
    
    """
    Builds the Piepline for drawing the line
    Returns Image of drawn lanes
    """
    image = cv2.resize(image, (960, 540))
    img=image
    im = grayscale(image)
    im = gaussian_blur(im, kernel_size)
    
    
    low, high = canny_threshold
    im = canny(im, low, high)
    
    imshape = im.shape
    vertices = np.array([[(0,imshape[0]),(450, 320), (490, 310), (imshape[1],imshape[0])]], \
                        dtype=np.int32)
    im = region_of_interest(im, vertices)
  
    lines= hough_lines(im, rho, theta, hough_threshold, min_line_len, max_line_gap)
 
    line_img = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)

    if straight:
        lines= [get_lanes(lines, img)]
        draw_lines(line_img, lines)
        line_img =region_of_interest(line_img, vertices)
    else:
         draw_lines(line_img, lines)
  
    im= weighted_img(line_img, initial_img=image, α=0.8, β=1., γ=0.)
  
    return im