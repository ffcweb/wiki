![alt text](https://upload.wikimedia.org/wikipedia/commons/thumb/3/3c/Flask_logo.svg/200px-Flask_logo.svg.png "Logo Title Text 1")
___

# Flask (web framework)
- Flask is a micro web framework written in Python. It is classified as a microframework because it does not require particular tools or libraries.[2] It has no database abstraction layer, form validation, or any other components where pre-existing third-party libraries provide common functions. However, Flask supports extensions that can add application features as if they were implemented in Flask itself. Extensions exist for object-relational mappers, form validation, upload handling, various open authentication technologies and several common framework related tools.[3]

- Applications that use the Flask framework include Pinterest and LinkedIn.[4][5]

## History
- Flask was created by Armin Ronacher of Pocoo, an international group of Python enthusiasts formed in 2004.[6] According to Ronacher, the idea was originally an April Fool's joke that was popular enough to make into a serious application.[7][8][9] The name is a play on the earlier Bottle framework.[7]

- When Ronacher and Georg Brandl created a bulletin board system written in Python in 2004, the Pocoo projects Werkzeug and Jinja were developed.[10]

- In April 2016, the Pocoo team was disbanded and development of Flask and related libraries passed to the newly formed Pallets project.[11][12] Since 2018, Flask-related data and objects can be rendered with Bootstrap.[13]

- Flask has become popular among Python enthusiasts. As of October 2020, it has the second-most number of stars on GitHub among Python web-development frameworks, only slightly behind Django,[14] and was voted the most popular web framework in the Python Developers Survey for years between and including 2018 and 2022.[15][16][17][18][19]

## Components
- The microframework Flask is part of the Pallets Projects (formerly Pocoo), and based on several others of them, all under a BSD license.

## Werkzeug
- Werkzeug (German for "tool") is a utility library for the Python programming language for Web Server Gateway Interface (WSGI) applications. Werkzeug can instantiate objects for request, response, and utility functions. It can be used as the basis for a custom software framework and supports Python 2.7 and 3.5 and later.[20][21]

## Jinja
- Main article: Jinja (template engine)
- Jinja, also by Ronacher, is a template engine for the Python programming language. Similar to the Django web framework, it handles templates in a sandbox.

## MarkupSafe
- MarkupSafe is a string handling library for the Python programming language. The eponymous MarkupSafe type extends the Python string type and marks its contents as "safe"; combining MarkupSafe with regular strings automatically escapes the unmarked strings, while avoiding double escaping of already marked strings.

## ItsDangerous
- ItsDangerous is a safe data serialization library for the Python programming language. It is used to store the session of a Flask application in a cookie without allowing users to tamper with the session contents.

## Features
- Development server and debugger
- Integrated support for unit testing
- RESTful request dispatching
- Uses Jinja templating
- Support for secure cookies (client side sessions)
- 100% WSGI 1.0 compliant
- Unicode-based
- Complete documentation
- Google App Engine compatibility
- Extensions available to extend functionality
___