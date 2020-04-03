# Muddy

> If the weather will be muddy in 3 days, it will return "MUDDY".  
> If the weather will not be muddy in 3 days, it will return "NOT MUDDY".  
> This code was written with the assumption that at any point 3 days from now, there is rain and the temperature at that time is above freezing, it will be muddy.


## Get an API token from [here](https://openweathermap.org)

## Create a Python virtual environment

```
TARDIS:muddy mspear$ virtualenv -p python3 venv
created virtual environment CPython3.7.4.final.0-64 in 271ms
  creator CPython3Posix(dest=/Users/mspear/muddy/venv, clear=False, global=False)
  seeder FromAppData(download=False, pip=latest, setuptools=latest, wheel=latest, via=copy,
 app_data_dir=/Users/mspear/Library/Application Support/virtualenv/seed-app-data/v1.0.1)
  activators BashActivator,CShellActivator,FishActivator,PowerShellActivator,PythonActivator,XonshActivator
```

## Activate it:
```
TARDIS:muddy $ source venv/bin/activate
```

## Install the requirements:
```
(venv) TARDIS:muddy $ pip3 install -r requirements.txt 
Collecting requests
  Using cached requests-2.23.0-py2.py3-none-any.whl (58 kB)
Processing /Users/mspear/Library/Caches/pip/wheels/80/a0/e2/7960cea226c97370c4c256a8f70c64a
392ab25b805a9683a5a/pprint-0.1-py3-none-any.whl
Collecting datetime
  Using cached DateTime-4.3-py2.py3-none-any.whl (60 kB)
Collecting Flask
  Downloading Flask-1.1.2-py2.py3-none-any.whl (94 kB)
     |████████████████████████████████| 94 kB 1.2 MB/s 
Collecting certifi>=2017.4.17
  Using cached certifi-2019.11.28-py2.py3-none-any.whl (156 kB)
Collecting urllib3!=1.25.0,!=1.25.1,<1.26,>=1.21.1
  Using cached urllib3-1.25.8-py2.py3-none-any.whl (125 kB)
Collecting chardet<4,>=3.0.2
  Using cached chardet-3.0.4-py2.py3-none-any.whl (133 kB)
Collecting idna<3,>=2.5
  Using cached idna-2.9-py2.py3-none-any.whl (58 kB)
Collecting zope.interface
  Using cached zope.interface-5.0.2-cp37-cp37m-macosx_10_9_x86_64.whl (184 kB)
Collecting pytz
  Using cached pytz-2019.3-py2.py3-none-any.whl (509 kB)
Collecting Werkzeug>=0.15
  Using cached Werkzeug-1.0.1-py2.py3-none-any.whl (298 kB)
Collecting Jinja2>=2.10.1
  Using cached Jinja2-2.11.1-py2.py3-none-any.whl (126 kB)
Collecting itsdangerous>=0.24
  Using cached itsdangerous-1.1.0-py2.py3-none-any.whl (16 kB)
Collecting click>=5.1
  Using cached click-7.1.1-py2.py3-none-any.whl (82 kB)
Requirement already satisfied: setuptools in ./venv/lib/python3.7/site-packages (from zope.interface->datetime->-r requirements.txt (line 3)) (46.1.3)
Collecting MarkupSafe>=0.23
  Using cached MarkupSafe-1.1.1-cp37-cp37m-macosx_10_6_intel.whl (18 kB)
Installing collected packages: certifi, urllib3, chardet, idna, requests, pprint, zope.interface, pytz, datetime, Werkzeug, MarkupSafe, Jinja2, itsdangerous, click, Flask
Successfully installed Flask-1.1.2 Jinja2-2.11.1 MarkupSafe-1.1.1 Werkzeug-1.0.1 certifi-2019.11.28 chardet-3.0.4 click-7.1.1 datetime-4.3 idna-2.9 itsdangerous-1.1.0 pprint-0.1 pytz-2019.3 requests-2.23.0 urllib3-1.25.8 zope.interface-5.0.2
```

## Add your token as an environment variable:

```
export API_TOKEN=...
```

## I've created a `Makefile` for the following:

## Building the Docker image:
```
(venv) TARDIS:muddy $ make build
docker build -t muddy:latest .
Sending build context to Docker daemon  25.96MB
Step 1/6 : FROM python:3
 ---> d47898c6f4b0
Step 2/6 : WORKDIR /usr/src/app
 ---> Using cache
 ---> a47d03d0d87b
Step 3/6 : COPY . .
 ---> 584d6e7f243e
Step 4/6 : RUN pip3 install --no-cache-dir -r requirements.txt
 ---> Running in 4802850f35f5
Collecting requests
  Downloading requests-2.23.0-py2.py3-none-any.whl (58 kB)
Collecting pprint
  Downloading pprint-0.1.tar.gz (860 bytes)
Collecting datetime
  Downloading DateTime-4.3-py2.py3-none-any.whl (60 kB)
Collecting Flask
  Downloading Flask-1.1.1-py2.py3-none-any.whl (94 kB)
Collecting chardet<4,>=3.0.2
  Downloading chardet-3.0.4-py2.py3-none-any.whl (133 kB)
Collecting idna<3,>=2.5
  Downloading idna-2.9-py2.py3-none-any.whl (58 kB)
Collecting certifi>=2017.4.17
  Downloading certifi-2019.11.28-py2.py3-none-any.whl (156 kB)
Collecting urllib3!=1.25.0,!=1.25.1,<1.26,>=1.21.1
  Downloading urllib3-1.25.8-py2.py3-none-any.whl (125 kB)
Collecting zope.interface
  Downloading zope.interface-5.0.2-cp38-cp38-manylinux2010_x86_64.whl (235 kB)
Collecting pytz
  Downloading pytz-2019.3-py2.py3-none-any.whl (509 kB)
Collecting Werkzeug>=0.15
  Downloading Werkzeug-1.0.1-py2.py3-none-any.whl (298 kB)
Collecting Jinja2>=2.10.1
  Downloading Jinja2-2.11.1-py2.py3-none-any.whl (126 kB)
Collecting click>=5.1
  Downloading click-7.1.1-py2.py3-none-any.whl (82 kB)
Collecting itsdangerous>=0.24
  Downloading itsdangerous-1.1.0-py2.py3-none-any.whl (16 kB)
Requirement already satisfied: setuptools in /usr/local/lib/python3.8/site-packages (from zope.interface->datetime->-r requirements.txt (line 3)) (46.1.3)
Collecting MarkupSafe>=0.23
  Downloading MarkupSafe-1.1.1-cp38-cp38-manylinux1_x86_64.whl (32 kB)
Building wheels for collected packages: pprint
  Building wheel for pprint (setup.py): started
  Building wheel for pprint (setup.py): finished with status 'done'
  Created wheel for pprint: filename=pprint-0.1-py3-none-any.whl size=1250 sha256=00e5de7bf32f4feb315f42a369c26e37da7af12a95d38b96287067ed4daeace6
  Stored in directory: /tmp/pip-ephem-wheel-cache-ca4k8jq5/wheels/db/43/1c/d58ea998a94cba18fba3d83fb3f574dcefe66b825f039cd932
Successfully built pprint
Installing collected packages: chardet, idna, certifi, urllib3, requests, pprint, zope.interface, pytz, datetime, Werkzeug, MarkupSafe, Jinja2, click, itsdangerous, Flask
Successfully installed Flask-1.1.1 Jinja2-2.11.1 MarkupSafe-1.1.1 Werkzeug-1.0.1 certifi-2019.11.28 chardet-3.0.4 click-7.1.1 datetime-4.3 idna-2.9 itsdangerous-1.1.0 pprint-0.1 pytz-2019.3 requests-2.23.0 urllib3-1.25.8 zope.interface-5.0.2
Removing intermediate container 4802850f35f5
 ---> 385a82d77276
Step 5/6 : EXPOSE 5000/tcp
 ---> Running in 2eec82b37bd3
Removing intermediate container 2eec82b37bd3
 ---> fdd4c754a342
Step 6/6 : CMD [ "python3", "muddy.py" ]
 ---> Running in 3331b86d6e27
Removing intermediate container 3331b86d6e27
 ---> 4710acba80f8
Successfully built 4710acba80f8
Successfully tagged muddy:latest
```

## Running the Docker image:
```
(venv) TARDIS:muddy $ make run
docker run --name muddy -d -p 5000:5000 -e API_TOKEN=f3a0a9d33043410f1b54498a42e5d3fd muddy
596d90899f0b54a3d2ddfe83d797038d53505e6c48bfa7bbfdd07a534aff737d
docker ps
CONTAINER ID        IMAGE               COMMAND              CREATED                  STATUS                  PORTS    
                NAMES
596d90899f0b        muddy               "python3 muddy.py"   Less than a second ago   Up Less than a second   0.0.0.0:5
000->5000/tcp   muddy
```

## Watching the application:
```
(venv) TARDIS:muddy $ make logs
docker logs -f muddy
 * Serving Flask app "muddy" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
172.17.0.1 - - [03/Apr/2020 02:57:03] "GET /?zip_code=48439 HTTP/1.1" 200 -
```

## Using the application:
Pass in the zipcode as a parameter
```
(venv) TARDIS:muddy $ curl http://localhost:5000/?zip_code=48439
NOT MUDDY
```

## Running the unit tests:
```
(venv) TARDIS:muddy $ python3 test_muddy.py 
....
----------------------------------------------------------------------
Ran 4 tests in 0.005s

OK
```