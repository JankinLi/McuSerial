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

            if len(data) < 2:
                continue

            if data[2] == 0x0E:
                print('error occur. code=' + str(data[3]))
                break

            if data[0] == 0xf7 and data[1] == 0xf8 and data[2] == 0x04 and data[3] == 0x01:
                data_1 = bytes([0xF7, 0xF8, 0xC1, 0x01, 0x02, 0x01, 0x00, 0x4d, 0x43, 0x44, 0x00, 0x00, 0x00, 0x00,
                                0x00, 0xFD])
                send_result = serial_obj.write(data_1)
                print('send_result=' + str(send_result))

            elif data[0] == 0xf7 and data[1] == 0xf8 and data[2] == 0x04 and data[3] == 0x05:
                data_1 = bytes([0xF7, 0xF8, 0x6, 0x07, 0xFD])
                send_result = serial_obj.write(data_1)
                print('send_result=' + str(send_result))
                break

        time.sleep(0.1)

    serial_obj.close()


if __name__ == '__main__':
    serial_obj = serial.Serial('COM5', 2400)
    if serial_obj.isOpen():
        print('open success.')
    else:
        print('open fail.')
        sys.exit(1)

    t = threading.Thread(target=receive_reply)
    t.start()
