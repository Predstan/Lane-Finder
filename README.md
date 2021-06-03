# **Finding Lane Lines on the Road** 
[![Udacity - Self-Driving Car NanoDegree](https://s3.amazonaws.com/udacity-sdc/github/shield-carnd.svg)](http://www.udacity.com/drive)



Overview
---

We use our eyes to determine where to go while driving. The lines on the road that indicate where the lanes are serve as a continual reference for steering the car. Naturally, one of the first things we would want to accomplish in the development of a self-driving vehicle is use an algorithm to automatically recognize lane lines.

Using Python and OpenCV, I will recognize lane lines in images and videos for this project. The term "Open-Source Computer Vision" refers to a software package that includes a number of helpful tools for evaluating images and addressing computer vision challenges.

Result output will look is attached to this image below:


<img src="examples/laneLines_thirdPass.jpg" width="480" alt="Combined Image" />

Running Pipeline
---

To Run

Step 1: Install Python 3

To run this project, you will need Python 3 along with the numpy, matplotlib, and OpenCV libraries, as well as Jupyter Notebook installed.

Choose the appropriate Python 3 Anaconda install package for your operating system here. Download and install the package.

If you already have Anaconda for Python 2 installed, you can create a separate environment for Python 3 and all the appropriate dependencies with the following command:

> conda create --name=yourNewEnvironment python=3 anaconda

> source activate yourNewEnvironment

Step 2: Installing OpenCV

Once you have Anaconda installed, first double check you are in your Python 3 environment:

>python


run the following commands at the terminal prompt to get OpenCV:

> pip install pillow
> conda install -c https://conda.anaconda.org/menpo opencv3

then to test if OpenCV is installed correctly:

> python
>>> import cv2

Step 3: Installing moviepy

"moviepy" is recommended for this project

To install moviepy run:

>pip install moviepy

Step 4: Opening the code in a Jupyter Notebook

This project will be completed in a Jupyter notebook. If you're new to Jupyter Notebooks, Cyrille Rossant's Basics of Jupyter Notebook and Python is a good place to start.

Jupyter is an interactive Python notebook that allows you to execute code blocks and view the results in real time. This project's code is all contained in a Jupyter notebook. Run the following command at the terminal prompt to launch Jupyter in your browser (make sure you're in your Python 3 environment!):

step 4.1: There is also a support for real time usage of the pipeline which is available in the video_pipeline.py file. It accesses the device camera and produces result in real time

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






