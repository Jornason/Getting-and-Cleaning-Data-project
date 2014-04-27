f = open("process.for","r")
sum0 = 0
sum1 = 0 
'''
for content in f.readlines():
	sum0 +=  float(content.split("     ")[-1][:-1][:4])
	sum1 +=  float(content.split("     ")[-1][:-1][-3:])
'''
for content in f.readlines():
	sum0 +=  float(content.split("     ")[-2][:4])
	sum1 +=  float(content.split("     ")[-2][:][-3:])
	
	
print sum0 - sum1
