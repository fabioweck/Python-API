# Python-API
Few lines of code to deliver a fully functional API!

With an ideia to expand my last React/Typescript repository (Bookings), I decided to go for Python
to create a simple API which handles Bookings web-app requests (GET, POST, DELETE).
The project makes use of Flask library and has a CORS handler as well.
There is a "after_request" method with a function to set headers and allow all origins (for test purposes).
Except for the GET method, POST and DELETE methods updates a variable defined on the first run, when the application
reads a JSON file content and delivers it as a list of objects (dictionaries) to the variable.
After that, the JSON file is opened and re-written with or without new items, depending on the method requested.
Finally, the application runs on port 7001 and can be redefined by the user.
