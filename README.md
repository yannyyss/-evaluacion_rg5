# Evaluacion_rg5

### Requisitos

- Python 3
- Docker

### Instrucciones

- Clonar este repo
- Crear imagen de docker

```
docker build -t evaluacion_rg5 .
```

- Correr imagen

```
docker run --name evaluacion_rg5 -d -p 5050:5000 -v /root/rockstart/evaluacion/evaluacion_rg5/data:/usr/src/app/data evaluacion_rg5
```

- Cerrar puerto
```
docker stop evaluacion_rg5
```


