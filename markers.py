#!/usr/bin/env python

from __future__ import print_function
import cv2
from ar_markers import detect_markers
import numpy as np
import sys
import urllib

if sys.version_info[0] == 3:
    from urllib.request import urlopen
else:
    # Not Python 3 - today, it is most likely to be Python 2
    # But note that this might need an update when Python 4
    # might be around one day
    from urllib import urlopen


url='http://192.168.1.9:8080/shot.jpg?rnd=198779'
print('Press "q" to quit')
while True:
    # Your code where you can use urlopen
    with urlopen('http://192.168.1.9:8080/shot.jpg?rnd=198779') as url:
        #s = url.read()
        imgNp=np.array(bytearray(url.read()))
        img=cv2.imdecode(imgNp,-1)

        if __name__ == '__main__':

            markers = detect_markers(img)
            for marker in markers:
                    marker.highlite_marker(img)
            cv2.imshow('Test Frame', img)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            #frame_captured, frame = capture.read()

            # When everything done, release the capture
cv2.destroyAllWindows()
