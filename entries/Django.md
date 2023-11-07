![alt text](https://upload.wikimedia.org/wikipedia/commons/thumb/7/75/Django_logo.svg/200px-Django_logo.svg.png "Logo Title Text 1")
___
# Django (web framework)

## [Django documentation](https://docs.djangoproject.com/en/4.2/)
- Everything you need to know about Django.

- Django is a web framework written using [Python](/wiki/Python) that allows for the design of web applications that generate [HTML](/wiki/HTML) dynamically.

# History
- Django was created in the autumn of 2003, when the web programmers at the Lawrence Journal-World newspaper, Adrian Holovaty and Simon Willison, began using Python to build applications. Jacob Kaplan-Moss was hired early in Django's development shortly before Simon Willison's internship ended.[15] It was released publicly under a BSD license in July 2005. The framework was named after guitarist Django Reinhardt.[16] Adrian Holovaty is a Romani jazz guitar player and a big fan of Django Reinhardt.[citation needed]

- In June 2008, it was announced that a newly formed Django Software Foundation (DSF) would maintain Django in the future.[17]


# Features
___
### Components

- Screenshot of the Django admin interface for modifying a user account
Despite having its own nomenclature, such as naming the callable objects generating the HTTP responses "views",[6] the core Django framework can be seen as an MVC architecture.[7] It consists of an object-relational mapper (ORM) that mediates between data models (defined as Python classes) and a relational database ("Model"), a system for processing HTTP requests with a web templating system ("View"), and a regular-expression-based URL dispatcher ("Controller").

### Also included in the core framework are:

- a lightweight and standalone web server for development and testing
- a form serialization and validation system that can translate between HTML forms and values suitable for - storage in the database
- a template system that utilizes the concept of inheritance borrowed from object-oriented programming
- a caching framework that can use any of several cache methods
- support for middleware classes that can intervene at various stages of request processing and carry out - custom functions
- an internal dispatcher system that allows components of an application to communicate events to each other via pre-defined signals an internationalization system, including translations of Django's own components into a variety of languages
- a serialization system that can produce and read XML and/or JSON representations of Django model instances
- a system for extending the capabilities of the template engine
- an interface to Python's built-in unit test framework


###  Bundled applications
- The main Django distribution also bundles a number of applications in its "contrib" package, including:
- an extensible authentication system
- the dynamic administrative interface
- tools for generating RSS and Atom syndication feeds
- a "Sites" framework that allows one Django installation to run multiple websites, each with their own content and applications
- tools for generating Google Sitemaps
- built-in mitigation for cross-site request forgery, cross-site scripting, SQL injection, password cracking and - other typical web attacks, most of them turned on by default[18][19]
- a framework for creating GIS applications

____