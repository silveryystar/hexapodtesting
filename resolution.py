from pipython import GCSDevice
from time import sleep
from operational import home
import random


def resolution_req(pidevice):
    """
    Command the hexapod to move to its home position.
    Record the values of X, Y, and Z.
    Command the hexapod to move 5 microns in z-prime.
    Verify from the measured values of (X, Y, Z) that the motion was achieved.
    Command the hexapod to move 2 microns in x-prime.
    Verify from the measured values of (X, Y, Z) that the motion was achieved.
    Repeat for y-prime.
    Repeat at a variety of hexapod positions (i.e., starting from somewhere other than the home position).
    """
    home(pidevice)
    pidevice.MOV({"Z": 0.005})
    print(pidevice.qPOS())
    sleep(1)

    pidevice.MOV({"X": 0.002})
    print(pidevice.qPOS())
    sleep(1)

    pidevice.MOV({"Y": 0.002})
    print(pidevice.qPOS())
    sleep(1)

    rand_x = random.uniform(-25, 25)  # Random floats.
    rand_y = random.uniform(-25, 25)
    rand_z = random.uniform(-25, 25)
    print(rand_x, rand_y, rand_z)

    home(pidevice)
    pidevice.MOV({"X": rand_x, "Y": rand_y, "Z": rand_z})
    print(pidevice.qPOS())
    sleep(1)

    pidevice.MOV({"Z": rand_z+0.005})
    print(pidevice.qPOS())
    sleep(1)

    pidevice.MOV({"X": rand_x+0.002})
    print(pidevice.qPOS())
    sleep(1)

    pidevice.MOV({"Y": rand_y+0.002})
    print(pidevice.qPOS())
    sleep(1)


with GCSDevice("C-184") as pidevice:
    pidevice.InterfaceSetupDlg()
    resolution_req(pidevice)
