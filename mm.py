import urllib3
import requests
import json
import datetime
import sqlite3
import plotly.plotly as py
import plotly.graph_objs as go
import pandas as pd
import musixmatch
from musixmatch import Musixmatch



######################AUTHENTICATION USING API KEY################################################################################
# Authentication with API key.
musixmatch = Musixmatch('api_key')


######################CATCHING THE DATA############################################################################################
#I collected the top 50 searched lyrics of a song for 8 countries. 
#caching us top charts
CACHE_FNAME1 = "us_cache.json"
try:
    cache_file = open(CACHE_FNAME1, 'r') # Try to read the data from the file
    cache_contents = cache_file.read()  # If it's there, get it into a string
    CACHE_DICTION1 = json.loads(cache_contents) # And then load it into a dictionary
    cache_file.close() # Close the file, we're good, we got the data in a dictionary.
except:
    CACHE_DICTION1 = {}


# #checking the cache of a particular user and returns that data or retrieves that cache'd data.
def get_us():
	# if statement is checking if you already looked it up, if you did, then use the thing you cache'd
	if 'message' in CACHE_DICTION1:
		print('using cache')
		mm_results = CACHE_DICTION1['message']
	else:
		print('getting data from internet')
		# getting top 25 looked up lyrcis of tracks based on country. page_size is the limit
		mm_results = musixmatch.chart_tracks_get(1, 100, f_has_lyrics = 0, country = 'United States')
		CACHE_DICTION1['message'] = mm_results['message']
		cache_file = open(CACHE_FNAME1, 'w')
		#json.dumps prints out the string of dictionary in a json file in one line
		cache_file.write(json.dumps(CACHE_DICTION1))
		cache_file.close()

	return CACHE_DICTION1['message']



#caching Russia's top charts
CACHE_FNAME2 = "rus_cache.json"
try:
    cache_file = open(CACHE_FNAME2, 'r') # Try to read the data from the file
    cache_contents = cache_file.read()  # If it's there, get it into a string
    CACHE_DICTION2 = json.loads(cache_contents) # And then load it into a dictionary
    cache_file.close() # Close the file, we're good, we got the data in a dictionary.
except:
    CACHE_DICTION2 = {}

def get_rus():
	# if statement is checking if you already looked it up, if you did, then use the thing you cache'd
	if 'message' in CACHE_DICTION2:
		print('using cache')
		mm_results = CACHE_DICTION2['message']
	else:
		print('getting data from internet')
		# getting top 25 looked up lyrcis of tracks based on country. page_size is the limit
		mm_results = musixmatch.chart_tracks_get(1, 100, f_has_lyrics = 0, country = 'ru')
		CACHE_DICTION2['message'] = mm_results['message']
		cache_file = open(CACHE_FNAME2, 'w')
		#json.dumps prints out the string of dictionary in a json file in one line
		cache_file.write(json.dumps(CACHE_DICTION2))
		cache_file.close()

	return CACHE_DICTION2['message']



#caching Mexico's top charts
CACHE_FNAME3 = "mx_cache.json"
try:
    cache_file = open(CACHE_FNAME3, 'r') # Try to read the data from the file
    cache_contents = cache_file.read()  # If it's there, get it into a string
    CACHE_DICTION3 = json.loads(cache_contents) # And then load it into a dictionary
    cache_file.close() # Close the file, we're good, we got the data in a dictionary.
except:
    CACHE_DICTION3 = {}

def get_mx():
	# if statement is checking if you already looked it up, if you did, then use the thing you cache'd
	if 'message' in CACHE_DICTION3:
		print('using cache')
		mm_results = CACHE_DICTION3['message']
	else:
		print('getting data from internet')
		# getting top 25 looked up lyrcis of tracks based on country. page_size is the limit
		mm_results = musixmatch.chart_tracks_get(1, 100, f_has_lyrics = 0, country = 'mx')
		CACHE_DICTION3['message'] = mm_results['message']
		cache_file = open(CACHE_FNAME3, 'w')
		#json.dumps prints out the string of dictionary in a json file in one line
		cache_file.write(json.dumps(CACHE_DICTION3))
		cache_file.close()

	return CACHE_DICTION3['message']



#caching South Africa's top charts
CACHE_FNAME4 = "za_cache.json"
try:
    cache_file = open(CACHE_FNAME4, 'r') # Try to read the data from the file
    cache_contents = cache_file.read()  # If it's there, get it into a string
    CACHE_DICTION4 = json.loads(cache_contents) # And then load it into a dictionary
    cache_file.close() # Close the file, we're good, we got the data in a dictionary.
except:
    CACHE_DICTION4 = {}

def get_za():
	# if statement is checking if you already looked it up, if you did, then use the thing you cache'd
	if 'message' in CACHE_DICTION4:
		print('using cache')
		mm_results = CACHE_DICTION4['message']
	else:
		print('getting data from internet')
		# getting top 25 looked up lyrcis of tracks based on country. page_size is the limit
		mm_results = musixmatch.chart_tracks_get(1, 100, f_has_lyrics = 0, country = 'za')
		CACHE_DICTION4['message'] = mm_results['message']
		cache_file = open(CACHE_FNAME4, 'w')
		#json.dumps prints out the string of dictionary in a json file in one line
		cache_file.write(json.dumps(CACHE_DICTION4))
		cache_file.close()

	return CACHE_DICTION4['message']



#caching France's top charts
CACHE_FNAME5 = "fr_cache.json"
try:
    cache_file = open(CACHE_FNAME5, 'r') # Try to read the data from the file
    cache_contents = cache_file.read()  # If it's there, get it into a string
    CACHE_DICTION5 = json.loads(cache_contents) # And then load it into a dictionary
    cache_file.close() # Close the file, we're good, we got the data in a dictionary.
except:
    CACHE_DICTION5 = {}

def get_fr():
	# if statement is checking if you already looked it up, if you did, then use the thing you cache'd
	if 'message' in CACHE_DICTION5:
		print('using cache')
		mm_results = CACHE_DICTION5['message']
	else:
		print('getting data from internet')
		# getting top 25 looked up lyrcis of tracks based on country. page_size is the limit
		mm_results = musixmatch.chart_tracks_get(1, 100, f_has_lyrics = 0, country = 'fr')
		CACHE_DICTION5['message'] = mm_results['message']
		cache_file = open(CACHE_FNAME5, 'w')
		#json.dumps prints out the string of dictionary in a json file in one line
		cache_file.write(json.dumps(CACHE_DICTION5))
		cache_file.close()

	return CACHE_DICTION5['message']



#caching United Kingdom's top charts
CACHE_FNAME6 = "uk_cache.json"
try:
    cache_file = open(CACHE_FNAME6, 'r') # Try to read the data from the file
    cache_contents = cache_file.read()  # If it's there, get it into a string
    CACHE_DICTION6 = json.loads(cache_contents) # And then load it into a dictionary
    cache_file.close() # Close the file, we're good, we got the data in a dictionary.
except:
    CACHE_DICTION6 = {}

def get_uk():
	# if statement is checking if you already looked it up, if you did, then use the thing you cache'd
	if 'message' in CACHE_DICTION6:
		print('using cache')
		mm_results = CACHE_DICTION6['message']
	else:
		print('getting data from internet')
		# getting top 25 looked up lyrcis of tracks based on country. page_size is the limit
		mm_results = musixmatch.chart_tracks_get(1, 100, f_has_lyrics = 0, country = 'uk')
		CACHE_DICTION6['message'] = mm_results['message']
		cache_file = open(CACHE_FNAME6, 'w')
		#json.dumps prints out the string of dictionary in a json file in one line
		cache_file.write(json.dumps(CACHE_DICTION6))
		cache_file.close()

	return CACHE_DICTION6['message']



#caching Australia's top charts
CACHE_FNAME7 = "au_cache.json"
try:
    cache_file = open(CACHE_FNAME7, 'r') # Try to read the data from the file
    cache_contents = cache_file.read()  # If it's there, get it into a string
    CACHE_DICTION7 = json.loads(cache_contents) # And then load it into a dictionary
    cache_file.close() # Close the file, we're good, we got the data in a dictionary.
except:
    CACHE_DICTION7 = {}

def get_au():
	# if statement is checking if you already looked it up, if you did, then use the thing you cache'd
	if 'message' in CACHE_DICTION7:
		print('using cache')
		mm_results = CACHE_DICTION7['message']
	else:
		print('getting data from internet')
		# getting top 25 looked up lyrcis of tracks based on country. page_size is the limit
		mm_results = musixmatch.chart_tracks_get(1, 100, f_has_lyrics = 0, country = 'au')
		CACHE_DICTION7['message'] = mm_results['message']
		cache_file = open(CACHE_FNAME7, 'w')
		#json.dumps prints out the string of dictionary in a json file in one line
		cache_file.write(json.dumps(CACHE_DICTION7))
		cache_file.close()

	return CACHE_DICTION7['message']



#caching Canada's top charts
CACHE_FNAME8 = "ca_cache.json"
try:
    cache_file = open(CACHE_FNAME8, 'r') # Try to read the data from the file
    cache_contents = cache_file.read()  # If it's there, get it into a string
    CACHE_DICTION8 = json.loads(cache_contents) # And then load it into a dictionary
    cache_file.close() # Close the file, we're good, we got the data in a dictionary.
except:
    CACHE_DICTION8 = {}

def get_ca():
	# if statement is checking if you already looked it up, if you did, then use the thing you cache'd
	if 'message' in CACHE_DICTION8:
		print('using cache')
		mm_results = CACHE_DICTION8['message']
	else:
		print('getting data from internet')
		# getting top 25 looked up lyrcis of tracks based on country. page_size is the limit.
		mm_results = musixmatch.chart_tracks_get(1, 100, f_has_lyrics = 0, country = 'ca')
		CACHE_DICTION8['message'] = mm_results['message']
		cache_file = open(CACHE_FNAME8, 'w')
		#json.dumps prints out the string of dictionary in a json file in one line
		cache_file.write(json.dumps(CACHE_DICTION8))
		cache_file.close()
	return CACHE_DICTION8['message']


######################HELPER FUNCTIONS############################################################################################
#Based on the country, this function returns the country name along with how many clean and explicit song lyrics that country searches
def track_info(d, country):
	cln_count = 0
	ex_count = 0
	#iterating through the body key of th dicitonary then over the track_list to go into each track. Each track is an element of the 
	#list
	for elem in d['body']['track_list']:
		#ex will be the value of whether the track is clean or explicit. 0 is clean. 1 is explicit.
		ex = elem['track']['explicit']
		#if song is clean
		if ex == 0:
			cln_count = cln_count + 1
		else:
			ex_count = ex_count + 1

	tupl = country, cln_count, ex_count
	return tupl

######################CREATING AND LOADING INTO DATABASE###########################################################################


conn = sqlite3.connect('explicit.sqlite', timeout = 10)
cur = conn.cursor()
# creating users table
cur.execute('DROP TABLE IF EXISTS Explicit')
cur.execute("CREATE TABLE EXPLICIT (country TEXT PRIMARY KEY, clean NUMBER, explicit NUMBER)")

lst = [] 
#Getting info for Australia
#get cache data
au_posts = get_au()
#call the track_info function to return tuple of the country, clean and explicit count
tup = track_info(au_posts, 'Australia')
#insert the tuple into the table corresponding to the column
cur.execute('INSERT INTO Explicit (country, clean, explicit) VALUES (?, ?, ?)',tup)


#Getting info for Canada
ca_posts = get_ca()
tup = track_info(ca_posts, 'Canada')
cur.execute('INSERT INTO Explicit (country, clean, explicit) VALUES (?, ?, ?)',tup)


#Getting info for France
fr_posts = get_fr()
tup = track_info(fr_posts, 'France')
cur.execute('INSERT INTO Explicit (country, clean, explicit) VALUES (?, ?, ?)',tup)


#Getting info for Mexico
mx_posts = get_mx()
tup = track_info(mx_posts, 'Mexico')
cur.execute('INSERT INTO Explicit (country, clean, explicit) VALUES (?, ?, ?)',tup)


#Getting info for Russia
rus_posts = get_rus()
tup = track_info(rus_posts, 'Russia')
cur.execute('INSERT INTO Explicit (country, clean, explicit) VALUES (?, ?, ?)',tup)


#Getting info for South Africa
za_posts = get_za()
tup = track_info(za_posts, 'South Africa')
cur.execute('INSERT INTO Explicit (country, clean, explicit) VALUES (?, ?, ?)',tup)


#Getting info for United Kingdom
uk_posts = get_uk()
tup = track_info(uk_posts, 'United Kingdom')
cur.execute('INSERT INTO Explicit (country, clean, explicit) VALUES (?, ?, ?)',tup)


#Getting info for United States
us_posts = get_us()
tup = track_info(us_posts, 'United States')
cur.execute('INSERT INTO Explicit (country, clean, explicit) VALUES (?, ?, ?)',tup)   

#Use the database connection to commit the changes to the database    
conn.commit() 



######################EXTRACT EACH COLUMN AND CREATE LIST TO ADD INTO PLOTLY###########################################################################

#getting data for x-axis
cur.execute('SELECT country FROM Explicit')
lst_x = cur.fetchall()
lst_country = [elem[0] for elem in lst_x]


#getting data for y-axis (clean tracks)
cur.execute('SELECT clean FROM Explicit')
lst_y1 = cur.fetchall()
lst_clean = [elem[0] for elem in lst_y1]


#getting data for y-axis (clean tracks)
cur.execute('SELECT explicit FROM Explicit')
lst_y2 = cur.fetchall()
lst_explicit = [elem[0] for elem in lst_y2]


#loading the data into the plotly bar graph.
trace0 = go.Bar(
    x=lst_country,
    y=lst_clean,
    name='Clean Songs',
    marker=dict(
        color='#00CCCC'
    )
)
trace1 = go.Bar(
    x=lst_country,
    y=lst_explicit,
    name='Explicit Songs',
    marker=dict(
        color= '#1C1B1B',
    )
)

data = [trace0, trace1]

#this labels the graph with title, style of font, x and y axis.
layout = go.Layout(
	title = 'UNDER THE INFLUENCE OF MUSIC?',
    xaxis=dict(
    	title='Countries',
        titlefont=dict(
            family='Courier New, monospace',
            size=18,
            color='#7f7f7f'
        ),
    	tickangle=-45,
    ),
    yaxis=dict(
        title='Number of Songs',
        titlefont=dict(
            family='Courier New, monospace',
            size=18,
            color='#7f7f7f'
        )
    ),
    barmode ='group'
)

fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename='MusixMatchBar')







