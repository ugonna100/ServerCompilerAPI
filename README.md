# ServerCompilerAPI
Docker hosted Flask API for programming language compiling and output results

## Installation
Currently tested in Windows using Docker For Windows, easily done in linux and environment will have better permissions.
Before anything can be done, Docker needs to be installed on the host computer
```
git clone https://github.com/ugonna100/ServerCompilerAPI
cd ServerCompilerAPI
docker build -t servercompilerapi . (should take around 10-25 minutes for the first time)
docker run -it -p 5000:5000 servercompilerapi
open index.html and test away.
```
This is expandable to a web server but to do so, it is recommended to implement security practices for bash commands.
The Docker VM by default does not give maximum priveleges but regardless is seperate from the main host entirely and can be set up again very easily
To avoid misuse, a parser may be needed to examine code for malicious commands.
