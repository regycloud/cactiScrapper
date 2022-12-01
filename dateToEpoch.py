import datetime 

def insertDate(year, month, date):
    start = datetime.datetime(year, month, date, 00, 00)
    end = datetime.datetime(year, month, date, 23, 59)
    epochStart = str(start.timestamp()).replace('.','')[:-1]
    epochEnd = str(end.timestamp()).replace('.','')[:-1]
    return [epochStart, epochEnd]
