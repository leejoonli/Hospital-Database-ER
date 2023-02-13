# Application Description

Hospital database using Django and Python.

# Table Relation Diagram

> https://www.w3resource.com/sql-exercises/

![hospital-database-e-r-diagram](https://user-images.githubusercontent.com/65789692/217952464-64615c7e-1b3f-4623-ba28-bdcac0f34d6c.png)

# Application State

![hospital](https://user-images.githubusercontent.com/65789692/218584082-ccea2e0e-4f7f-4e97-a557-89cb68ef150f.png)

# Technologies Used

- Python
- Django
- PostgreSQL

# API Routes

| Method | Route | Description |
| ------ | ----- | ----------- |
| GET | /procedures/ | Read all procedures |
| GET | /procedures/:id | Read one procedure |
| POST | /procedures/ | Create one procedure |
| PUT | /procedures/:id | Update one procedure |
| DELETE | /procedures/:id | Delete one procedure |
| GET | /medications/ | Read all medications |
| GET | /medications/:id | read one medication |
| POST | /medications/ | Create one medication |
| PUT | /medications/:id | Update one medication |
| DELETE | /medications/:id | Delete one medication |
| GET | /physicians/ | Read all physicians |
| GET | /physicians/:id | Read one physician |
| POST | /physicians/ | Create one physician |
| PUT | /physicians/:id | Update one physician |
| DELETE | /physicians/:id | Delete one physician |
| GET | /nurses/ | Read all nurses |
| GET | /nurses/:id | Read one nurse |
| POST | /nurses/ | Create one nurse |
| PUT | /nurses/:id | Update one nurse |
| DELETE | /nurses/:id | Delete one nurse |
| GET | /patients/ | Read all patients |
| GET | /patients/:id | Read one patient |
| POST | /patients/ | Create one patient |
| PUT | /patients/:id | Update one patient |
| DELETE | /patients/:id | Delete one patient |
| GET | /departments/ | Read all departments |
| GET | /departments/:id | Read one department |
| POST | /departments/ | Create one department |
| PUT | /departments/:id | Update one department |
| DELETE | /departments/:id | Delete one department |
| GET | /blocks/ | Read all blocks |
| GET | /blocks/:id | Read one block |
| POST | /blocks/ | Create one block |
| PUT | /blocks/:id | Update one block |
| DELETE | /blocks/:id | Delete one block |
| GET | /on_calls/ | Read all on calls |
| GET | /on_calls/:id | Read one on call |
| POST | /on_calls/ | Create one on call |
| PUT | /on_calls/:id | Update one on call |
| DELETE | /on_calls/:id | Delete one on call |
| GET | /affiliated_withs/ | Read all affiliated withs |
| GET | /affiliated_withs/:id | Read one affiliated with |
| POST | /affiliated_withs/ | Create one affiliated with |
| PUT | /affiliated_withs/:id | Update one affiliated with |
| DELETE | /affiliated_withs/:id | Delete one affiliated with |
| GET | /trained_ins/ | Read all trained ins |
| GET | /trained_ins/:id | Read one trained in |
| POST | /trained_ins/ | Create one trained in |
| PUT | /trained_ins/:id | Update one trained in |
| DELETE | /trained_ins/:id | Delete one trained in |
| GET | /appointements/ | Read all appointments |
| GET | /appointements/:id | Read one appointment |
| POST | /appointements/ | Create one appointment |
| PUT | /appointements/:id | Update one appointment |
| DELETE | /appointements/:id | Delete one appointment |
| GET | /prescribes/ | Read all prescribes |
| GET | /prescribes/:id | Read one prescribe |
| POST | /prescribes/ | Create one prescribe |
| PUT | /prescribes/:id | Update one prescribe |
| DELETE | /prescribes/:id | Delete one prescribe |
| GET | /rooms/ | Read all rooms |
| GET | /rooms/:id | Read one room |
| POST | /rooms/ | Create one room |
| PUT | /rooms/:id | Update one room |
| DELETE | /rooms/:id | Delete one room |
| GET | /stays/ | Read all stays |
| GET | /stays/:id | Read one stay |
| POST | /stays/ | Create one stay |
| PUT | /stays/:id | Update one stay |
| DELETE | /stays/:id | Delete one stay |
| GET | /undergoes/ | Read all undergoes |
| GET | /undergoes/:id | Read one undergoes |
| POST | /undergoes/ | Create one undergoes |
| PUT | /undergoes/:id | Update one undergoes |
| DELETE | /undergoes/:id | Delete one undergoes |

# Additional Notes

- You may use the admin login to modify entries using the username and password below.

| Username | Password |
| -------- | -------- |
| admin | postgresadmin |

- You may have to install additional packages to run this server such as PostgreSQL, Django, and a virtual environment.  For more information please go here: `https://docs.djangoproject.com/en/4.1/topics/install/`.