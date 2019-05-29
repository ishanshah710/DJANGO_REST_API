# DJANGO_REST_API

Technologies used :- REST framework ,API , DJANGO , PYTHON , SQLITE3

It is a Django REST API (uses Django REST framework)  which handles all  CRUDL on one endpoint i.e we can do whole CRUD on one page. 

project :- restapi
application :- status

It uses rest_api.py(in scripts folder) to test diffrent methods for CRUD(these testing methods are in rest_api.py). 


The speciality of this is that it uses only one endpoint(localhost:8000/api/status/) which handles whole CRUD for us.

We don't need to use other diffrent pages for update and delete                                                                           ( e.g. localhost:8000/api/status/update/<int:pk>/ & localhost:8000/api/status/delete/<int:pk>/)  but we can do whole CRUD on single endpoint as mentioned above. 

I mainly handled views in status/api/views.py  

I also used one file shell_examples.py(in restapi/status/api ) which I used to test diffrent ways of SERIALIZING data(i.e for converting data to JSON, validating it and making it more consistent) for single instance and also for whole queryset.

So I used both files rest_api.py and shell_examples.py for testing purpose which I handled in command line only.

I used two ways to handle CRUD. 
1. By Generic views of rest_frameworf
2. By Mixins of rest_framework 

I inherited both in corresponding API classes to use them.
