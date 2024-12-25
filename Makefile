.PHONY: db-login
db-login:
	psql -d postgres -U mathewcarter -w

.PHONY: db-start
db-start:
	brew services start postgresql@17

.PHONY: db-stop
db-stop:
	brew services stop postgresql@17

.PHONY: db-populate
db-populate:
	source env/bin/activate;\
	cd data;\
	../env/bin/python populate.py;\
	deactivate;

.PHONY: db-wipe
db-wipe:
	source env/bin/activate;\
	cd data;\
	../env/bin/python wipe.py;\
	deactivate;

.PHONY: api-start
api-start:
	fastapi dev api/main.py
