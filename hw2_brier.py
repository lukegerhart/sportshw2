import csv

games = []

#Read custom csv file.
#hw2dataformatted.csv is a subset of nfl_elo.csv
#There are 2 columns: HomeWinProb, HomeTeamWon, where HomeTeamWon is 1 or 0
with open('hw2dataformatted.csv', newline='') as csvfile:
	reader = csv.reader(csvfile, delimiter=',')
	for row in reader:
		games.append(row)
num_games = len(games)
home_wins = 0

#count home wins
for game in games:
	home_wins = home_wins + int(game[1])

#base rate is how often home team wins
base_rate = home_wins/num_games

#calculate uncertainty
uncertainty = base_rate * (1 - base_rate)

#calculate resolution

#first bin the data
bins = [[] for y in range(10)]
for game in games:
	bin_num = int(float(game[0]) // 0.1)
	#bin[1] contains games where home team had 10's% chance of winning, bin[2] 20's% and so on
	bins[bin_num].append(game)

#iterate through bins and calculate 
resolution = 0
bin_rates = [0 for z in range(10)]
for i in range(10):
	bin = bins[i]
	if len(bin) == 0:
		continue
	one = 0
	for game in bin:
		if game[1] == '1':
			one = one + 1
	rate = one/len(bin)
	bin_rates[i] = rate
	difference = rate - base_rate
	value = len(bin) * (difference ** 2)
	resolution = resolution + value

#calculate reliability 
reliability = 0
for i in range(10):
	bin = bins[i]
	if len(bin) == 0:
		continue
	prob = 0
	for game in bin:
		prob = prob + float(game[0])
	average_prob = prob/len(bin)
	difference = average_prob - bin_rates[i]
	reliability = reliability + (len(bin) * (difference ** 2))
print("Uncertainty:", uncertainty)
print("Resolution:", resolution)
print("Reliability:", reliability)
print("Brier Score:", reliability - resolution + uncertainty)
