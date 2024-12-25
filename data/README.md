Set up local postgres

1. Create a file called .pgpass (use template file .pgpass.template)
2. Write a connection string in the following format
    - hostname:port:database:username:password
    - Example: localhost:5432:postgres:postgres:password
3. Set your PGPASSFILE environment variable to be here with the following command
    > export PGPASSFILE=$(pwd)/.pgpass
4. Grant permissions to the file (read and write only for current user)
    > sudo chmod 600 .pgpass
5. Start postgres server
    > brew services start postgresql@17
5. Log in without password
    > psql -U mathewcarter -w
    - Postgres creates a user with your computer username - run following command to get username
        > whoami
    - If you get "psql: error: connection to server on socket "/tmp/.s.PGSQL.5432" failed: FATAL:  database "mathewcarter" does not exist" error, then you need to create a database for yourself
        > createdb
6. To quit out of postgres, use following command
    > \quit
7. To end postgres service, use following command
    > brew services stop postgresql@17

Set default schema in psql terminal
> ALTER USER mathewcarter SET search_path='underdog';

Kill postgres process
> sudo pkill -u postgres