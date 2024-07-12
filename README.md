# Online Art Gallery and Chat Box

![alt text](imgForReadme/giAll.gif)


## Features

*Deleting products <br>
*Adding products <br>
*Modifying products <br>
*Displaying all products  <br>
*Incrementation and decrementation of number of pruducts <br>
*Incrementation and decrementation of number of pruducts <br>
*Incrementation and decrementation of number of pruducts <br>
*Send a message between rooms <br>


## Usage
### for the (models file) :
To use the this project you hae to import the librery's :

```python
from django.db import models
import datetime
from django.utils import timezone
```
### for the (views file):
```python
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,response,Http404,HttpResponseRedirect
from .form import FormControlProfile
from .models import Profile
from django.db.models import F
```

### for the (urls file):

````python
from django.urls import path
from .import views
````
# To run the project 

Go to the root of the project and execute the following script in a terminal : 
```bash
python manage.py makemigrations app1
python manage.py migrate
python manage.py runserver
```

