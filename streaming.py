import cv2
import numpy as np
import zmq
import argparse

camera = []

ap = argparse.ArgumentParser()
ap.add_argument("-p", "--port", type=int, default=5555,
                help="port number")
ap.add_argument("-i", "--ip", type=str,
                help="ip address")
ap.add_argument("-nc", "--num_camera", type=int, default=1,
                help="camera number")

args = vars(ap.parse_args())
print(args)

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
     print(args["num_camera"])
     brute_check(args["num_camera"])