# MMe2k Graphviz

This is my example repository to my Blog Post at [https://**Never-Stop-Learning**.de/](https://never-stop-learning.de/) about [Build a Microservice for Power Platform](https://never-stop-learning.de/build-microservices-4-pp).

## Build & Run the Microservice

Ensure, that you have installed Python and VS Code on your local machine.

1. Clone the repository

   ```cmd
   git clone https://github.com/megel/mme2k-graphviz.git
   ```

1. Open VS Code
1. Create a virtual environment. Run **[Ctrl+Shift+P] Python: Create Environment...** and install the **src/requirements.txt**
1. Launch VS Code in Debug Mode **[F5]**

## Docker Container

Here are some useful commands to build the docker image and start a new container:

1. Build the docker image:

   ```cmd
   docker build -t mme2k-graphviz .\src\.
   ```

1. Start a local docker container:

   ```cmd
   docker run --name mme2k-graphviz -p 80:80 -d mme2k-graphviz:latest
   ```

1. Stop and remove the docker container

   ```cmd
   docker rm mme2k-graphviz -f
   ```

The micro service is listening on localhost port 80 after starting the docker container.

## Using the API

Use VS Code with the RESTClient extension to run these HTTP calls.

```
### Variable
@host = http://127.0.0.1:80/

### Render a Graph
POST {{host}}/render?format=png&engine=dot
Content-Type: text/plain

A -> B
B -> C
C -> D

### Render a simple Graph
POST {{host}}/render?format=png&engine=dot
Content-Type: text/plain

"Grapviz on Python Flask rocks!" [shape=box, fontname="sego ui", style=filled, fillcolor="#ccdee0"]

### Render a more complex Graph
POST {{host}}/render?format=png&engine=dot
Content-Type: text/plain

app          [label="Canvas App", fontname="sego ui", shape=box, style=filled, fillcolor="#E696C9"]
flow         [label="Power Automate", fontname="sego ui", shape=box, style=filled, fillcolor="#72BDFD"]
http         [label="Azure Web Service", fontname="sego ui", shape=box, style=filled, fillcolor="#0078d4", fontcolor="white"]
flask        [label="Flask", fontname="sego ui", shape=box, style=filled, fillcolor="#57C580"]
graphviz     [label="Graphviz", fontname="sego ui", shape=box, style=filled, fillcolor="#85D887"]

app -> flow
flow -> app
flow -> http
http -> flow
http -> flask
flask -> http
flask -> graphviz
graphviz -> flask
```
