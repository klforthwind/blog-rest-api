#Helpful PostgreSQL Information
##05/28/2019

- Log in to PostgreSQL (psql always logs in to the database associated with the username, unless you add the -d option specifying database):
```sh
psql -U postgres -h localhost
```
- Create the database to store data:
```sh
create database mydb;
```
- Show database list:
```sh
\l
```
- Create a user:
```sh
create user username with password 'password';
```
- Connect to the new database:
```sh
\c mydb;
```
- Creating a schema inside of the database connected to:
```sh
create schema schemaName;
```
- Create a table inside of a specific schema:
```sh
create table schemaName.tableName(nameOne typeOne, nameTwo typeTwo);
```
- Table Column Types
    - Boolean
        - yes, y, t, 1 are converted to true
        - no, n, f, 0 are are converted to false 
    - Character
        - CHAR(n): strings of size n, padding strings to make it size n
        - VARCHAR(n): strings of up to size n
        - TEXT: strings of unlimited length
    - Numeric
        - Integer
            - SMALLINT: 2 byte signed integers (-32,768 to 32,767)
            - INT: 4 byte signed integers
            - SERIAL: a number that is automatically generated and increases every entry
        - Floating-point Number
            - float(n): a floating-point number with precision n (max 8 bytes)
            - real / float8: a double-precision (8 bytes) floating-point number
            - numeric / numeric(p, s): a real number with p digits with s numbers after decimal point
    - Temporal
        - DATE: date values
        - TIME: time of day values
        - TIMESTAMP: both date and time values
        - TIMESTAMPTZ: timezone-dependent timestamp values
        - INTERVAL: periods of time
    - Arrays
        - Can store arrays of variables (TEXT[])
    - JSON
        - JSON: plain JSON data
        - JSONB: JSON data in binary format
    - UUID
        - UUID: Universal Unique Identifiers
    - Other Special Types
        - box: a rectangular box
        - line: a set of points
        - point: a geometric pair of numbers
        - lseg: a line segment
        - polygon: a closed geometric
        - inet: an IP4 address
        - macaddr: a MAC address
- Select all from specific table:
```sh
select * from schemaName.tableName;
```
- Show database information:
```sh
\d schemaName.tableName
```
- Insert a row into the table:
```sh
insert into schemaName.tableName('ColumnOneValue','ColumnTwoValue');
```
- Delete a row from the table:
```sh
delete from schemaName.tableName where condition;
```
- Show table:
```sh
select * from schemaName.tableName;
```
- Exit database:
```sh
\q
```
- Exports database:
```sh
pg_dump -U username -h localhost databaseName >> sqlfile.sql 
```

:)


#####Sources:
######[PostgreSQL Tutorial](http://www.postgresqltutorial.com/postgresql-python/ "Link to PostgreSQL Python")