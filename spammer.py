import time;import requests;import pyfiglet;import pystyle ;import threading;from pystyle import Colorate, Colors, Add; import keyboard; import os 
import telegram
os.system("title Telegram Spammer - [@natrixdev]")
banner = pyfiglet.figlet_format("TELEGRAM SPAMMER")
print(banner)
print(Colorate.Horizontal(Colors.blue_to_red, "@natrixdev on github"))
print('');print('')
z = print(Colorate.Horizontal(Colors.green_to_red, "[Console]"));print('')
v = Colorate.Horizontal(Colors.green_to_red, "[>]")
inf = Colorate.Horizontal(Colors.green_to_red, "[Info]")
y = " User to spam: "
ed = " Message to spam: "
rt = " Saved User: "
one = Colorate.Horizontal(Colors.blue_to_red, "[1]")
two = Colorate.Horizontal(Colors.blue_to_red, "[2]")
msg = input(v + y)
acc = Colorate.Horizontal(Colors.red_to_white, msg)
print('')
print(inf + rt + acc)
print('')
print('')
msg1 = input(v + ed)
acc1 = Colorate.Horizontal(Colors.blue_to_green, msg1)
while True:
    print(inf + " Spamming " + acc1 + " on " + acc)
    message = telegram.newMessage("@"+acc : acc1)
    telegram.send(message)
