#!/usr/bin/python3
import sys
import signal

statusCode = {"200": 0,
              "301": 0,
              "400": 0,
              "401": 0,
              "403": 0,
              "404": 0,
              "405": 0,
              "500": 0}

counter = 0
count = 0


def interrupt_handler(signum, frame):
    print("File size: ", count, end=" ")
    for k in statusCode:
        print(f"{k}: {statusCode[k]}")


try:
    signal.signal(signal.SIGINT, interrupt_handler)
    for i in sys.stdin:
        for item in statusCode:
            count += int(i.split(" ")[-1])
            if item == i.split(" ")[-2]:
                statusCode[item] += 1
                # print(f"{item}: {statusCode[item]}")
        counter += 1
        if counter % 10 == 0:
            print("File size: ", count)
            for item in statusCode:
                print(f"{item}: {statusCode[item]}")
except KeyboardInterrupt:
    pass
