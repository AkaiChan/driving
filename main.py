strcountry = input("where are you from?")
intAge = input("how old are you?")
intAge = int(intAge)
if strcountry == "Taiwan":
	if intAge >= 18:
		print("You can go test of driving exam")
	else:
		print("You cannot go test of driving exam")
elif strcountry == "US":
	if intAge >= 16:
		print("You can go test of driving exam")
	else:
		print("You cannot go test of driving exam")