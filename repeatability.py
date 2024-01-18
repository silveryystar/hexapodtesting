from pipython import GCSDevice
from time import sleep
from operational import home
import random


def repeatability_req(pidevice, direction):
    """
    Command the hexapod to move to its home position.
    Record the values of X, Y, and Z.
    Command the hexapod to move 100 microns in z-prime, then -100 microns in z-prime (i.e., back to the home position).
    Verify from the measured values of (X, Y, Z) that the position is within 5 microns of the home position.
    Command the hexapod to move 100 microns in x-prime, then -100 microns in x-prime (i.e., back to the home position).
    Verify from the measured values of (X, Y, Z) that the position is within 2 microns of the home position.
    Repeat for y-prime.
    Repeat at a variety of hexapod positions (i.e., starting from somewhere other than the home position).
    """
    home(pidevice)
    pidevice.MOV({direction: 0.100})
    print(pidevice.qPOS())
    sleep(1)

    pidevice.MOV({direction: -0.100})
    print(pidevice.qPOS())

    rand_x = random.uniform(-25, 25)
    rand_y = random.uniform(-25, 25)
    rand_z = random.uniform(-25, 25)
    print(rand_x, rand_y, rand_z)

    home(pidevice)
    pidevice.MOV({"X": rand_x, "Y": rand_y, "Z": rand_z})
    print(pidevice.qPOS())

    # Determines correct direction to move hexapod.
    if direction == "X":
        start = rand_x
    elif direction == "Y":
        start = rand_y
    else:
        start = rand_z

    pidevice.MOV({direction: start+0.100})
    print(pidevice.qPOS())
    sleep(1)

    pidevice.MOV({direction: start-0.100})
    print(pidevice.qPOS())


with GCSDevice("C-184") as pidevice:
    pidevice.InterfaceSetupDlg()
    repeatability_req(pidevice, "Z")
    repeatability_req(pidevice, "X")
    repeatability_req(pidevice, "Y")
