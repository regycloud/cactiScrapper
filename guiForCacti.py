import PySimpleGUI as sg
from cactiScrapper import cactiScrapper
from data_customer import data_cust, month
from daysNumber import daysNumber
sg.ChangeLookAndFeel('DarkBlue')
layout= [
    # [sg.Checkbox('Uppercase Letters?', key='Upper', default=True)],
    # [sg.Checkbox('Symbols?', key='Symbols', default=True)],
    # [sg.Text('User name :')],
    # [sg.InputText(key = 'uname')],
    # [sg.Text('Password :')],
    # [sg.InputText(key = 'pw')],
    [sg.Text('Month : ')],
    [sg.Combo([
        'January',
        'February',
        'March',
        'April',
        'May',
        'June',
        'July',
        'August',
        'September',
        'October',
        'November',
        'December'], key = 'month', size=(30,6))],
    [sg.Text('CID: ')],
    [sg.Combo([
        'PGAS.VAL.33.01#1',
        'PGAS.VAL.33.01#2',
        'PGAS.VAL.33.04',
        'PGAS.VAL.43.01',
        'PGAS.VAL.33.01#2',
        'PGAS.VAL.43.03',
        'PGAS.VAL.43.04',
        'PGAS.VAL.43.05',
        'NTT',
        'TELIA',
        'PGAS.VAL.33.05',
        'PGAS.VAL.33.06',
        'PCCW',
        'TATA',
        'PGAS.VAL.43.06',], key = 'cid', size=(30,6))],
    [sg.Text('year :')],
    [sg.Combo(['2022', '2021'], key='year', size=(30,6))],
    [sg.Button('Submit'), sg.Button('Cancel')]
]
        # [psg.Combo(['New York','Chicago','Washington', 'Colorado','Ohio','San Jose','Fresno','San Fransisco'],key='dest')],

mainscreen = sg.Window('Report Generator', layout, resizable=True, element_justification='j').Finalize()
while True:
    event, value = mainscreen.Read()
    # verify the input
    if event in (None, 'Cancel'):
        break
    if event == 'Submit':
        # selection
        for n in data_cust:
            if value['cid'] == data_cust[n]['nameService']:
                selection = n
            
        # month
        for n in month:
            if value['month'] == n:
                selectedMonth = month[n]
        cactiScrapper(
            selection,
            int(value['year']),
            selectedMonth,
            1,
            daysNumber(
                int(value['year']), int(selectedMonth)
            ),
            1)
        sg.popup('finished')
        exit()
