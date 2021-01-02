# Poke-Django-Api-Test
A Pokemon team management API to test Django Rest Framework

## Available End-points:

```json
    {
    "path": "trainer/create/",
    "Method": "POST",
    "body": {"name":"string", "last_name":"string"},
    "code": "201"
    }

    {
    "path": "trainer/delete/<int:pk>/",
    "Method": "DELETE",
    "code": "204"
    }

    {
    "path": "trainer/get/<int:pk>/",
    "Method": "GET",
    "code": "200"
    }

    {
    "path": "trainer/update/<int:pk>/",
    "Method": "PUT",
    "body": {"name":"string", "last_name":"string"},
    "code": "200"
    }

    {
    "path": "teams/create/",
    "Method": "POST",
    "body": {"trainer":"int"},
    "code": "201"
    }

    {
    "path": "teams/get/<int:pk>",
    "Method": "GET",
    "code": "200"
    }

    {
    "path": "teams/delete/<int:pk>",
    "Method": "DELETE",
    "code": "204"
    }

    {
    "path": "teams/add/",
    "Method": "POST",
    "Description": "Adds a pokemon to the designated slot. Can replace an already existing pokemon",
    "body": {
        "id": "<int>|<string>",
        "slot": "<int>|<string>",
        "pokemon_name": "moltres",
        },
    "code": "201"
    }
    
    {
    "path": "teams/delete/<int:id>/<int:slot>/",
    "Method": "POST",
    "Description": "Removes a pokemon from the specified team and specified slot",
    "code": "204"
    }

    {
    "path": "teams/getall/<int:id>/",
    "Method": "GET",
    "Description": "Gets all teams belonging to a trainer id",
    "code": "200"
    }

```

## Setting Up:
- Install MySQL Server, Django and Django Rest Framework.
- Install Python dependencies for MySQL: `pip install mysql-connector-python` and `pip install mysqlclient`.
- Install Python dependency for pokeApi python wrapper: `pip install pokebase`.
- Setup DB credentials in `Settings.py` in DB section.
- Run migrations: `py manage.py makemigrations` (make sure the DB exists in MySQL server: `pokemon_trainers`)

## Running tests:
To run the test cases: `py manage.py test <module>.tests`.
Or just: `py manage.py test` to run all tests.

## Exercise Details:

Technical exercise

### Requirements:

Create a simple and easy to use REST API to manage Pokemon Trainer's Teams. The user should be able to register as a trainer and create pokemon teams. Each team is limited to a maximum of 6 pokemon.
The API should provide the following operations
Create, Read, Update, Delete (CRUD) trainers
CRUD pokemon teams
CRUD  single pokemons on a team.
 
### Technical Requirements:

Python 3.6+ with Django 2.2+ and Django Rest framework.
You can use any database wish (MySQL/PostgreSQL are suggested)
You must use the following REST API to get Pokemon information: https://pokeapi.co/ 
You are free to decide which information to include in the API responses, but have in mind that you want a simple but useful API.
Include a README file describing how to build and run your application
 
### Additional notes:

Although none of this are requirements, consider having them in mind when coding the solution:
Use of best practices/conventions (PEP8, linters, etc.)
- Clean code and refactoring
- Unit tests (just if you have enough time)
- Insightful comments in your code
- Use swagger to document the API (just if you have enough time)
 
### Final instructions:

Any requirement not specified above is left to your consideration. Remember. Keep it simple.
Include in your readme usage example of your API.
Use a git repo to version your application. 
Post your project on github or gitlab and share the link to it.
