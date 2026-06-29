# Exercício solucionado: calculando as datas e parcelas de um empréstimo
# Maria pegou um empréstimo de 1.000.000
# para realizar o pagamento em 5 anos.
# A data em que ela pegou o empréstimo foi
# 20/12/2020 e o vencimento de cada parcela
# é no dia 20 de cada mês.
# - Crie a data do empréstimo
# - Crie a data do final do empréstimo
# - Mostre todas as datas de vencimento e o valor de cada parcela
from datetime import datetime

from dateutil.relativedelta import relativedelta

data_emprestimo = datetime(2020, 12, 20)
tempo = relativedelta(years=5)
final_emprestimo = data_emprestimo + tempo
incremento = relativedelta(months=1)
parcela_atual = data_emprestimo + incremento

n_parcelas = tempo.years * 12 + tempo.months

val_emprestimo = 1000000
val_parcela = 1000000 / n_parcelas

fmt = "%d/%m/%Y"

parcelas = []

for i in range(n_parcelas):
    parcelas.append(parcela_atual)
    parcela_atual = parcela_atual + incremento

for index, parcela in enumerate(parcelas):
    print(
        f"Númeor da parcela: {(index + 1):02d} | Vencimento: {parcela.strftime(fmt)} | Valor a pagar: R${val_parcela:,.2f}"
    )

print()
print(
    f"Você pegou R${val_emprestimo:,.2f} para pagar em {tempo.years} anos ({n_parcelas} meses) em parcelas de R${val_parcela:,.2f}"
)
