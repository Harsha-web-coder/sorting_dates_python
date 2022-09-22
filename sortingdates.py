from datetime import datetime
	
def printDates(dates):
	for i in range(len(dates)):
		print(dates[i])
	
	
if __name__ == "__main__":

	dates = ["23 Jun 2018", "2 Dec 2017", "11 Jun 2018","01 Jan 2019", "10 Jul 2016", "01 Jan 2007"]
	
	dates.sort(key = lambda date: datetime.strptime(date, '%d %b %Y'))
	
	printDates(dates)