from main import execute
from datetime import datetime, timedelta
import random



def nova_locacao(locacoes_id ,filmes_id, usuarios_id, tipo_pagamento, status_pagamento, valor_pagamento):
    data_inicio = datetime.now()
    tempo_de_locacao = timedelta(days=2)
    data_fim =  data_inicio + tempo_de_locacao
    x = "123456789abcdefghijlmnopqrstuvxz"
    chave_aleatoria = random.choice(x) + random.choice(x) + random.choice(x) + random.choice(x) + random.choice(x) + random.choice(x)
    execute(f"""insert into locacoes (id, data_inicio, data_fim, filmes_id, usuarios_id)
    values (%s, '{data_inicio}','{data_fim}', %s, %s)""",(locacoes_id, filmes_id, usuarios_id))
    execute(f"""insert into pagamento (tipo, status, codigo_pagamento, valor, data, locacoes_id)
    values (%s, %s, '{chave_aleatoria}', %s, '{data_inicio}', %s)""",(tipo_pagamento, status_pagamento, valor_pagamento, locacoes_id))

#nova_locacao(10,1,1,"paypal", "aprovado", 9.50)
#nova_locacao(10,1,1,"paypal", "aprovado", 9.50)
# ID da Locacao, Filme_id, Usuario_id,
# Tipo de pagamento(1,2,3) ou por escrito(dredito, crebito, paypel)
#status de pagamento(1,,2,3) ou por escrito(aprovado, em analise, reprovado)
