import string

digit = int(input("Enter digit from 0 to 8640000: "))
if digit < 0 or digit > 8640000:
    print('wrong digit')
day = 24 * 60 * 60
hour = 60 * 60
minute = 60

days, digit = divmod(digit, day)
hours, digit = divmod(digit, hour)
minutes, digit = divmod(digit, minute)

if days % 10 == 1 and days % 100 != 11:
    day_word = "день"
elif 2 <= days % 10 <= 4 and not (12 <= days % 100 <= 14):
    day_word = "дні"
else:
    day_word = "днів"

time_result = (
    f"{days} {day_word}, " +
    f"{str(hours).zfill(2)}:" +
    f"{str(minutes).zfill(2)}:" +
    f"{str(digit).zfill(2)}"
)
print('time_result', time_result)