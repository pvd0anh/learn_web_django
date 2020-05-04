### **Install POSTGRESQL**
```sh
#HOW TO INSTALL POSTGRESQL
brew update
brew install postgresql
postgres --

#HOW TO CREATE A PHYSICAL POSTGRESQL DATABASE
initdb /usr/local/var/

#HOW TO START/STOP A POSTGRESQL DATABASE
pg_ctl -D /usr/local/var/postgres start
pg_ctl -D /usr/local/var/postgres stop

#HOW TO CREATE THE ACTUAL POSTGRESQL DATABASE
createdb mydatabasename
dropdb mydatabasename

psql mydatabasename

CREATE DATABASE mydatabasename;
DROP DATABASE mydatabasename;
```

- \list - List all of your actual databases.
- \c mydatabasename - Connect to another database.
- \d - List the relations of your currently connected database.
- \d mytablename - Shows information for a specific table.

Note: pass on windows device: sdt-Doanh 
### **requirements.txt**
- Generate `requirements.txt`
    ```
    pip freeze > requirements.txt
    ```

- Install `requirement.txt`
    ```
    pip install -r requirements.txt
    ```