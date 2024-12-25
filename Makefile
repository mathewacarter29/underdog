.PHONY: login
login:
	psql -d postgres -U mathewcarter -w

.PHONY: db-start
db-start:
	brew services start postgresql@17

.PHONY: db-stop
db-stop:
	brew services stop postgresql@17

.PHONY: db-populate
db-populate:
	cd data;\
	source env/bin/activate;\
	$$(pwd)/env/bin/python populate.py;\
	deactivate;

.PHONY: db-wipe
db-wipe:
	cd data;\
	source env/bin/activate;\
	$$(pwd)/env/bin/python wipe.py;\
	deactivate;

