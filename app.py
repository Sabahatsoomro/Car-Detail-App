Import config

from flask import Flask, request
from cassandra.cluster import Cluster

cluster = Cluster(['cassandra'])
session = cluster.connect()
app = Flask(__name__)

apikey=config.apikey #api key 

@app.route('/') #Homepage
def hello():
	url = 'http://api.apixu.com/v1/current.json?key={}&q=London'.format(apikey) 
	resp = requests.get(url)
	content = resp.json()
	temp = (content['current']['temp_c']) #Fetch temperature using the api
	print(temp)
	return('<h1>Car Detail App</h1><br><br> The temperature today is {}</h1>'.format(temp)) #Display current temperature


@app.route('/car/<car>') #Specify the car name in this path
def profile(car):
	rows = session.execute( """Select * From car.stats where car = '{}' ALLOW FILTERING""".format(car)) #Selects the car mentioned in the path
	for row in rows:
		name = row.car
		c= row.cylinders
		w=row.weight
		return('<h1>{} has {} cylinders and weighs {} kg!</h1>'.format(name,c,w)) #Displays details of the mentioned car

	return('<h1>That car does not exist</h1>') #Displays this message if the car does not exist

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8080)
