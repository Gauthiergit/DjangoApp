# Run server
all:
	@python3 merchex/manage.py runserver

# Create tables in database
migration:
	@python3 merchex/manage.py makemigrations

# Execute migration of news models in tables of database
migrate:
	@python3 merchex/manage.py migrate

# Open shell python in django to add some data manualy
shell:
	@python3 merchex/manage.py shell


# create an app into our django project
# 		python3 manage.py startapp <app name>

# Create super user for our web site
# 		@python3 manage.py createsuperuser
# 		user = gauthdev
# 		pw = djangopw

# show migartion
# 		python3 manage.py showmigrations

# returning to previous migration
# 		python3 manage.py migrate <app_name> <previous_migration>

# delete migration
# 		rm <app_name>/migrations/<migration>.py

# merge migrations in project with other dev
# 		python3 manage.py makemigrations --merge