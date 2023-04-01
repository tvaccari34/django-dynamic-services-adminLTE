# [Django Dynamic Services](https://github.com/app-generator/django-dynamic-services) 

Open-source **Django** project that showcases the **[API Generator](https://appseed.us/developer-tools/django-api-generator/)** and other **[Dynamic Services](https://appseed.us/developer-tools/django-dynamic-datatables/)** - actively supported by [AppSeed](https://appseed.us/).

> 👉 [Django - Build Services without Coding](https://www.youtube.com/watch?v=EtMCK5AmdQI) - `video presentation` (learn how to use this starter)

### Features

- ✅ `Up-to-date Dependencies`
- ✅ Theme: [Django AdminLTE](https://github.com/app-generator/django-admin-adminlte) `v3.2.0`
- ✅ [API Generator](https://github.com/app-generator/django-api-generator) - `Free Python Library` 
- ✅ [Dynamic DataTables](https://github.com/app-generator/django-dynamic-datatb) - `Free Python Library`
- 🚀 `Deployment`: Docker, `CI/CD` flow via `Render`

<br />

![Django Dynamic Services - free developer tools provided by AppSeed.](https://user-images.githubusercontent.com/51070104/219007148-34cefb52-92cc-4ef3-bbf9-f8ee6ae2389b.png)

<br />

## Start the app in Docker

> 👉 **Step 1** - Download the code from the GH repository (using `GIT`)

```bash
$ git clone https://github.com/app-generator/django-dynamic-services.git
$ cd django-dynamic-services
```

> 👉 **Step 2** - Start the APP in `Docker`

```bash
$ docker-compose up --build
```

Visit `http://localhost:5085` in your browser. The app should be up & running.


> 👉 **Step 3** - Create Superuser in `Docker`

```bash
$ # List containes & get the ID
$ docker container ls  
$ # Create the superuser
$ docker exec <CONTAINER_ID> python manage.py createsuperuser 
```

<br />

## Manual Build 

> 👉 Download the code  

```bash
$ git clone https://github.com/app-generator/django-dynamic-services.git
$ cd django-dynamic-services
```

<br />

> 👉 Install modules via `VENV`  

```bash
$ virtualenv env
$ source env/bin/activate
$ pip install -r requirements.txt
```

<br />

> 👉 Set Up Database

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

<br />

> 👉 Generate API

```bash
$ python manage.py generate-api     # requires confirmation
// 
$ python manage.py generate-api -f  # no input (API folder is overwritten)
```

<br />

> 👉 Create the Superuser

```bash
$ python manage.py createsuperuser
```

<br />

> 👉 Start the app

```bash
$ python manage.py runserver
```

At this point, the app runs at `http://127.0.0.1:8000/` and the generated API can be found at: 

- http://localhost:8000/api/product/ - For `products`
- http://localhost:8000/api/sales/ - For `sales` 

The default API nodes can be tested via this [POSTMAN](./media/test.postman_collection) Collection.  

<br />

## How to use the API

- Start the app
- Make sure the endpoints are up & running 
- Authenticate via API and het the access token
  - `http://localhost:8000/login/jwt/` usind existing credentials 
  - Save the token in the requests `HEADER`
- `GET Requests` are public (no token required)
  - GET ALL products: `http://localhost:8000/api/product/`
  - GET product by ID: `http://localhost:8000/api/product/1/`
  - GET ALL Sales: `http://localhost:8000/api/sales/`
- `Create`, `Delete`, `Update` requires a token in the header

For API sample requests, open and edit the [POSTMAN](./media/test.postman_collection) Collection sample.

<br />

## How Update the API

- Define or update your models
- Migrate the database
- Update the configuration `API_GENERATOR` section
- Regenerate the API
  - `python manage.py generate-api`

At this point, you should be able to use the API. For more information regarding the library used to generate the code, access: 

> 👉 [API Generator for Django](https://github.com/app-generator/django-api-generator) - Open-Source Library

<br />

## Codebase structure

The project is coded using a simple and intuitive structure presented below:

```bash
< PROJECT ROOT >
   |
   |-- core/                            
   |    |-- settings.py                  # Project Configuration  
   |    |-- urls.py                      # Project Routing
   |
   |-- home/
   |    |-- views.py                     # APP Views 
   |    |-- urls.py                      # APP Routing
   |    |-- models.py                    # APP Models 
   |    |-- tests.py                     # Tests  
   |    |-- templates/                   # Theme Customisation 
   |         |-- includes                # 
   |              |-- footer.py          # Custom Footer      
   |     
   |-- requirements.txt                  # Project Dependencies
   |
   |-- env.sample                        # ENV Configuration (default values)
   |-- manage.py                         # Start the app - Django default start script
   |
   |-- ************************************************************************
```

<br /> 

---
[Django Dynamic Services](https://github.com/app-generator/django-dynamic-services) - Open-Source **Django** starter provided by **[AppSeed](https://appseed.us/)**
