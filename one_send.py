
import serial
import time


def send_receive(send_data):
    serial_obj = serial.Serial('COM3', 115200)
    if serial_obj.isOpen():
        print('open success.')
    else:
        print('open fail.')
        return

    send_result = serial_obj.write(send_data)
    print('send_result=' + str(send_result))

    while True:
        count = serial_obj.inWaiting()
        if count > 0:
            print('count=' + str(count))
            data = serial_obj.read(count)
            if data == b'':
                time.sleep(0.5)
                continue
            print('data=' + str(data))
            if str(data).find('exit.') != -1:
                break
        time.sleep(0.1)

    serial_obj.close()


if __name__ == '__main__':
    head = bytes([0x4D, 0x43, 0x01, 0x01, 0x00, 0x00, 0x00, 0x00])
    print('head=' + str(head))

    send_receive(head)
