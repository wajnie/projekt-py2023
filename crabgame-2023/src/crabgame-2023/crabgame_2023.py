
import re
import pymem
import os
from time import sleep
# inicjalizacja, deklaracja podstawowych zmiennych
index = pymem.Pymem('Crab Game.exe') # proces
ga = pymem.process.module_from_name(index.process_handle, 'GameAssembly.dll') # uzyskiwanie modułu z wcześniej zdefiniowanego pliku
#gaBytes = index.read_bytes(ga.lpBaseOfDll, ga.SizeOfImage) czytanie bajtów z gameassembly

# modyfikacje
infskok = False
nokb = False
fastpunch = False

# -------- WYJAŚNIONE ZNACZENIA MODYFIKACJI ---------
# 1)
# Nieskończonego skoku nie trzeba tłumaczyć, modyfikuje regułę, 
# która odpowiada za warunek, w którym gracz musi stać na ziemi aby skoczyć.

# 2)
# Knockback, a właściwie jego brak to inaczej 
# usunięcie jakiegokolwiek odrzutu gracza, 
# który następuje, gdy przeciwny gracz go uderzy.

# 3)
# Istnieje limit prędkości ciosów na 
# sekundę, ponieważ autoclickery by były zbyt mocne.
# owy skrypt będzie się starał go pozbyć.

# prosty error handler
def ErrorReturn():
        os.system('cls')
        print('[!] Nie mozesz wlaczyc tej samej modyfikacji 2 razy.')
        sleep(3)
        os.system('cls')

# główna pętla
while True:
     print('Wybierz liczbe od 1-3 aby wprowadzic modyfikacje do gry.\n')
     print('1) Nieskonczony skok')
     print('2) 0% Knockback')
     print('3) Szybkie uderzanie\n') 
     arg = int(input())
     if arg == 1: 
        if infskok == False:
             gaBytes = index.read_bytes(ga.lpBaseOfDll, ga.SizeOfImage)
             infskok = True
             skok = ga.lpBaseOfDll + re.search(rb'\x80\xBB.....\x74\x09\x80\xBB.....', gaBytes).start() 
             index.write_bytes(skok, b"\x90\x90\x90\x90\x90\x90\x90\x90\x90", 9)
             os.system('cls')
             print('Pomyslnie wlaczono modul: 1) Nieskonczony skok')
             continue
        else: 
             ErrorReturn()
             continue
     elif arg == 2: 
         if nokb == False:
             gaBytes = index.read_bytes(ga.lpBaseOfDll, ga.SizeOfImage)
             nokb = True
             kb = ga.lpBaseOfDll + re.search(rb'\x48\x89\x5C\x24.\x48\x89\x74\x24.\x57\x48\x83\xEC.\x80\x3D.....\x48\x8B\xF2\x48\x8B\xD9\x75.\x48\x8D\x0D....\xE8....\x48\x8D\x0D....\xE8....\xC6\x05.....\x48\x8B\x7B', gaBytes).start()
             index.write_bytes(kb, b"\xC3\x90\x90\x90\x90", 5)
             os.system('cls')
             print('Pomyslnie wlaczono modul: 2) 0% Knockbacku') 
             continue
         else: 
             ErrorReturn()
             continue
     elif arg == 3: 
         if fastpunch == False:
             gaBytes = index.read_bytes(ga.lpBaseOfDll, ga.SizeOfImage)
             fastpunch = True
             punch = ga.lpBaseOfDll + re.search(rb'\xC6\x43\x24\x00\x48\x8B\xCB', gaBytes).start() + 3 
             index.write_uchar(punch, 1)
             os.system('cls')
             print('Pomyslnie wlaczono modul: 3) Szybkie uderzanie') 
             continue
         else:
             ErrorReturn()
             continue