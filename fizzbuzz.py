for i in range(1, 101):		#for values 1 through 100
	if i%3 == 0 and i%5 == 0:		#if value is divisible by both 3 and 5
		print "fizzbuzz"
	elif i%3 == 0:		#if value is divisible by 3
		print "fizz"
	elif i%5 == 0:		#if value is divisible by 5
		print "buzz"
	else:
		print i
