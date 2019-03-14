# certi_server
Servidor HTTP que transfomra número em um JSON cuja chave extenso é a versão por  extenso do número inteiro enviado no path.

Instale o Docker


Ubuntu:  sudo apt-get install docker.io

Windows 10:  Download Docker (https://hub.docker.com/editions/community/docker-ce-desktop-windows)


Construa o docker (ubuntu):

sudo docker build -t flask-server:latest .


Com o DOCKER instalado e cronstruído, para rodar o servidor basta executar (Ubuntu):

sudo docker run -d -p 5000:5000 flask-server


Após inicializar o docker acesse o servidor através do link:
http://localhost:5000/
