# Runes Tables





# Tests
The tests of the project are separated by the specific code and the specific 
packages of the projects of the code, so, the standard way to name the tests is 

```txt
For general tests, like the website authentication, model or views:

    test_auth.py    -> Testing authentication for the site of the project.
    test_views.py   -> Testing the templates views for the site of the project.
    test_xxx.py     -> Testing any general feature or package of the project.

For specific tests, like checking if the character creator in the api package is working, or if the
api is getting the data from the request, and correctly working if them, we gonna use the terminology:
    
    test_api_init.py                                    -> Testing if the package is initializing correctly.
    test_api_character_creator.py                       -> Testing if the creator module is creating the character.
    test_api_character_document_creator.py              -> Testing if the document with the character data 
                                                           is correctly created.
    test_api_data_serving_for_user_create_character.py  -> Testing if the data from the API is been correctly 
                                                           servindo for the user.

```
### Api Character Creator
For the tests of the 