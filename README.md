# HBNB

This is the console /command interpreter for the Holberton Airbnb clone project. The console can be used to store objects in and retrieve objects from a JSON.

## Supported classes

* BaseModel
* User
* State
* City
* Amenity
* Place
* Review

### Commands

* create - create an object
* show - show an object (based on id)
* destroy - destroy an object
* all - show all objects, of one type or all types
* quit/EOF - quit the console
* help - see descriptions of commands

To start, navigate to the project folder and enter `./console.py` in the shell.

#### Create

`create <class name>`
Example:
`create BaseModel`

#### Show

`show <class name> <object id>`
Example:
`show User my_id`

#### Destroy

`destroy <class name> <object id>`
Example:
`destroy Place my_place_id`

#### All

`all` or `all <class name>`
Example:
`all` or `all State`

#### Quit

`quit` or `EOF`

#### Help

`help` or `help <command>`
Example:
`help` or `help quit`

Additionally, the console supports `<class name>.<command>(<parameters>)` syntax.
Example:
`City.show(my_city_id)`

## Authors

* **Nicolas Forero Puello** - [NickForero11](https://github.com/NickForero11)

* **Pablo Andres Sanchez Monsalve** - [Jackeado](https://github.com/Jackeado)
