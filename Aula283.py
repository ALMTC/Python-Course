import calendar
import locale

print(calendar.month(2026, 6))

locale.setlocale(locale.LC_ALL, "")

print(calendar.month(2026, 6))
