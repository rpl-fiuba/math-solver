# math-learning-server

Servidor Django

## requisitos previos

- Docker: docker.com
- Docker compose: https://docs.docker.com/compose/install/
- Python3: https://www.python.org/
- virtualenv: https://virtualenv.pypa.io/en/latest/

## Correr usando Docker compose

Correr el siguiente comando en una terminal estando posicionado en el mismo directorio que el docker-compose.yml:

Primera vez:

    $ source ./bin/activate
    $ pip3 install -r mathlearning/requirements.txt 
    $ docker-compose up --build
    
Una vez creada la imagen (una vez corrido el comando anterior) a menos de que haya cambios se puede correr el siguiente comando:

    $ docker-compose up


## Correr utilizando un virtualenv

correr el siguiente comando para activar el entorno virtual:

    $ source ./bin/activate

luego correr el siguiente comando para instalar las dependencias:

    $ pip3 install -r requirements.txt 

por ultimo para iniciar la aplicacion django correr:

    $ python manage.py runserver 0.0.0.0:5000


## Tests

### Correr usando IntelliJ
    Usar las run configurations creadas "Test All" / "Test Resolve" / "Test Evaluate"

### Correr con la consola

    Ejecutar un paquete el script de manage con el comando de tests y el paquete a evaluar como parametro
    ./manage.py test test.api.evaluate

    Ejecutar todos los tests
    ./manage.py test

### Agregar tests

    Agregar clase al paquete de test.api.(evaluate/resolve) segun corresponda
    La clase debe comenzar con el prefijo "test_" (ej: test_domain.py)
    El metodo del test debe comenzar con el prefijo "test_" (ej: test_rational_domain_root_zero)