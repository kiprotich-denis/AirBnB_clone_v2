<center> <h1>AirBnB clone - MySQL</h1> </center>

The Airbnb clone project for which we are creating a copy of the Airbnb. Only some features will be implemented and will be listed below once completed. As part of the project we were asked to fork from a different repo to add code and update the functionality of the existing codebase. To access the part one of theproject please click here.


<h1>Project Description</h1>

The Airbnb clone is one of the main projects at Holberton School, it's a long term project that we need to accomplish by building up trough a series of small modules or pieces. This project is thinking as a whole for a software developer,to learn and become a full-stack developer, gluing alltogether the infrastructure of the Airbnb from back to front, including databases, static and dynamic content, web frameworks, APIs, and web infrastructure. The first step that we need to build is "the console" or the command interpreter, this is meant to be atool to validate or manipulate the storage system, through the console we are gonna be able of:


   *  Create our data model.

   *  Manage (create, update, destroy, etc) objects.

   *  Store and persist objects to a file (JSON file)

---

<center><h3>Directory Files Description</h3> </center>

| Tasks | Files | Description |
| ----- | ----- | ------ |
|  Authors/README File | [AUTHORS](https://github.com/justinmajetich/AirBnB_clone/blob/dev/AUTHORS) | Project authors |
|  Pep8 | N/A | All code is pep8 compliant|
|  Unit Testing | [/tests](https://github.com/justinmajetich/AirBnB_clone/tree/dev/tests) | All class-defining modules are unittested |
|  Make BaseModel | [/models/base_model.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/base_model.py) | Defines a parent class to be inherited by all model classes|
|  Update BaseModel w/ kwargs | [/models/base_model.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/base_model.py) | Add functionality to recreate an instance of a class from a dictionary representation|
|  Create FileStorage class | [/models/engine/file_storage.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/engine/file_storage.py) [/models/_ _init_ _.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/__init__.py) [/models/base_model.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/base_model.py) | Defines a class to manage persistent file storage system|
|  Console 0.0.1 | [console.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/console.py) | Add basic functionality to console program, allowing it to quit, handle empty lines and ^D |
| Console 0.1 | [console.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/console.py) | Update the console with methods allowing the user to create, destroy, show, and update stored data |
|  Create User class | [console.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/console.py) [/models/engine/file_storage.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/engine/file_storage.py) [/models/user.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/user.py) | Dynamically implements a user class |
|  More Classes | [/models/user.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/user.py) [/models/place.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/place.py) [/models/city.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/city.py) [/models/amenity.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/amenity.py) [/models/state.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/state.py) [/models/review.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/review.py) | Dynamically implements more classes |
| Console  | [console.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/console.py) [/models/engine/file_storage.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/engine/file_storage.py)

<center> <h2>Prerequisites</h2> </center>

This program was made and tested using Ubuntu 20.04.3 LTS and Python 3.8.5 So we recommend you to test this command interpreter under this conditions.

<h2>Built With</h2>


  *  Ubuntu 20.04.3 LTS Running on a Virtual Machine "Emacs"
  *  GNU Emacs 24.3.1
  *  Python 3.8.5

<h1>AUTHORS</h1>

<h3>Meaza Lemma</h3>

 * Github @MahiET
 
 * Linkedln - Meaza Lemma

<h3>Denis Kiprotich</h3>

 * Github @ kiprotich-denis

<h2>License</h2>

Opensource project.
    
