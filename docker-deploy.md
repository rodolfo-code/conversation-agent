# Como Subir Imagem para Docker Hub

## 1. Construir a Imagem

```bash
docker build -t seu-usuario/devops-api:v1 .
```

ou

```bash
docker buildx build -t seu-usuario/devops-api:v1 .
```

## 2. Fazer Login no Docker Hub

```bash
docker login
```

Digite seu usuário e senha quando solicitado.

## 3. Enviar para o Docker Hub

```bash
docker push seu-usuario/devops-api:latest
```

## 4. Verificar no Docker Hub

Acesse https://hub.docker.com e verifique se sua imagem foi enviada.

## 5. Usar a Imagem

Outras pessoas podem usar sua imagem com:

```bash
docker pull seu-usuario/devops-api:latest
docker run -p 8000:8000 seu-usuario/devops-api:latest
```
