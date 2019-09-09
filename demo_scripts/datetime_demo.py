import datetime

x = datetime.datetime.now()
print(x)
print("This is sleeping for 2 seconds at {}".format(x))
sleep(2)
print("This has finished sleeping for 2 seconds at {}".format(x))
