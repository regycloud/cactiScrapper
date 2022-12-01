import PySimpleGUI as sg
from cactiScrapper import cactiScrapper
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
while True:
    event, value = mainscreen.Read()
    if event in (None, 'Cancel'):
        break
    if event == 'Submit':
        cactiScrapper(
                int(value['selection'])
                , 2022, 11, 1, 2, 0)
        sg.popup('finished')
        exit()
