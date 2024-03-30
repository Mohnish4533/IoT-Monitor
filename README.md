# IoT-Monitoring-System

This is an IoT system for streaming multiple cameras on a network to a host device.

## Set Up
1. Install the required libraries
```
pip install -r requirements.txt
```
2. Run the below scripts on a streaming device and on a receivig device respectively

## Streaming

```
usage: streaming.py [-h] [-p PORT] [-i IP] [-nc NUM_CAMERA]

optional arguments:
  -h, --help            show this help message and exit
  -p PORT, --port PORT  port number
  -i IP, --ip IP        ip address
  -nc NUM_CAMERA, --num_camera NUM_CAMERA
                        camera number
```

## Viewing

```
usage: viewing.py [-h] [-i IP] [-p PORT]

optional arguments:
  -h, --help            show this help message and exit
  -i IP, --ip IP        ip address of the server to which the client      
                        will connect
  -p PORT, --port PORT  port number of the server to which the client     
                        will connect
```
