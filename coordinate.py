from pipython import GCSDevice
from time import sleep
from operational import home


def transform(pidevice, direction):
    """
    Command the hexapod to move to its home position.
    Record the values of X, Y, and Z.
    Command the hexapod to move 500 microns in x-prime.
    Record the values of X, Y, and Z.
    Return the hexapod to its home position.
    Repeat for y-prime and z-prime.
    """
    home(pidevice)
    pidevice.MOV({direction: 0.500})
    sleep(1)

    home(pidevice)


with GCSDevice("C-184") as pidevice:
    pidevice.InterfaceSetupDlg()
    transform(pidevice, "X")
    transform(pidevice, "Y")
    transform(pidevice, "Z")
