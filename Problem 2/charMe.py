def charMe(aSet):
	aSet = aSet.replace(' ', '')
	aT = re.compile('[+-]?[.0-9]*\D*\^*[.0-9]*')
	aSets = aT.match(aSet)
	print(aSets.group(0))
	a = aSets.group(0)
	aL = len(a)
	for n in range(0,aL):
		print(a[n])
