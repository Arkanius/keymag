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
Principal()

print ('''
[\033[1;91m*\033[1;m] Modo quebra de chaves.\n
OBS: É necessário que a Wordlist e o arquivo -01.cap esteja na mesma pasta dos scripts.
  ''');

rIWL = raw_input("\033[1;36mDigite a nome da Worldlist: \033[1;m");
rI01CAP = raw_input("\033[1;36mDigite a nome do arquivo -01.cap: \033[1;m");
print ("\n")
print ("Aguarde...\n");
while True:
  os.system ("sudo aircrack-ng -w "), rIWL, (" "), rI01CAP
  break