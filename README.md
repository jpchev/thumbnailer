# thumbnailer

A Python web app to make thumbnails, 
based on [llibvips](http://libvips.github.io/libvips/), 
the fast image processing library with low memory needs.

This app is based on [Flask](https://palletsprojects.com/p/flask/) for the web service, 
[Celery](https://docs.celeryproject.org/en/stable/index.html) 
and [RabbitMq](https://www.rabbitmq.com/) for the task management.
For production, the webapp should probably run on a WSGI server like 
[gunicorn](https://gunicorn.org/)
The [Pyramid](https://trypyramid.com/) framework would be a more 
complete alternative to Flask.

## Install on Linux

this has been tested on [Ubuntu on WSL](https://ubuntu.com/wsl)

```shell
sudo apt-get install gtk-doc-tools
sudo apt-get install gobject-introspection
```

build libvips from sources
```shell
git clone git://github.com/jcupitt/libvips.git
./autogen.sh
make
sudo make install
```

install RabbitMq
```shell
sudo apt-get install rabbitmq-server
```

create and activate virtual environment
```shell
pip install virtualenv
virtualenv venv
source venv/bin/activate
```

install the dependencies with the command
```shell
pip install -r requirements.txt
```

if pip is not available, try with
```shell
python -m pip <pip command>
```

## Configuration
edit the file [config.py](config.py)
pay attention especially to the variable UPLOAD_FOLDER

## Run Celery workers
Workers can be started on several machines.
On each machine several workers can be started.

Activate virtual env, if not already done
```shell
source venv/bin/activate
```

run Celery worker(s) with the following command
```shell
celery -A thumbnailerapp.services.tasks worker --loglevel=info
```

## Run Flask web server
activate virtual env, if not already done
```shell
source venv/bin/activate
```
```shell
python run.py
```