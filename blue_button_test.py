import serial
import sys
import time
import threading


def receive_reply():

    while True:
        count = serial_obj.inWaiting()
        if count > 0:
            print('count=' + str(count))
            data = serial_obj.read(count)
            if data == b'':
                time.sleep(0.5)
                continue
            print('data=' + str(data))

            if str(data).find('no space') != -1:
                print('no space occur.')
                break
        time.sleep(0.1)

    serial_obj.close()


if __name__ == '__main__':
    serial_obj = serial.Serial('COM3', 115200)
    if serial_obj.isOpen():
        print('open success.')
    else:
        print('open fail.')
        sys.exit(1)

    t = threading.Thread(target=receive_reply)
    t.start()
