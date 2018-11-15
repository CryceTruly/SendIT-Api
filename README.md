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
| `api/v1/parcels/<int:id>` | `GET` | Retrieves a specific parcel delivery order given its identifier|
| `api/v1/parcels/<int:id>/cancel` | `PUT` | Cancels a specific parcel delivery order given its identifier |
| `api/v1/users` | `GET` | Retrieve all users |
| `api/v1/users` | `POST` |  Creates a new User |
| `api/v1/users/<int:id>/parcels` | `GET` | Retrieves parcel orders for a specific user |

## Deployement
[Heroku Deployement](https://senditappp.herokuapp.com)
