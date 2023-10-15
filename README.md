# AirBnB_clone

The HBNB project is an AirBnB cloning that's divided into different smaller projects where in each project we work on a set of technologies to build a specific thing.

<ins>Project Description</ins>
The Airbnb project is divided into 7 smaller projects, which are:

<ins>The console:</ins>

Console (CLI) Description
This console is a single use function (a CLI) from which you can create, modify and delete objects
in your file storage.
This is a sandbox to check what does and doesn't work in the storage.
This project covers file serialization and deserialization in JSON.
Every modification, creation or deletion of any data is saved in the JSON file.
The console is basically the creation of the File Storage Engine.

Installation

Clone the project on your PC
$ https://github.com/johngaitho05/AirBnB_clone.git

Getting Started(how to start)

navigate to the directory

$ cd ./AirBnB_clone

run the python file (CLI)

$ ./console.py

### File Storage Engine
All data operations in the CLI are saves in a JSON file and the saved data will be retrieved when the console is launched again. The FileStorage engine is written in the FileStorage class and has the following functions:

#### all: to return all the data.
####new: to add a newly created data to the existing list of data.
####save: to save the data in JSON file.
####reload: to reload data from the JSON file.
####Data to create, modify and delete in CLI
####All the data classes inherit from a common parent class called BaseClass.

The BaseClass contains the following attributes:

id: unique id for each instance.
created_at: date of creation.
updated_at: date of last instance update.
The BaseClass contains the following methods:
init: used for initialization.
str: to return a string representation of an instance.
save: to save the data.
to_dict: to return a dictionary representation of an instance.

The other classes that inherit from BaseClass are:

User
State
City
Amenity
Place
Review

## Console Functionalities and Usage Examples:

The console has different functionalities (commands), which we'll be covering in the upcoming list:
quit: to quit the console.
help: to display a list of the available commands and to display a specific command's help (usage, documentation..)
The usage of the help command is very important because it shows the user how to each command and functionality in the CLI.
```sh
(hbnb) Usage.all()
[]
(hbnb) User.all()
[[User] (a096d36f-c829-488d-88b4-5a5574b2f729) {'name': 'Lionel Andres messi', 'id': 'a096d36f-c829-488d-88b4-5a5574b2f729', 'updated_at': datetime.datetime(2020, 2, 20, 1, 4, 26, 324496), 'created_at': datetime.datetime(2020, 2, 20, 1, 4, 26, 324423)}]
(hbnb) User.all()
[[User] (a096d36f-c829-488d-88b4-5a5574b2f729) {'name': 'Lionel Andres messi', 'id': 'a096d36f-c829-488d-88b4-5a5574b2f729', 'updated_at': datetime.datetime(2020, 2, 20, 1, 4, 26, 324496), 'created_at': datetime.datetime(2020, 2, 20, 1, 4, 26, 324423)}]
(hbnb) User.count()
1
(hbnb) City.count()
0
(hbnb) Review.all()
[]
(hbnb) Review.count()
0
(hbnb) all User
["[User] (a096d36f-c829-488d-88b4-5a5574b2f729) {'name': 'Lionel Andres messi', 'id': 'a096d36f-c829-488d-88b4-5a5574b2f729', 'updated_at': datetime.datetime(2020, 2, 20, 1, 4, 26, 324496), 'created_at': datetime.datetime(2020, 2, 20, 1, 4, 26, 324423)}"]
(hbnb) User.show("a096d36f-c829-488d-88b4-5a5574b2f729")
[User] (a096d36f-c829-488d-88b4-5a5574b2f729) {'name': 'Lionel Andres messi', 'id': 'a096d36f-c829-488d-88b4-5a5574b2f729', 'updated_at': datetime.datetime(2020, 2, 20, 1, 4, 26, 324496), 'created_at': datetime.datetime(2020, 2, 20, 1, 4, 26, 324423)}
(hbnb) User.destroy("a096d36f-c829-488d-88b4-5a5574b2f729")
(hbnb) all User
[]
[]
(hbnb) all
["[BaseModel] (cf2d280d-b163-408d-a77e-67cf07163139) {'created_at': datetime.datetime(2020, 2, 20, 1, 4, 8, 788705), 'updated_at': datetime.datetime(2020, 2, 20, 1, 4, 8, 788772), 'id': 'cf2d280d-b163-408d-a77e-67cf07163139'}", "[Place] (b41ba918-71e2-4014-8d7f-b85da9d0c026) {'created_at': datetime.datetime(2020, 2, 20, 1, 10, 38, 687662), 'updated_at': datetime.datetime(2020, 2, 20, 1, 10, 38, 687740), 'id': 'b41ba918-71e2-4014-8d7f-b85da9d0c026'}", "[State] (dc67167d-f532-4a0d-b8a9-708df1d5c7ee) {'created_at': datetime.datetime(2020, 2, 20, 1, 8, 8, 269607), 'updated_at': datetime.datetime(2020, 2, 20, 1, 8, 8, 269684), 'id': 'dc67167d-f532-4a0d-b8a9-708df1d5c7ee'}", "[Place] (e9072088-0348-457e-b984-d54f712647a8) {'name': 'Heaven on Earth Baby', 'id': 'e9072088-0348-457e-b984-d54f712647a8', 'updated_at': datetime.datetime(2020, 2, 20, 1, 10, 31, 510283), 'created_at': datetime.datetime(2020, 2, 20, 1, 10, 31, 510220)}", "[State] (7c79fdb3-79b1-4262-a290-366f9f14db53) {'created_at': datetime.datetime(2020, 2, 20, 1, 8, 3, 629532), 'updated_at': datetime.datetime(2020, 2, 20, 1, 8, 3, 629608), 'id': '7c79fdb3-79b1-4262-a290-366f9f14db53'}"]
(hbnb) State.update("7c79fdb3-79b1-4262-a290-366f9f14db53", "name", "Texas")
(hbnb) all State
["[State] (dc67167d-f532-4a0d-b8a9-708df1d5c7ee) {'created_at': datetime.datetime(2020, 2, 20, 1, 8, 8, 269607), 'updated_at': datetime.datetime(2020, 2, 20, 1, 8, 8, 269684), 'id': 'dc67167d-f532-4a0d-b8a9-708df1d5c7ee'}", "[State] (7c79fdb3-79b1-4262-a290-366f9f14db53) {'name': 'Texas', 'id': '7c79fdb3-79b1-4262-a290-366f9f14db53', 'updated_at': datetime.datetime(2020, 2, 20, 1, 8, 3, 629608), 'created_at': datetime.datetime(2020, 2, 20, 1, 8, 3, 629532)}"]
(hbnb) all User
[]
(hbnb) create User
cf1d3cec-4403-4629-ba33-8f91f1063801
(hbnb) all User
["[User] (cf1d3cec-4403-4629-ba33-8f91f1063801) {'id': 'cf1d3cec-4403-4629-ba33-8f91f1063801', 'updated_at': datetime.datetime(2020, 2, 20, 1, 30, 12, 377358), 'created_at': datetime.datetime(2020, 2, 20, 1, 30, 12, 377283)}"]
(hbnb) User.update("cf1d3cec-4403-4629-ba33-8f91f1063801", {'first_name': "John", "age": 89})
(hbnb) all User
["[User] (cf1d3cec-4403-4629-ba33-8f91f1063801) {'age': 89, 'id': 'cf1d3cec-4403-4629-ba33-8f91f1063801', 'updated_at': datetime.datetime(2020, 2, 20, 1, 30, 12, 377358), 'created_at': datetime.datetime(2020, 2, 20, 1, 30, 12, 377283), 'first_name': 'John'}"]
```
