# Django-WebSocket 🚀

## Comenzando 

_Esta aplicacion esta diseñada para trabajar con websocket soportado en redis_



### Pre-requisitos 📋

_Para que este proyecto funcione correctamente necesitas los siguientes paquetes_

* Python (2.7, 3.5, 3.6, 3.7)
* Django (1.11, 2.0, 2.1)
* Docker (18.09.2, build 6247962)

### Instalación 🔧

_Sigue los pasos para que se ejecute correctamenete_


_Parado en la caperta principal del proyecto ejecuta los siguientes comandos en el CMD o POWERSHELL de windows_

```

#Se installan los paquetes necesarios

pip install -r requirements.txt

#Se hacen las migraciones

python manage.py makemigrations

#Migramos a las base de datos

python manage.py migrate

#$ OPTIONAL Crea un super usuario para administrar el poryecto

python manage.py createsuperuser

#Inicia los servidores 

docker run -p 6379:6379 -d redis:2.8
python manage.py runserver

```



## Construido con 🛠️


* [PYTHON](https://www.python.org/) - El lenguaje usado
* [DJANGO](https://www.djangoproject.com/) - El framework web usado
* [DOCKER](https://www.docker.com//) - El soporte para el servidor de redis



## Autores ✒️


* **Santiago Yunda** - *Implementacion* - [Swanky](https://github.com/YUND4)


## Licencia 📄

MIT


![alt text](https://github.com/YUND4/Django-WebSocket/blob/master/docs/images/lobby.png)

![alt text](https://github.com/YUND4/Django-WebSocket/blob/master/docs/images/chat.png)

![alt text](https://github.com/YUND4/Django-WebSocket/blob/master/docs/images/permission.png)

![alt text](https://github.com/YUND4/Django-WebSocket/blob/master/docs/images/notification.png)