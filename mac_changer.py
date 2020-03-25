import sys
import os
import random
import colorama
from colorama import *
colorama.init()
def main():
 mac=generate_new_mac()
 change_mac(mac)
def generate_new_mac():
 result=""
 sym=['a','b','c','d','e','f','1','2','3','4','5','6','7','8','9','0']
 for i in range(0,3):
  result+=random.choice(sym)+random.choice(sym)+':'
 result='b4:2e:99:'+result[:-1]
 print(Fore.GREEN+"Generated NEW MAC: {}".format(result.upper())+Fore.RESET)
 return result
def change_mac(mac):
 os.system('ifconfig '+sys.argv[1]+' down && ifconfig '+sys.argv[1]+' hw ether '+mac.strip()+' && ifconfig '+sys.argv[1]+' up') 
main()
