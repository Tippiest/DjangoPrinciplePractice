# Django-Practice

Steps:

- Install python and add pip to system path

- Creating virtual environment within terminal directory : 
  - > pip install virtualenv
  - > virtualenv -p python3 venv
  - > venv\Scripts\activate

- Create Django Project and Applications:
  - > pip install django
  - > django-admin startproject modelproject
  - > cd ./modelproject
  - > django-admin startapp modelapp

- Enter models.py file within modelapp folder and create models called Customer and Vehicle.

- Enter admin.py within the same folder to register models from model.py.
- Ensure that modelapp is included in project settings.py

Populate Models with Data using terminal python shell:
  - Add Customers:
    - >>> from modelapp.models import Customer, Vehicle
    - >>> c=Customer(name="Henry")
    - >>> c.save()
    - >>> Customer.objects.create(name="Hameed")
  - Add Vehicles:
    - >>> v=Vehicle(name="Honda", customer=c)
    - >>> v.save()
    - >>> v=Vehicle(name="Toyota", customer=c)
    - >>> v.save()
    
    - Practice using create method simulating INSERT SQL operations
    
    - >>> Vehicle.objects.create(name="Ford", customer=c)
    - >>> Vehicle.object.create(name="Nissan", customer=c)

 Fetch Data:
  - Use all() method from the Manager:
    - >>> lst=Customer.objects.all()
    - >>> [c.name for c in lst]
      -This iterates over all objects and displays them.
  - Display all objects and associations
    - >>> lst=Vehicle.object.all()
    - >>> for v in lst:
    - ...     print(v.name, " : ", v.customer.name)
    - ...
    - This will Display a message like this:
        Honda :  Hameed 
        Toyota :  Hameed 
        Ford :  Henry 
        Nissan :  Henry 
        
- Updating and removing a model object:
  - >>>  c = Customer.objects.get(name="Henry")
  - >>> c.name = "Helen"
  - >>> c.save()
  - >>> c=Customer.objects.get(pk=2)
  - >>> c.delete()
