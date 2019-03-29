Import config

from flask import Flask, request
from cassandra.cluster import Cluster

cluster = Cluster(['cassandra'])
session = cluster.connect()
app = Flask(__name__)

apikey=config.apikey

@app.route('/')
def hello():
	url = 'http://api.apixu.com/v1/current.json?key={}&q=London'.format(apikey)
	resp = requests.get(url)
	content = resp.json()
	temp = (content['current']['temp_c'])
	print(temp)
	return('<h1>Car Detail App</h1><br><br> The temperature today is {}</h1>'.format(temp))


@app.route('/car/<car>')
def profile(car):
	rows = session.execute( """Select * From car.stats where car = '{}' ALLOW FILTERING""".format(car))
	for row in rows:
		name = row.car
		c= row.cylinders
		w=row.weight
		return('<h1>{} has {} cylinders and weighs {} kg!</h1>'.format(name,c,w))

	return('<h1>That car does not exist</h1>')

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8080)
