import serial
import sys
import time
import threading


def receive_reply():
    receive_count = 0
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
                print('code=' + str(data[3]))
                print('receive_count=' + str(receive_count))
                receive_count = receive_count + 1
                if receive_count > 10:
                    data_0x06_0x01_2 = bytes([0x4D, 0x43, 0x06, 0x01, 0x01, 0x00, 0x00, 0x00, 0x03])
                    serial_obj.write(data_0x06_0x01_2)
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

    data_0x06_0x01 = bytes([0x4D, 0x43, 0x06, 0x01, 0x01, 0x00, 0x00, 0x00, 0x02])
    send_result = serial_obj.write(data_0x06_0x01)
    print('send_result=' + str(send_result))
