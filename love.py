import re
import billboard
import pandas as pd 

chart = billboard.ChartData('hot-100')

lovedic = {}

while chart.previousDate:
	for s in chart:
		if re.search("(?i)lov", s.title) or re.search("(?i)luv", s.title):
			if (s.title, s.artist) not in lovedic:
				lovedic[(s.title, s.artist)] = {}

			if int(chart.date[:4]) not in lovedic[(s.title, s.artist)]:
				lovedic[(s.title, s.artist)][int(chart.date[:4])] = 0

			lovedic[(s.title, s.artist)][int(chart.date[:4])] += 1

	chart = billboard.ChartData('hot-100', chart.previousDate)




lovelist = []
for k, v in lovedic.items():
	title, artist = k
	for year, count in v.items():
		lovelist.append([title, artist, year, count])

lovedf = pd.DataFrame(lovelist, columns = ["Title", "Artist", "Year", "Count"])

lovedf.to_csv("lovedf.csv")
