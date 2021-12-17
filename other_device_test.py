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

            if data[2] == 0x0E:
                print('error occur. code=' + str(data[3]))
                break
        time.sleep(0.1)

    serial_obj.close()


if __name__ == '__main__':
    serial_obj = serial.Serial('COM5', 115200)
    if serial_obj.isOpen():
        print('open success.')
    else:
        print('open fail.')
        sys.exit(1)

    t = threading.Thread(target=receive_reply)
    t.start()

    data_0x08_0x02 = bytes([0x01, 0x00, 0x00, 0x00, 0x0B])
    send_result = serial_obj.write(data_0x08_0x02)
    print('send_result=' + str(send_result))
