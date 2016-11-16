#!/usr/bin/env python

'''
Send ash data messages to pixhawk
'''

import sys, struct, time, os

from argparse import ArgumentParser
parser = ArgumentParser(description=__doc__)

parser.add_argument("--baudrate", type=int,
                  help="master port baud rate", default=115200)
parser.add_argument("--device", required=True, help="serial device")
parser.add_argument("--rate", default=4, type=int, help="requested stream rate")
parser.add_argument("--source-system", dest='SOURCE_SYSTEM', type=int,
                  default=255, help='MAVLink source system for this GCS')
parser.add_argument("--showmessages", action='store_true',
                  help="show incoming messages", default=False)
args = parser.parse_args()


from pymavlink import mavutil

def wait_heartbeat(m):
    '''wait for a heartbeat so we know the target system IDs'''
    print("Waiting for APM heartbeat")
    m.wait_heartbeat()
    print("Heartbeat from APM (system %u component %u)" % (m.target_system, m.target_system))


# create a mavlink serial instance
master = mavutil.mavlink_connection(args.device, baud=args.baudrate)

# wait for the heartbeat msg to find the system ID
wait_heartbeat(master)

while True:
	binCount0String = input("binCount0: ")
	binCount1String = input("binCount1: ")
	binCount2String = input("binCount2: ")
	binCount3String = input("binCount3: ")
	binCount4String = input("binCount4: ")
	binCount5String = input("binCount5: ")
	binCount6String = input("binCount6: ")
	binCount7String = input("binCount7: ")
	binCount8String = input("binCount8: ")
	binCount9String = input("binCount9: ")
	binCount10String = input("binCount10: ")
	binCount11String = input("binCount11: ")
	binCount12String = input("binCount12: ")
	binCount13String = input("binCount13: ")
	binCount14String = input("binCount14: ")
	binCount15String = input("binCount15: ")
	samplingPeriodString = input("samplingPeriod: ")
	myPM1String = input("myPM1: ")
	myPM3String = input("myPM3: ")
	myPM10String = input("myPM10: ")
	myPM17_5String = input("myPM17_5: ")
	totalConcString = input("totalConc: ")
	
	binCount0 = int(binCount0String)
	binCount1 = int(binCount1String)
	binCount2 = int(binCount2String)
	binCount3 = int(binCount3String)
	binCount4 = int(binCount4String)
	binCount5 = int(binCount5String)
	binCount6 = int(binCount6String)
	binCount7 = int(binCount7String)
	binCount8 = int(binCount8String)
	binCount9 = int(binCount9String)
	binCount10 = int(binCount10String)
	binCount11 = int(binCount11String)
	binCount12 = int(binCount12String)
	binCount13 = int(binCount13String)
	binCount14 = int(binCount14String)
	binCount15 = int(binCount15String)
	samplingPeriod = float(samplingPeriodString)
	myPM1 = float(myPM1String)
	myPM3 = float(myPM3String)
	myPM10 = float(myPM10String)
	myPM17_5 = float(myPM17_5String)
	totalConc = float(totalConcString)
	
	print("Sending ash data: %u, %u, %u, %u, %u, %u, %u, %u, %u, %u, %u, %u, %u, %u, %u, %u, %f, %f, %f, %f, %f, %f" % (binCount0, binCount1, binCount2, binCount3, binCount4, binCount5, binCount6, binCount7, binCount8, binCount9, binCount10, binCount11, binCount12, binCount13, binCount14, binCount15, samplingPeriod, myPM1, myPM3, myPM10, myPM17_5, totalConc))
	master.mav.send_ash_data_send(binCount0, binCount1, binCount2, binCount3, binCount4, binCount5, binCount6, binCount7, binCount8, binCount9, binCount10, binCount11, binCount12, binCount13, binCount14, binCount15, samplingPeriod, myPM1, myPM3, myPM10, myPM17_5, totalConc)
