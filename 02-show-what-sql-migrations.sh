
#There’s a command that will run the migrations for you and 
# manage your database schema automatically - that’s called migrate, 
# and we’ll come to it in a moment - but first, let’s see what
#  SQL that migration would run. The sqlmigrate command takes
# migration names and returns their SQL:
python manage.py sqlmigrate polls 0001