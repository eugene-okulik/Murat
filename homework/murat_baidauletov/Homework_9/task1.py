import datetime

test_time = "Jan 15, 2023 - 12:05:33"
python_time = datetime.datetime.strptime(test_time, "%b %d, %Y - %H:%M:%S")
print(python_time)
print(python_time.strftime("%B"))
print(f'{python_time.strftime("%d.%m.%Y, %H:%M")}')
