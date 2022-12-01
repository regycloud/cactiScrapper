import PySimpleGUI as sg
import random
from cactiScrapper import cactiScrapper, data

sg.ChangeLookAndFeel('DarkBlue')
layout= [
    # [sg.Checkbox('Uppercase Letters?', key='Upper', default=True)],
    # [sg.Checkbox('Symbols?', key='Symbols', default=True)],
    # [sg.Text('User name :')],
    # [sg.InputText(key = 'uname')],
    # [sg.Text('Password :')],
    # [sg.InputText(key = 'pw')],
    [sg.Text('Selection :')],
    [sg.InputText(key = 'selection')],
    [sg.Button('Submit'), sg.Button('Cancel')]

]
mainscreen = sg.Window('Report Generator', layout, resizable=True, element_justification='j').Finalize()
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowercase_letters = uppercase_letters.lower()
digits = '1234567890'
symbols = '@#=+_-'
upper, lower, nums, syms = True, True, True, True
all = ''
while True:
    event, value = mainscreen.Read()
    if event in (None, 'Cancel'):
        break
    if event == 'Submit':
        # sg.popup('Not a registerd user, please recheck your credential') if value['uname'] == '0' else 'bbye'
        # cactiScrapper(value['selection'], 2022, 11, 1, 2, 0)
        print(data[value['selection']])
        
