# Template Documentation

# Introduction

This repository contains the content for the Vuetify-Flask-GoogleLogin Template project.
- Flask as backend
- Vue + Vuetify + Vuex as frontend
- Google Login as oauth authentication
- Celery as background worker
- Alembic as database migration tool

# Development Setup

## Backend
- Install python version 3.x
- Install project dependencies
    `cd backend`
    `pip install -r requirements.txt`
- Run the development server
    `python app.py`
- The web application listens on port 8888
- Backend configuration is in *Config/__init__.py*
- Whenever any model is changed use documentation about data migration to migrate db to accomodate new changes.

## Frontend
- Install npm from [node](nodejs.org)
- Install frontend dependencies
    `cd frontend`
    `npm install`
- Run the development server
    `npm run serve`
- Navigate to the UI using the [browser](http://localhost:8080)
- Frontend configuration is in *src/config.js*


## Database Migration

- Database migrations are handled implicitly using Flask-Migrate.
- Before first run, create your initial migrations using `flask db migrate -m "Initial db.`
- To apply the changes or create db before first run `flask db upgrade`
- For subsequent Model change, generate the migration script using `flask db migrate -m "Added columns for job creation."`
- Flask-Migrate cannot detect all changes and requires manual review of scripts generated but works for the common cases out of the box.
- The migration scripts are in the folder `Models/Migrations`


## Authentication Setup

- Setup your own Google auth project as described [here](https://www.youtube.com/watch?v=V4KqpIX6pdI)
- In the `Config/__init__.py` replace the Google secret with one for your project.
- in `frontend/src/config.js` replace client_id with your client id.

## Background Workers

- Add your background worker files in `backend/Workers`
- in `WorkerRef.py` add a reference to this new worker py file in conf imports next to `StmWorker.py`
- Change the number of Worker processes launched from `Workers/__init.py`
- Celery uses file system broker. Change the configuration to use redis - rabbitmq

## Deployment

- Frontend to be built using `npm run build` which copies the built files to `backend/Ui`
- Backend run in production mode using `FLASK_ENV=production python app.py`
- Deploy as a systemd service by modifying the `backend/Deploy/template.service` file


## Documents

- The .md document files are included in the Help section of the application.
- They contain an outer skeleton and can be expanded as required.

## Release Management

- git tags can be used to manage releases but this is not fully functional and requires tweaks.
- Create a release using `git tag v00.00.02` followed by `git push origin --tags`
- The available releases are visible on the Administration -> "Server Health" page.
