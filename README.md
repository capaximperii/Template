# Template Documentation

# Introduction

This repository contains the content for the Template project.
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
- For a Model change, generate the migration script using `flask db migrate -m "Added columns for job creation."`
- Flask-Migrate cannot detect all changes and requires manual review of scripts generated but works for the common cases out of the box.
- To apply the changes run `flask db upgrade`
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
