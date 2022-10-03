# SQL services

## MySQL

### MariaDB

`mariadb` client

- By default, the local root user can log in to MySQL or MariaDB without password

- `SHOW DATABASES;`
- `USE <DATABASE-NAME>`
- `SHOW tables;`
- `SELECT * FROM <database-table-name>`
- `DESCRIBE <database-table-name>;`

## NoSQL

### MongoDB

`mongo` is deprecated since MongoDB v5.0, use `mongosh` instead

- connect
  - `mongosh $ip:27017`
- list all the databases
  - `show dbs`
  - `use db-name`
- listing out the collections in a database
  - `show collections`
- dumping the content of all the documents within the collection from active database named flag in a format that is easy to read
  - `db.flag.find().pretty()`
