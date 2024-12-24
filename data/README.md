Set up local postgres

1. Create a file called .pgpass (use template file)
2. Write a connection string in the following format
    - hostname:port:database:username:password
    - Example: localhost:5432:postgres:postgres:password
3. Set your PGPASSFILE environment variable to be here with the following command
    > export PGPASSFILE=$(pwd)/.pgpass
4. Grant permissions to the file (read and write only for current user)
    > sudo chmod 600 .pgpass
5. Log in without password
    > psql -U postgres -w
6. To quit out of postgres, use following command
    > \quit