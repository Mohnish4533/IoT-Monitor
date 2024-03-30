import cv2
import numpy as np
import zmq
import argparse

camera = []

def brute_check(nc):
        """ 
            Iterates over video ports brutishly
        """
        index = 0
        curr_camera_count = 0
        
        while True:
            cap = cv2.VideoCapture(index)
            
            if not cap.read()[0]:
                if curr_camera_count == nc:
                    cap.release()
                    break
            else:
                camera.append(index)
                curr_camera_count += 1
            
            cap.release()
            index += 1

        print(f"Available cameras: {camera}")


if __name__ == "__main__":
     brute_check(1)
