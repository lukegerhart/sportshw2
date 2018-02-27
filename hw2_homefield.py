import csv
games = []

def find_homefield(margins, iters, initial):
	alpha = 0
	for counter in range(1, 10000):
		i = counter % len(margin_list)
		alpha = 2/counter
		marg = margin_list[i]
		diff = marg - initial
		diff = alpha*diff
		initial = initial + diff
	return initial

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

marginl = [x for x in margins.values()]
margin_list = [item for sublist in marginl for item in sublist]

print('NFL 2016 homefield advantage:', find_homefield(margin_list, 10000, 4))

games = []
with open('nhl2016.csv', newline='') as csvfile:
	reader = csv.reader(csvfile, delimiter=',')
	for row in reader:
		modrow = row[0].split(',')
		if modrow[0] == 'Date':
			continue
		games.append(modrow)

margin_list = []
for game in games:
	margin = int(game[4]) - int(game[2])
	margin_list.append(margin)
print('NHL 2016 homefield advantage:', find_homefield(margin_list, 10000, 4))

games = []
with open('nba2016.csv', newline='') as csvfile:
	reader = csv.reader(csvfile, delimiter=',')
	for row in reader:
		if len(row) == 0:
			continue
		modrow = row[0].split(',')
		if modrow[0] == 'Date':
			continue
		games.append(modrow)

margin_list = []
for game in games:
	margin = int(game[5]) - int(game[3])
	margin_list.append(margin)
print('NBA 2016 homefield advantage:', find_homefield(margin_list, 10000, 4))

games = []
with open('mlb2016.csv', newline='') as csvfile:
	reader = csv.reader(csvfile, delimiter=',')
	for row in reader:
		games.append(row)

margin_list = []
for game in games:
	margin = int(game[1].split('(')[1].split(')')[0]) - int(game[0].split('(')[1].split(')')[0])
	margin_list.append(margin)

print('MLB 2016 homefield advantage:', find_homefield(margin_list, 10000, 4))