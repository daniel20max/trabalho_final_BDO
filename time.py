from datetime import datetime, date, timedelta, time

atual = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
hoje = datetime.now()
dias = timedelta(days=2, hours=0, minutes=0, seconds=0)
amanha = hoje + dias
print(hoje + dias)
print(amanha)
print(atual)
print(dias)