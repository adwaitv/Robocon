#!/usr/bin/env python
from __future__ import print_function
import rospy
from final_task.srv import *
import numpy as np
import cv2

def lidar_client(centerX,centerY):
    rospy.wait_for_service('scan')
    try:
        scan = rospy.ServiceProxy('scan',lidar)
        resp = scan(centerX,centerY)
        return resp.lidar_array
    except rospy.ServiceException as e:
        pass

def plot(centerX,centerY):
    lidar_array = []
    lidar_array = lidar_client(centerX,centerY)
    if(lidar_array!=None):
        # Convert the lidar array to polar coordinates
        angles = np.deg2rad(lidar_array[::2])  # Get the angles from the array
        distances = lidar_array[1::2]  # Get the distances from the array

        # Convert polar coordinates to Cartesian coordinates
        x = (distances * np.cos(angles)).astype(int)
        y = (distances * np.sin(angles)).astype(int)

        # Offset the coordinates to the image center
        x += centerX
        y += centerY
            # Draw the lidar points on the image
        for i in range(len(x)):
            cv2.circle(image, (x[i], y[i]), 1, (0, 0, 0), -1)
         
 
if __name__ == "__main__":
    width, height = 400, 400
    x = np.linspace(0,width,int(width/20),dtype=int)
    y = np.linspace(0,height,int(height/20),dtype=int)
    global image
    image = np.zeros((height, width, 3), np.uint8)
    image[:] = (255, 255, 255)
    for i in range(20):
        for j in range(20):
            plot(x[i],y[j])

    
    # Save the image
    image_path = "lidar_image.png"
    cv2.imwrite(image_path, image)

    print("Image saved as", image_path)