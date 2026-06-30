# Usando calendar para calendários e datas
# https://docs.python.org/3/library/calendar.html
# calendar é usado para coisas genéricas de calendários e datas.
# Com calendar, você pode saber coisas como:
# - Qual o último dia do mês (ex.: monthrange)
# - Qual o nome e número do dia de determinada data (ex.: weekday)
# - Criar um calendário em si (ex.: monthcalendar)
# - Trabalhar com coisas específicas de calendários (ex.: calendar, month)
# Por padrão dia da semana começa em 0 até 6
# 0 = segunda-feira | 6 = domingo
import calendar

# print(calendar.calendar(2026))
# print(calendar.month(2026, 6))
# print(calendar.monthrange(2026, 6))

n_1_day, ult_day = calendar.monthrange(2026, 6)
week_day_1 = calendar.day_name[n_1_day]
week_day_last = calendar.day_name[calendar.weekday(2026, 6, ult_day)]

print(
    f"O primeiro dia do mês caiu em uma {week_day_1}\nJá o último dia do mês caiu em uma {week_day_last}"
)
