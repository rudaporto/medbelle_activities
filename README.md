# Medebelle :: Activities

Activities for a healthy weekend!

## Get started!

First you need to clone this repository from github:

```
git clone git@github.com:rudaporto/medebelle_activities.git
```

## Virtualenv

Next you need a new python3 virtualenv:

```
cd medebelle_activities
make create_venv
source venv/bin/activate
```

## Packages

Install all the necessary python packages:

```
make packages
```

## Migrations

Migrate the database to latest version:

```
make migrate_db
```


## Start

Start the application server:

```
make run_server
```

## Create admin

Create the admin user to manage the application:

```
make create_admin
```

## Open

Finally you can open the [Activities](http://localhost:8089) application.
