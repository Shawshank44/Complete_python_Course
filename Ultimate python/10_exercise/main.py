import time as t

Hours = int(t.strftime('%H'))
Hours = 13
if(Hours >= 0) and (Hours <= 12) :
	print("good morning")
elif(Hours > 12) and (Hours <= 14):
	print("good afternoon")
elif(Hours > 14) and (Hours <= 18):
	print("good evening")
elif(Hours > 18) and (Hours <= 23):
	print("good night")
