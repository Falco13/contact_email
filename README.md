# Small Django app with contact form and email sending

- The contact form consists of - Name, Email and Message text.
- When you click on the Send button, it saves the message to the database and also sends this message to the email (using Celery tasks) of
  the site administrator.

__Validation fields:__

- On the Name field - the Name should not start with a nubmer, also, the Name must not contain numbers or spaces.
- On the Text field - the number of message characters should not exceed 2000.

__API:__

- /api/ - end-point for the same implementation, only in the API.

__Used tools:__    
:heavy_check_mark: Python    
:heavy_check_mark: Django [web framework]    
:heavy_check_mark: Django [REST framework]    
:heavy_check_mark: HTML+CSS+Bootstrap    
:heavy_check_mark: Celery + Redis    
:heavy_check_mark: Docker + Docker-compose    
:heavy_check_mark: SQLite database    
