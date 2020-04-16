import csv
def mapper(flangeClass, NPS):
	if (flangeClass == 2500):
		if (NPS > 12):
			raise Exception('Size {} does not exist for class #{} flanges.'.format(str(NPS), str(flangeClass)))
	if (flangeClass == 900) or (flangeClass == 1500) or (flangeClass == 2500):
		if (NPS == 3.5) or (NPS == 22):
			raise Exception('Size {} does not exist for class #{} flanges.'.format(str(NPS), str(flangeClass)))
	filename = "C:\\Users\\jcoll\\abaqus_plugins\\FlangeMainGUI\\Flanges_B16.5_" + str(flangeClass) + '.csv'
	with open(filename, 'rb') as file:
		lines = csv.reader(file, delimiter=',')
		for line in lines:
			if(line[0] == str(NPS)):
				ans = line[2:12]

	ans = map(float, ans)
	ans[4] = int(ans[4])
	return ans