import csv
games = []
with open('nfl2016.csv', newline='') as csvfile:
	reader = csv.reader(csvfile, delimiter=',')
	for row in reader:
		if row[0] == '' or row[0] == 'Winner/tie':
			continue
		games.append(row)
margins = {}
for game in games:
	margin = 0
	home = ''
	if game[1] == '@':
		home = game[2]
		margin = int(game[4]) - int(game[3])
	else:
		home = game[0]
		margin = int(game[3]) - int(game[4])
	#print(margin)
	if home in margins:
		margins[home].append(margin)
	else:
		margins[home] = []
		margins[home].append(margin)
print(margins)