#!/usr/bin/python3

import pyping
import os

ei1pod = pyping.ping('ei11.customer.com')
ei2pod = pyping.ping('ei21.customer.com')
ei3pod = pyping.ping('ei3.customer.com')
ei4pod = pyping.ping('ei4.customer.com')


def ping_function():
    print("Verifying if the destination are reachable")
    if ei1pod.ret_code == 0:
        print("ei1.customer.com POD success!")
    else:
        print("Failed with {}".format(ei1pod.ret_code))
        global podError
        podError = "EI-1 POD is Down!!!"
        createSendEmail()

    if ei2pod.ret_code == 0:
        print("ei2.customer.com POD success!")
    else:
        print("Failed with {}".format(ei2pod.ret_code))
        podError = "EI-2 POD is Down!!!"
        createSendEmail()

    if ei3pod.ret_code == 0:
        print("ei3.customer.com POD success!")
    else:
        print("Failed with {}".format(ei3pod.ret_code))
        podError = "EI-3 POD is Down!!!"
        createSendEmail()

    if ei4pod.ret_code == 0:
        print("ei4.customer.com POD success!")
    else:
        print("Failed with {}".format(ei4pod.ret_code))
        podError = "EI-4 POD is Down!!!"
        createSendEmail()


def verify_function():
    print ("Validating all fields")
    if (ei1pod.ret_code == 0 and
            ei2pod.ret_code == 0 and
            ei3pod.ret_code == 0 and
            ei4pod.ret_code == 0):
        print ("All PODs are responding, moving forward...")
        fileStatus = open("carvalho.txt", "w+")
        fileStatus.write("Woops! Some of your services is reporting status == DOWN!")
        fileStatus.close()
    else:
        print ("All, or one of the PODs are down, connect to the VPN first")
#        os.system('mutt -s "Testing Mutt" jcarvalhodt2@gmail.com < carvalho.txt')


def createSendEmail():
    print ("Creating file with the error...")
    print (podError)
    fileStatus = open("carvalho.txt", "w+")
    fileStatus.write(podError)
    fileStatus.close()
    print ("Sending Email to the recipients")
    os.system('mutt -s "Testing Mutt" myemail@gmail.com < carvalho.txt')

# Driver Code
ping_function()
# verify_function()
