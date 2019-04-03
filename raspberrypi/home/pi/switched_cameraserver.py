#!/usr/bin/env python3
'''Uses the CameraServer class to automatically capture video from two USB
webcams and send one of them to the dashboard without doing any processing.
To switch between the cameras, change the /CameraPublisher/selected value in NetworkTables

Warning: If you're using this with a python-based robot, do not run this
in the same program as your robot code!
'''

from cscore import CameraServer, UsbCamera
import networktables

def main():
    cs = CameraServer.getInstance()
    cs.enableLogging()

    usb0 = UsbCamera('Camera 0', 0)
    usb0.setFPS(10)
    usb0.setResolution(176, 144)
    usb1 = UsbCamera('Camera 1', 1)
    usb1.setFPS(10)
    usb1.setResolution(176, 144)

    # We "bounce" between these two camera objects using a Command on
    # the robot.
    cams = [usb0, usb1]

    # Add a "Switched" camera opject to Network Tables,
    # and set the source to the first camera (usb0).
    server = cs.addSwitchedCamera('Switched')
    server.setSource(cams[0])
    server.setFPS(10)
    server.setCompression(80)
    server.setResolution(176, 144)


    def _listener(source, key, value, isNew):
        '''Use networktables to switch the camera source.
        We set the camera source to the camera object in the "cams"
        dictionary. We use the bitwise Exclusive Or of "value" to index
        the array (see https://wiki.python.org/moin/BitwiseOperators for
        bit operators).

        "value" MUST be 0 (zero) or 1 (one) in order for this to work
        '''
        # print("cams[int(value)]: value: {} cams: {}".format(int(value), cams[int(value)]))
        # print("usb0: {}   usb1: {}".format(usb0, usb1))
        server.setSource(cams[int(value)])

    table = networktables.NetworkTables.getTable('/CameraPublisher')
    table.putNumber('selected', 0)
    table.addEntryListener(_listener, key='selected')

    cs.waitForever()


if __name__ == '__main__':

    # To see messages from networktables, you must setup logging
    import logging

    logging.basicConfig(level=logging.ERROR)

    # You should change this to connect to the RoboRIO
    networktables.NetworkTables.initialize(server='10.59.3.2')

    main()
