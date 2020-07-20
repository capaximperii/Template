# MSSQL Basic Setup
- Create a Database

    `create database StmMatch;`

- Contained databases allow user creation with password.

    `EXEC sp_configure 'CONTAINED DATABASE AUTHENTICATION', 1
    GO
    RECONFIGURE
    GO`


- Make sure our database has containment set to allow user creation.

    `USE [master]
    GO
    ALTER DATABASE [StmMatch] SET CONTAINMENT = PARTIAL
    GO`

- Create a user

    `USE [StmMatch]
    GO
    CREATE USER production
    WITH PASSWORD = 'simulation@123';
    GO`

- Give the user owner permissions on this database.

    `USE [StmMatch]
    GO
    EXEC sp_addrolemember 'db_owner', 'production'
    GO`
