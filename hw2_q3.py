import os, csv, time, sys, numpy
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.externals import joblib
base_dir = os.getcwd()

def read_files(dir):
	os.chdir(base_dir)
	os.chdir(os.getcwd()+dir)
	for game in os.listdir():
		game_data = []
		if '.csv' in game:
			file = open(game, newline='')
			reader = csv.reader(file, delimiter=',')
			for row in reader:
				if row[0] == 'game_id':
					continue
				#all_data.append(row[13:17])
				game_data.append(row[13:17])
			margin = int(game_data[-1][2]) - int(game_data[-1][1])
			for g in game_data:
				away = int(g[1])
				home = int(g[2])
				period = int(g[0])
				timeremaining = time.strptime(g[3], '%H:%M:%S')
				#print(timeremaining)
				new_g = []
				new_g.append(away)
				new_g.append(home)
				if margin > 0:
					new_g.append(1)
				else:
					new_g.append(0)
				secondsremaining = ((timeremaining.tm_min + ((4 - period) * 12)) * 60) + timeremaining.tm_sec
				new_g.append(secondsremaining)
				print(*new_g, sep=',')

def get_data():
	print('Reading q3data.csv for game data...')
	all_data = []
	file = open('q3data.csv')
	reader = csv.reader(file, delimiter=',')
	for row in reader:
		all_data.append(row)
	return numpy.array(all_data)
def train(data):
	print('Training model...')
	x_train, x_test, y_train, y_test = train_test_split(data[:,[0,1,3]], data[:,2], test_size=0.25, random_state=0)
	logisticRegr = LogisticRegression()
	x_train = x_train.astype(float)
	y_train = y_train.astype(float)
	logisticRegr.fit(x_train, y_train)
	x_test = x_test.astype(float)
	predictions = logisticRegr.predict(x_test)
	y_test = y_test.astype(float)
	score = logisticRegr.score(x_test, y_test)
	print('Coefficients:', logisticRegr.coef_)
	print('Intercept:', logisticRegr.intercept_)
	print('Accuracy: ',score)
	return logisticRegr
if len(sys.argv) == 1:
	print('Usage: ')
	print('python hw2_q3.py -c to generate condensed dataset')
	print('python hw2_q3.py -t to train the model')
	print('python hw2_q3.py -p to make a prediction')
elif sys.argv[1] == '-t':
	#train
	data = get_data()
	model = train(data)
	joblib.dump(model, 'model.pkl')
	#print(data[:,0][0:10])
elif sys.argv[1] == '-p':
	#predict
	away_score = input('Away Team current score: ')
	home_score = input('Home Team current score: ')
	time_remaining = input('Time Remaining(in seconds [0,2880]: ')
	test_data = []
	test_data.append(away_score)
	test_data.append(home_score)
	test_data.append(time_remaining)
	#test_data = test_data.astype(float)
	td = numpy.array(test_data).astype(float)
	td = td.reshape(1, -1)
	#numpy.reshape(td, (1, -1))
	#data = get_data()
	#logisticRegr = train(data)
	logisticRegr = joblib.load('model.pkl')
	proba = logisticRegr.predict_proba(td)
	print("Probability of Home Team winning: ", proba[0][1])
	#log_proba = logisticRegr.predict_log_proba(td)
	#print(log_proba)
elif sys.argv[1] == '-c':
	#go to 2014 season directory
	read_files('\\2014-15\\2014-15')
	read_files('\\15-16\\15-16')