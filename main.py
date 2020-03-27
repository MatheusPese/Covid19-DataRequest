import  requests

url =('https://pomber.github.io/covid19/timeseries.json')
req = requests.get(url, timeout=3000)
covidCases = req.json()

stringInfo= """
 Country: {country}
 Confirmed Cases: {confirmed}
 Deaths: {dead}
 Recovered: {recovered}
 Death percentage: {percentage}
 Last Update: {date}\n"""

def returnHighestNumberOfCases():
	country = ''
	dead = 0
	confirmed = 0
	date = ''
	recovered = 0
	for i in covidCases:
		dictionary=covidCases[i]
		info=dictionary[-1]
		if confirmed < info['confirmed']:
			dead = info['deaths']
			confirmed = info['confirmed']
			recovered = info['recovered']
			date = info['date']
			country=i
			percentage = str(round((dead/confirmed)*100,2)) + "%"
	return  (country, confirmed, dead, recovered, percentage, date)

def printHighestNumberOfCases(data):
	country, confirmed, dead, recovered, percentage, date = data
	mapping = {"country":country, "confirmed":confirmed, "dead":dead, "recovered":recovered,"percentage":percentage, "date":date}

	print("\nHighest number of cases:".upper(),end='')
	print(str(stringInfo).format(**mapping))

def returnHighestNumberOfDeaths():
	country =''
	dead=0
	confirmed=0
	date = ''
	recovered = 0
	for i in covidCases:
		dictionary=covidCases[i]
		info=dictionary[-1]
		if dead < info['deaths']:
			dead = info['deaths']
			confirmed = info['confirmed']
			recovered = info['recovered']
			date = info['date']
			country=i
			percentage = str(round((dead/confirmed)*100,2)) + "%"
	return (country, confirmed, dead, recovered, percentage, date)

def printHighestNumberOfDeaths(data):
	country, confirmed, dead, recovered, percentage, date = data
	mapping = {"country":country, "confirmed":confirmed, "dead":dead, "recovered":recovered,"percentage":percentage, "date":date}

	print("Highest number of deaths:".upper(),end='')
	print(str(stringInfo).format(**mapping))

def returnDeathPercentage():
	country =''
	dead=0
	confirmed=0
	percentage=0
	date = ''
	highestNumberOfCases = int(returnHighestNumberOfCases()[1])
	highestNumberOfDeaths = int(returnHighestNumberOfDeaths()[2])

	for i in covidCases:
		dictionary=covidCases[i]
		info=dictionary[-1]
		confirmed = info['confirmed']
		dead = info['deaths']
		if confirmed>100 and dead >0:
			if percentage < ((dead+highestNumberOfDeaths)/(confirmed+highestNumberOfCases)):
				percentage = (dead+highestNumberOfDeaths)/(confirmed+highestNumberOfCases)
				date = info['date']
				country=i
	dictionary = covidCases[country]
	info = dictionary[-1]
	confirmed = info['confirmed']
	dead = info['deaths']
	recovered = info['recovered']
	percentage = str(round((dead/confirmed)*100,2)) + "%"

	return (country, confirmed, dead, recovered, percentage, date)


def printDeathPercentage(data):
	country, confirmed, dead, recovered, percentage, date = data
	mapping = {"country":country, "confirmed":confirmed, "dead":dead, "recovered":recovered,"percentage":percentage, "date":date}
	print("Worst case until now:".upper(),end='')
	print(str(stringInfo).format(**mapping))

def returnCountryData(country):
	if country.lower() == 'us':
		country = "US"

	dictionary = covidCases[country]
	info = dictionary[-1]
	date = info['date']
	confirmed = info['confirmed']
	dead = info['deaths']
	recovered = info['recovered']
	percentage = str(round((dead/confirmed)*100,2)) + "%"

	return (country, confirmed, dead, recovered, percentage, date)

def printCountryData(data):
	country, confirmed, dead, recovered, percentage, date = data
	mapping = {"country":country, "confirmed":confirmed, "dead":dead, "recovered":recovered,"percentage":percentage, "date":date}
	print("\n======================",end="")
	print(str(stringInfo).format(**mapping), end="")
	print("======================",end="")
 
printHighestNumberOfCases(returnHighestNumberOfCases())
printHighestNumberOfDeaths(returnHighestNumberOfDeaths())
printDeathPercentage(returnDeathPercentage())
printCountryData(returnCountryData(input("\nEnter a country name to access its information:\nEx: Brazil, US, Africa\n>").capitalize()))


