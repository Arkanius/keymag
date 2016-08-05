#!/usr/bin/python
# coding=UTF-8

import os, sys

def Principal():
	print ('''\033[1;36m
                      :::!~!!!!!:.
                  .xUHWH!! !!?M88WHX:.
                .X*#M@$!!  !X!M$$$$$$WWx:.
               :!!!!!!?H! :!$!$$$$$$$$$$8X:
              !!~  ~:~!! :~!$!#$$$$$$$$$$8X:
             :!~::!H!<   ~.U$X!?R$$$$$$$$MM!
             ~!~!!!!~~ .:XW$$$U!!?$$$$$$RMM!
               !:~~~ .:!M"T#$$$$WX??#MRRMMM!
               ~?WuxiW*`   `"#$$$$8!!!!??!!!
             :X- M$$$$       `"T#$T~!8$WUXU~
            :%`  ~#$$$m:        ~!~ ?$$$$$$
          :!`.-   ~T$$$$8xx.  .xWW- ~""##*"
.....   -~~:<` !    ~?T#$$@@W@*?$$      /`
W$@@M!!! .!~~ !!     .:XUW$W!~ `"~:    :
#"~~`.:x%`!!  !H:   !WM$$$$Ti.: .!WUn+!`
:::~:!!`:X~ .: ?H.!u "$$$B$$$!W:U!T$$M~
.~~   :X@!.-~   ?@WTWo("*$$$W$TH$! `
Wi.~!X$?!-~    : ?$$$B$Wu("**$RM!                 
$R@i.~~ !     :   ~$$$$$B$$en:``
?MXT@Wx.~    :     ~"##*$$$$M~\033[1;m
	\033[1;91m __  __                         ____            
	|  \/  | __ _  __ _ _ __   __ _/ ___|  ___  ___ 
	| |\/| |/ _` |/ _` | '_ \ / _` \___ \ / _ \/ __|
	| |  | | (_| | (_| | | | | (_| |___) |  __/ (__   \033[0;0m_\033[1;91m
	|_|  |_|\__,_|\__, |_| |_|\__,_|____/ \___|\___| \033[0;0m(_)\033[1;91m
	              |___/\033[0;0m
		''');

def Final():
  print ('''
[\033[1;91m*\033[0;0m] Comando não encontrado...
[\033[1;91m*\033[0;0m] Lamentamos o possível erro.
    ''');

Principal()

print ('''
[\033[1;91m*\033[0;0m] Modo de monitor de Redes Wireless próximos.
[\033[1;91m*\033[0;0m] Inicie o keymag-dump.py em outra janela de terminal logo após coletar os dados.
  ''');

raw_input("[\033[1;32m*\033[1;m]Pressione ENTER para continuar...\n");

print("Escolha a sua placa de rede de monitoramento: \n");
print ('''
1) mon0
2) wlan0mon
3) mon0wlan
4) 0mon
5) wlan0
6) 0wlan
  ''');
rInterface = input("\033[1;36mOpção: \033[1;m")
if rInterface == 1:
  while True:
    os.system("sudo airodump-ng mon0")
    break
elif rInterface == 2:
  while True:
    os.system("sudo airodump-ng wlan0mon")
    break
elif rInterface == 3:
   while True:
    os.system("sudo airodump-ng mon0wlan")
    break
elif rInterface == 4:
   while True:
    os.system("sudo airodump-ng 0mon")
    break
elif rInterface == 5:
  while True:
    os.system("sudo airodump-ng mon0")
    break
elif rInterface == 6:
  while True:
    os.system("sudo airodump-ng 0wlan")
    break
else:
  Final()