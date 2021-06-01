# **Finding Lane Lines on the Road** 
[![Udacity - Self-Driving Car NanoDegree](https://s3.amazonaws.com/udacity-sdc/github/shield-carnd.svg)](http://www.udacity.com/drive)



Overview
---

We use our eyes to determine where to go while driving. The lines on the road that indicate where the lanes are serve as a continual reference for steering the car. Naturally, one of the first things we would want to accomplish in the development of a self-driving vehicle is use an algorithm to automatically recognize lane lines.

Using Python and OpenCV, I will recognize lane lines in images and videos for this project. The term "Open-Source Computer Vision" refers to a software package that includes a number of helpful tools for evaluating images and addressing computer vision challenges.

Result output will look similar to this image below:


<img src="examples/laneLines_thirdPass.jpg" width="480" alt="Combined Image" />


The Project Pipeline
---

**Step 1:** Read input image/Frame

**Step 2:** Convert to grayscale image
**Step 3:** blur/smooth out image with Gaussian Blurring function
**Step 4:** Apply Canny for edge finder
**Step 5:** Detect lines in the Canny image with Hough Transform
**Step 6:** Infer Lanes using the slope and intercept from the lines
**Step 7:** Cut out only the area of interest since there may be multiple lines in the image
**Step 8:** Draw and overlay lines on orignal image


Running Pipeline
---

To run the project on images or videos available on device. Open up the Ipython NOteboom and follow the instructions. 
There is also a support for real time usage of the pipeline which is availabl in the video_pipeline.py file. It accesses the device camera and produces result in real time

