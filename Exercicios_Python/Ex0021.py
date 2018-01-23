'''
Tocar um arquivo mp3
Nome: Edson Ricardo Czarneski
Disciplina: Programação II - Python
Data: 23/01/2018

'''

from pygame import mixer
mixer.init()
mixer.music.load('MeuArquivo.mp3')
mixer.music.play()
input()



