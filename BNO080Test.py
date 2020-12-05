import board
import busio
import adafruit_bno08x

i2c = busio.I2C(board.SCL, board.SDA)
bno = adafruit_bno08x.BNO08X(i2c)

while True:
    quat = bno.rotation_vector
    print("Rotation Vector Quaternion:")
    print("I: %0.3f J: %0.3f K: %0.3f Accuracy: %0.3f"%(quat.i, quat.j, quat.k, quat.accuracy))