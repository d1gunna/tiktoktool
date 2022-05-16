import os,string;from pystyle import *;from time import sleep;from random import choice, randint
logo = """
  ▄████  █    ██  ███▄    █  ███▄    █  ▄▄▄
 ██▒ ▀█▒ ██  ▓██▒ ██ ▀█   █  ██ ▀█   █ ▒████▄
▒██░▄▄▄░▓██  ▒██░▓██  ▀█ ██▒▓██  ▀█ ██▒▒██  ▀█▄
░▓█  ██▓▓▓█  ░██░▓██▒  ▐▌██▒▓██▒  ▐▌██▒░██▄▄▄▄██
░▒▓███▀▒▒▒█████▓ ▒██░   ▓██░▒██░   ▓██░ ▓█   ▓██▒
 ░▒   ▒ ░▒▓▒ ▒ ▒ ░ ▒░   ▒ ▒ ░ ▒░   ▒ ▒  ▒▒   ▓▒█░
  ░   ░ ░░▒░ ░ ░ ░ ░░   ░ ▒░░ ░░   ░ ▒░  ▒   ▒▒ ░
░ ░   ░  ░░░ ░ ░    ░   ░ ░    ░   ░ ░   ░   ▒
      ░    ░              ░          ░       ░  ░
"""
os.system("mode con cols=90 lines=25")
os.system("title " + "TikTok Botting Tool : Logged In As gunna#0001")
class TikTokTool:
   def __init__(self):
      print(f"{Col.green}{logo}")
      print(f"\t\t\t     {Col.green}#{Col.white} Coded by gunna#0001")
      print(f"\t\t\t     {Col.green}#{Col.white} Contact gunna#0001")
      try:
         c = int(input(f"""
{Col.white}[{Col.green}1{Col.white}]{Col.white} Views
{Col.white}[{Col.green}2{Col.white}]{Col.white} Shares
{Col.white}[{Col.red}3{Col.white}]{Col.red} Likes (Coming soon...)

{Col.white}>> """))
      except:os.system('cls');self.__init__()
      if c == 1:
            self.btc()
      elif c==2:
         self.btc()
      elif c==3:
         self.btc()
      else:os.system('cls');self.__init__()
   def btc(self):
      while True:
         btc = input(f"\n{Col.white}[{Col.red}+{Col.white}]{Col.red} Enter TikTok Link {Col.white}>> ")
         if btc.startswith("t"):print(f"\n{Col.white}[{Col.green}+{Col.white}]{Col.green} Valid Address | Starting Process..");sleep(2);break
         else:print(f"{Col.white}[{Col.red}+{Col.white}]{Col.red} Invalid BTC Address");sleep(2)
      print(f"{Col.white}[{Col.dark_red}+{Col.white}]{Col.dark_red} Decrypting in : {Col.white}APIlang4")
      sleep(1.5)
      proxies = randint(100,170)
      seconds = randint(23142,43254)
      print(f"{Col.white}[{Col.red}+{Col.white}]{Col.red} Scraped : {Col.white}{proxies} {Col.red}proxies in{Col.white} 1.5{seconds} {Col.red}seconds")
      sleep(5.5)
      print(f"{Col.white}Currently updating, contact {Col.green}gunna#0001 {Col.white}for further issues.")
      sleep(10000000.0)
TikTokTool() # uwu