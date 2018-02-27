import csv

def find_homefield(margins, iters, initial):
	alpha = 0
	for counter in range(1, iters):
		i = counter % len(margins)
		alpha = 2/counter
		marg = margins[i]
		diff = marg - initial
		diff = alpha*diff
		initial = initial + diff
	return initial
	
def margins(game_data, h, a):
	margin_list = []
	for game in game_data:
		margin = int(game[h]) - int(game[a])
		margin_list.append(margin)
	return margin_list

def nfl():
	def get_margins(games):
		margin_list = []
		for game in games:
			margin = 0
			if game[1] == '@':
				margin = int(game[4]) - int(game[3])
			else:
				margin = int(game[3]) - int(game[4])
			margin_list.append(margin)
		return margin_list
	
	def get_data(filename):
		nflgames = []
		with open(filename, newline='') as csvfile:
			reader = csv.reader(csvfile, delimiter=',')
			for row in reader:
				if row[0] == '' or row[0] == 'Winner/tie':
					continue
				nflgames.append(row)
		return nflgames
	
	print('NFL 2006 homefield advantage:', find_homefield(get_margins(get_data('nfl2006.csv')), 10000, 4))
	print('NFL 2016 homefield advantage:', find_homefield(get_margins(get_data('nfl2016.csv')), 10000, 4))

def nhl():
	
	def get_data(filename):
		nhlgames = []
		with open(filename, newline='') as csvfile:
			reader = csv.reader(csvfile, delimiter=',')
			for row in reader:
				modrow = row[0].split(',')
				if modrow[0] == 'Date':
					continue
				nhlgames.append(modrow)
		return nhlgames
	
	print('NHL 2006 homefield advantage:', find_homefield(margins(get_data('nhl2006.csv'), 4, 2), 10000, 4))
	print('NHL 2016 homefield advantage:', find_homefield(margins(get_data('nhl2016.csv'), 4, 2), 10000, 4))

def nba():
	
	def get_data(filename):
		nbagames = []
		with open(filename, newline='') as csvfile:
			reader = csv.reader(csvfile, delimiter=',')
			for row in reader:
				if len(row) == 0:
					continue
				nbagames.append(row)
		return nbagames
	
	print('NBA 2006 homefield advantage:', find_homefield(margins(get_data('nba2006.csv'), 1, 0), 10000, 4))
	print('NBA 2016 homefield advantage:', find_homefield(margins(get_data('nba2016.csv'), 1, 0), 10000, 4))

def mlb():
	def get_data(filename):
		mlbgames = []
		with open(filename, newline='') as csvfile:
			reader = csv.reader(csvfile, delimiter=',')
			for row in reader:
				if len(row) == 0:
					continue
				mlbgames.append(row)
		for game in mlbgames:
			game[1] = game[1].split('(')[1].split(')')[0]
			game[0] = game[0].split('(')[1].split(')')[0]
		return mlbgames

	print('MLB 2006 homefield advantage:', find_homefield(margins(get_data('mlb2006.csv'), 1, 0), 10000, 4))
	print('MLB 2016 homefield advantage:', find_homefield(margins(get_data('mlb2016.csv'), 1, 0), 10000, 4))
nfl()
nhl()
nba()
mlb()