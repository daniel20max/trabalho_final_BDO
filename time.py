from datetime import datetime, date, timedelta, time
from main import insert

def insert_time_locacao():
    atual = datetime.today()
    entregar = atual + timedelta(days=2)
    return insert(f"insert into loca (data_inicio, data_fim) values ({atual}, {entregar})")



#insert_time_locacao()





#atual = datetime.today().strftime('%d-%m-%Y %H:%M:%S')
#hoje = datetime.now()
#dias = timedelta(days=2)
#amanha = hoje + dias
#print(hoje + dias)
#print(amanha)
#atual = datetime.h()
#print(atual)
#print(dias)

