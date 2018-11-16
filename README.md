# SendIT-Api
[![Build Status](https://travis-ci.org/CryceTruly/SendIT-Api.svg?branch=mainapp)](https://travis-ci.org/CryceTruly/SendIT-Api) [![Coverage Status](https://coveralls.io/repos/github/CryceTruly/SendIT-Api/badge.svg?branch=mainapp)](https://coveralls.io/github/CryceTruly/SendIT-Api?branch=mainapp)
[![Maintainability](https://api.codeclimate.com/v1/badges/f84f7744ada502f4799c/maintainability)](https://codeclimate.com/github/CryceTruly/SendIT-Api/maintainability) [![Codacy Badge](https://api.codacy.com/project/badge/Grade/ac47983c1bc5459e9774c9af64f7974d)](https://www.codacy.com/app/CryceTruly/SendIT-Api?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=CryceTruly/SendIT-Api&amp;utm_campaign=Badge_Grade)

A rest api for the SendIT application

## Installation

Create a virtual environment for the project.

```
virtualenv "name of the virtual environment"
```
Then Activate the venv using:
```
source "name of the virtual environment/bin/activate
```

* Navigate to the application directory:

```
cd SendRestApi
```

* Create a virtual environment to install the
application in. You could install virtualenv and virtualenvwrapper.
Within your virtual environment, install the application package dependencies with:

```
pip install -r requirements.txt
```

* Run the application with:

```
python run.py
```
* for tests run in terminal using:

```
py.test
```

#### URL endpoints

| URL Endpoint | HTTP Methods | Summary |
| -------- | ------------- | --------- |
| `api/v1/parcels` | `POST`  | Creates a new Parcel delivery order|
example
```
{
	"user_id":1,
	"pickup_address":"Kigali Rwanda",
	"destination_address":"Jinja Uganda",
	"comment_description":"comment_description",
	"status":"started",
	"current_location":"Kigali Rwanda",
	"sender_email":"crycetruly@gmail.com",
	"recipient_phone":"07666777665",
	"recipient_email":"getaplott@gmail.com",
	"recipient_name":"name",
	"weight":20
}
```
| `api/v1/parcels/<int:id>` | `GET` | Retrieves a specific parcel delivery order given its identifier|
example
```
GET http://127.0.0.1:5000/api/v1/parcels/1
```
| `api/v1/parcels/<int:id>/cancel` | `PUT` | Cancels a specific parcel delivery order given its identifier |
```
http://127.0.0.1:5000/api/v1/parcels/1/cancel
```
| `api/v1/users` | `GET` | Retrieve all users |
```
GET http://127.0.0.1:5000/api/v1/users

```

| `api/v1/users` | `POST` |  Creates a new User |
Example body
```
Example body
{
"fullname":"fullname",
"username":"username",
"phone_number":"0756778877",
"email":"email@email.com",
"password":"password"
	
}
```
| `api/v1/users/<int:id>/parcels` | `GET` | Retrieves parcel orders for a specific user |
```
eg
PUT http://127.0.0.1:5000/api/v1/users/1/parcels
```

## Deployement
[Heroku Deployement](https://senditappp.herokuapp.com)
