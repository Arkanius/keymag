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
  Inicial1()

def Inicial3():
  print ('''
\n[*] keymag.py:

- Instala os componentes necessários para a invasão;
- Ativa o modo de monitoramento;
- Habilita o modo de Scaneamente de Rede Wireless próximas;

[*] keymag-dump.py:

- Coleta os pacotes brutos e dá informação após a injeção de frames;

[*] keymag-frame.py:

- Injeta o frames no rotiador alvo para conseguir autenticação da Worldlist.

[*] keymag-crack.py:

- Recolhe a Worldlist e tenta a chaves geradas nela em função do arquivo -01.cap.
    ''');
  raw_input("\033[1;36mPara voltar a menu principal, pressione ENTER...\033[1;m ");
  Principal()
  Inicial1()

def Inicial2():
  print ('''
MagnaSec é um grupo que sua ideologia é de um mundo melhor para todos, e sua missão é 
compartilhar todo o seu conhecimento sobre diversas áreas da Segurança da Informação.
O script keymag é o primeiro projeto que envolva Pentest, programado para facilitar 
o método de invasão em redes wireless (WPA/WP2), utilizando o seu esqueleto focado no
programa de quebra de chaves o, aircrack-ng.

[*] Mais informações:

Aircrack-ng: https://www.aircrack-ng.org/
MagnaSec: [Breve]
    ''');
  raw_input("\033[1;36mPara voltar a menu principal, pressione ENTER...\033[1;m ");
  Principal()
  Inicial1()

def Inicial1():
  print ('''
[*] Script destinado a um melhor progresso em invasões em redes Wireless.
[*] Selecione uma categoria abaixo:

1) Iniciar invasão;
2) Sobre a MagnaSec;
3) Ajuda;
    ''');
  rI1 = input("\033[1;36mOpção: \033[1;m")
  if rI1 == 1:
    print ('''
[\033[1;91m*\033[1;m] Começando o teste de invasão em redes Wireless...

Deseja instalar os componentes necessários para continuar?

1) Continuar e instalar;
2) Recusar;
      ''');
    rI11 = input("\033[1;36mOpção: \033[1;m");
    print ("\n");
    if rI11 == 1:
      print ('''
[\033[1;91m*\033[1;m] Aguarde enquanto instalamos os arquivos necessários...
Antes de tudo nos forneça a senha de root se caso precisar para continuar:
        ''');
      while True:
          os.system("sudo apt-get -y install aircrack-ng")
          break
      raw_input("[\033[1;32m*\033[1;m] Instalado com sucesso, pressione ENTER para continuar...\n");
      print ("\n")
      print ('''
[\033[1;91m*\033[0;0m] Inicie o keymag-monitor.py em outra janela de terminal.
        ''');
      raw_input("\033[1;36mSó pressione, ENTER, quando terminar todos os processos.\033[1;m ");
      while True:
        os.system("sudo airmon-ng stop mon0");
      print ("\n");
    elif rI11 == 2:
      Final()
    else:
      Final()
  elif rI1 == 2:
    Inicial2()
  elif rI1 == 3:
    Inicial3()
  else:
    Final()
Principal()
Inicial1()
