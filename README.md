# **Finding Lane Lines on the Road** 
[![Udacity - Self-Driving Car NanoDegree](https://s3.amazonaws.com/udacity-sdc/github/shield-carnd.svg)](http://www.udacity.com/drive)



Overview
---

We use our eyes to determine where to go while driving. The lines on the road that indicate where the lanes are serve as a continual reference for steering the car. Naturally, one of the first things we would want to accomplish in the development of a self-driving vehicle is use an algorithm to automatically recognize lane lines.

Using Python and OpenCV, I will recognize lane lines in images and videos for this project. The term "Open-Source Computer Vision" refers to a software package that includes a number of helpful tools for evaluating images and addressing computer vision challenges.

Result output will look similar to this image below:


<img src="examples/laneLines_thirdPass.jpg" width="480" alt="Combined Image" />
### Running 

To Run

Step 1: Install Python 3

To run this project, you will need Python 3 along with the numpy, matplotlib, and OpenCV libraries, as well as Jupyter Notebook installed.

I recommend downloading and installing the Anaconda Python 3 distribution from Continuum Analytics because it comes prepackaged with many of the Python dependencies you will need for this and future projects, makes it easy to install OpenCV, and includes Jupyter Notebook. Beyond that, it is one of the most common Python distributions used in data analytics and machine learning, so a great choice if you're getting started in the field.

Choose the appropriate Python 3 Anaconda install package for your operating system here. Download and install the package.

If you already have Anaconda for Python 2 installed, you can create a separate environment for Python 3 and all the appropriate dependencies with the following command:

> conda create --name=yourNewEnvironment python=3 anaconda

> source activate yourNewEnvironment

Step 2: Installing OpenCV

Once you have Anaconda installed, first double check you are in your Python 3 environment:

>python
Python 3.5.2 |Anaconda 4.1.1 (x86_64)| (default, Jul 2 2016, 17:52:12)
[GCC 4.2.1 Compatible Apple LLVM 4.2 (clang-425.0.28)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
(Ctrl-d to exit Python)

run the following commands at the terminal prompt to get OpenCV:

> pip install pillow
> conda install -c https://conda.anaconda.org/menpo opencv3

then to test if OpenCV is installed correctly:

> python
>>> import cv2
>>> (i.e. did not get an ImportError)

(Ctrl-d to exit Python)

Step 3: Installing moviepy

I recommend the "moviepy" package for processing video in this project (though you're welcome to use other packages if you prefer).

To install moviepy run:

>pip install moviepy

and check that the install worked:

>python
>>>import moviepy
>>> (i.e. did not get an ImportError)

(Ctrl-d to exit Python)

Step 4: Opening the code in a Jupyter Notebook

You will complete this project in a Jupyter notebook. If you are unfamiliar with Jupyter Notebooks, check out Cyrille Rossant's Basics of Jupyter Notebook and Python to get started.

Jupyter is an ipython notebook where you can run blocks of code and see results interactively. All the code for this project is contained in a Jupyter notebook. To start Jupyter in your browser, run the following command at the terminal prompt (be sure you're in your Python 3 environment!):

> jupyter notebook

A browser window will appear showing the contents of the current directory. Click on the file called "P1.ipynb". Another browser window will appear displaying the notebook. Follow the instructions in the notebook to complete the project.

The Project Pipeline
---

**Step 1:** Read input image/Frame

**Step 2:** Convert to grayscale image, This allows us to work on only one of the image's channels rather than all three (BGR). As a result, it is less computationally demanding.

**Step 3:** blur/smooth out image with Gaussian Blurring function, The picture is then blurred using Gaussian Blur.

**Step 4:** Apply Canny for edge finder, Then, on this smoothed picture, I used Canny Edge detection: Hyperparameter tuning is one of the most challenging in computer vision problems. To make the process faster and efficient, I used a simple GUI tool to search accross all paramters and choose the best one that produces more accurate result

**Step 5:** Detect lines in the Canny image with Hough Transform: This results in line segments with edges close to the lane lines. I used a mask to filter the area of interest. I deleted the margins in other regions of the picture since we're only interested in the boundaries in the location where we anticipate our road to be.

**Step 6:** Infer Lanes using the slope and intercept from the lines: extrapolated the left lane line and right lane line, based on the angle.

**Step 7:** Cut out only the area of interest since there may be multiple lines in the image

**Step 8:** Draw and overlay lines on orignal image: I used the cv2 line drawer to draw lane lines on the original image and returned.


Running Pipeline
---

To run the project on images or videos available on device. Open up the Ipython NOtebook and follow the instructions. 
There is also a support for real time usage of the pipeline which is available in the video_pipeline.py file. It accesses the device camera and produces result in real time

