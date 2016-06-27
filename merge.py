#python-merge strings

a = ''
b = ''
c = ''

for i in range(max(len(a),len(b))):
	if not a[i]:
		c = c + b[i]
	elif not b[i]:
		c = c + a[i]
	else:
		c = c + a[i] + b[i]

print c