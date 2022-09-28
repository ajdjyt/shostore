A basic interactive shell python store management system
Price system WIP

SETUP:

Copy .env.example to .env and replace:
<sqluser> with the username for sql
<sqlpass> with the password for your sql user 
<sqlhost> the hostname/FQDN for your sql server
<adminpass> password to access the admin user
*NOTE* Password is currently stored in cleartext in .env

USAGE:
Start mysql server localy or spin up a docker container 
setup mysql user (tables and database are checked and created at every run)
if you want to alocate a database manually and manage permissions the only database used by this program is "electonics"
Put main.py,func.py and your .env file in the same folder and run main.py via
python3 main.py


