import cv2
import zmq
import argparse
import numpy as np
import datetime

args = argparse.ArgumentParser()
args.add_argument("-i", "--ip", type=str,
                  help="ip address of the server to which the client will connect")

args.add_argument("-p", "--port", type=str, default="5555",
                  help="port number of the server to which the client will connect")

args = vars(args.parse_args())
