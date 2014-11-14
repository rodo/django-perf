tuna
====

Test les différentes méthodes de DELETE de nombreux objects liés

Utilisation
===========

* création des objets SQL avec **syncdb**
* mise en place des triggers avec **trigger.sql**

Results
=======

Book : 110000
Editor : 10053
Author : 20103
raw_delete      18140 time 0.0360250473022 seconds
list_delete     18389 time 4.13527798653 seconds
del_delete      18331 time 3.69426584244 seconds
regular_delete  18421 time 4.57518696785 seconds
Book : 54859
Editor : 10053
Author : 20103
