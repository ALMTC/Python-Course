# Criando datas com módulo datetime
# datetime(ano, mês, dia)
# datetime(ano, mês, dia, horas, minutos, segundos)
# datetime.strptime('DATA', 'FORMATO')
# datetime.now()
# https://pt.wikipedia.org/wiki/Era_Unix
# datetime.fromtimestamp(Unix Timestamp)
# https://docs.python.org/3/library/datetime.html
# Para timezones
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
# Instalando o pytz
# pip install pytz types-pytz

from datetime import datetime, timedelta

from pytz import timezone

data_timezone = datetime.now(timezone("America/Fortaleza"))
data = datetime.now()
data_ontem = data.replace(day=data.day - 1)
data_especifica = datetime(2025, 5, 23)

comparacao = data < data_especifica

print(data - data_especifica)

print(comparacao)
print(f"data: {data}")

print(
    f"Data atual: {data.date()}\nData ontem: {data_ontem.date()}\nData um dia: {data_especifica.date()}"
)


delta = timedelta(days=5, hours=6)

data_modificada = data + delta
print(data_modificada)


###################################################################################################################

print("#" * 20)
fmt = "%d/%m/%Y"
# data = datetime(2026, 6, 29, 9, 38, 40)
data = datetime.strptime("2026-06-29 09:38:40", "%Y-%m-%d %H:%M:%S")
print(data)
print(data.strftime(fmt), data.time())

print("#" * 20)
print(data.strftime("%d/%m/%Y %H:%M"))
print(data.strftime("%d/%m/%Y %H:%M:%S"))
print(data.strftime("%Y"), data.year)
print(data.strftime("%d"), data.day)
print(data.strftime("%m"), data.month)
print(data.strftime("%H"), data.hour)
print(data.strftime("%M"), data.minute)
print(data.strftime("%S"), data.second)
