# Car-Detail-App

A car detail app built to better understand the functionality of flask, Cassandra and Kubernetes.

## Features

This is a simple use case to better understand Flask, Cassandra and Kubernetes. It uses the internal IP to get information about a specific car type. 

The purpose of this collection is to help new Cassandra users better understand Cassandra and to present illustrative use cases.

It searches for the details of the car passed in the app route and fetches details such as the weight of the car and the number of cylinders it has.

It also makes use of the "https://www.apixu.com/" weather api to display current weather on the homepage.

## Libraries and Requirements

External Libraries used are: 
- 'cassandra' (Driver to connect to the cassandra db) 
- 'flask' (Setting up a web-interface)

The first thing to do is install all the prerequisite packages. They can be found in requirements.txt. Here's a simple way to do it from the command line using pip.

``` $ pip install -r requirements.txt ```
		
## Docker image is available and you can run using the following command on gcloud:
``` docker 
kubectl run car-project --image=gcr.io/${PROJECT_ID}/car-10 --port 8080
```

