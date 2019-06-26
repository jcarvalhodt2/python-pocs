#!/usr/bin/python3

"""This module is responsible to grab an information \
from a POD and send an email in case of failure. """

import os
import pyping


EI1POD = pyping.ping('ei11.customer.com')
EI2POD = pyping.ping('ei21.customer.com')
EI3POD = pyping.ping('ei3.customer.com')
EI4POD = pyping.ping('ei4.customer.com')


def ping_function():
    print "Verifying if the destination are reachable"
    if EI1POD.ret_code == 0:
        print "ei1.customer.com POD success!"
    else:
        print "Failed with {}".format(EI1POD.ret_code)
        global PODERROR
        PODERROR = "EI-1 POD is Down!!!"
        create_send_email()

    if EI2POD.ret_code == 0:
        print "ei2.customer.com POD success!"
    else:
        print "Failed with {}".format(EI2POD.ret_code)
        PODERROR = "EI-2 POD is Down!!!"
        create_send_email()

    if EI3POD.ret_code == 0:
        print "ei3.customer.com POD success!"
    else:
        print "Failed with {}".format(EI3POD.ret_code)
        PODERROR = "EI-3 POD is Down!!!"
        create_send_email()

    if EI4POD.ret_code == 0:
        print "ei4.customer.com POD success!"
    else:
        print "Failed with {}".format(EI4POD.ret_code)
        PODERROR = "EI-4 POD is Down!!!"
        create_send_email()


def verify_function():
    print "Validating all fields"
    if (EI1POD.ret_code == 0 and
            EI2POD.ret_code == 0 and
            EI3POD.ret_code == 0 and
            EI4POD.ret_code == 0):
        print "All PODs are responding, moving forward..."
        file_status = open("carvalho.txt", "w+")
        file_status.write("Woops! Some of your services is reporting status == DOWN!")
        file_status.close()
    else:
        print "All, or one of the PODs are down, connect to the VPN first"
#        os.system('mutt -s "Testing Mutt" your_email@gmail.com < carvalho.txt')


def create_send_email():
    print "Creating file with the error..."
    print PODERROR
    file_status = open("carvalho.txt", "w+")
    file_status.write(PODERROR)
    file_status.close()
    print "Sending Email to the recipients"
    os.system('mutt -s "Testing Mutt" your_email@gmail.com < carvalho.txt')

# Driver Code
ping_function()
# verify_function()
