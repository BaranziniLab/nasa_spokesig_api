An API for use by NASA-Genelab to fetch Gene SPOKEsigs

# Application Setup

## Requirements

* Python 3.6 (API has been tested on Python 3.6.9)
* MySQL

## Clone this repo and install dependencies to a virtualenv

Clone this repo

Create a virtualenv and activate it 

Then install dependencies to that virtualenv as follows:

```
pip install -r requirements.txt
```

## Setup the configuration file

Create a config file or use the template given in the repo named "nasa_spokesig_api.conf.example". Remove the ".example" suffix from the filename.

Give MySQL credentials such as username and password. Provide database name as **gene_spokesig** in the *mysql* section of the config file.

Provide data paths to the *data* section of the config file.

Note: *column_mapping_file* in the *data* section of the config file should be named as a **.tsv** file. Its okay even if you don't have this file. This will be generated later. Now, just give a name (along with the path) that you want this file to be called.

Then:

* Save it as ".nasa_spokesig_api.conf" to the home folder (~)

OR

* Save it as "nasa_spokesig_api.conf" to "/etc" folder

## Create column map file

To create this file (which is given in the *data* section of the config file as *column_mapping_file*), run the following:

```
python -m nasa_api.bin.create_column_mappings
```

## Create database and tables

Next, to create database and tables in MySQL, run the following:

```
python -m nasa_api.bin.create_db_and_tables
```

## Populate the database

To populate database in MySQL, run the following:

```
python -m nasa_api.bin.populate_db
```

Note: This could take some time to complete (in the order of minutes)

## Run unit tests

```
python -m unittest discover tests.unit
```

## Start the app

```
python -m nasa_api.app
```

This runs the Flask development server, which is really only meant for testing.


If you want to run it in production, it's recommended to use WSGI, pointed at
`nasa_api.app:app`.

## Test the API using Swagger UI

Open the browser.

Type `http://localhost:5555/nasa_api/v1/swagger`

This will show a Swagger UI for the API as per OpenAPI Specification. 

You can see details regarging this API and also documentation of endpoints in this Swagger UI. 

You can also try making API calls from the Swagger UI.






