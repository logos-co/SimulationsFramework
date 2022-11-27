# Simulations Framework

This framework is to run simulations, as well as being able to obtain plots from the results in an easy-one command manner.

Simulations supported:
- Snow family: https://github.com/logos-co/consensus-research (default)

## How to use

In order to build the image, simply run:

`docker build -t desired_name_of_docker_image .`

In order to tell the container what to do, you need to specify the options in a configuration file, as json.
More information in:


Supported parameters:
- Run parameters `--run` or `-r`
  - `both` (default) (to-do)
  - `simulation`
  - `plotter` (to-do)
- Simulation type `--protocol` or `-p` (to-do)
  - `snow-family` (default, not changeable)
- Configuration file `--configuration-file` or `-cf`
  - <configuration_file_name.json>

In order to receive the information, plots, and whatever is done inside the container, a shared folder is 
provided inside this repository. Before running the container, 

### Example of execution:

`docker run --rm -v </your/path/to/SimulationsFramework/shared>:/app/shared <desired_name_of_docker_image> 
-r <simulation> -cf <configuration_file_name.json>`

The parameters inside `< >` can be changed. Where:

- `docker run --rm` will launch a docker container, and after it finishes, it will automatically destroy itself.
- `-v </your/path/to/SimulationsFramework/shared>:/app/shared` is the mount folder that will be used to share data 
between the container and the host. In order to make things easier, the folder inside this repo can be used for that.
Still, any desired folder can be put here, as long as it is in absolute path. `/app/shared` is a internal framework
location, so this needs to remain unchanged.
- `<desired_name_of_docker_image>` is the docker image name previously created.
- `-r <simulation>` is the type of execution we want. It can be only simulation `simulation`, only plotting `plotter`,
or simulation and plot `both`. This last option is as default, so if this is the case, it is something that needs to
be specified.
- `-cf <configuration_file_name.json>` is the configuration file where we set up what we want to do in the execution. 
This file needs to be in our shared host folder. 

So, an example of a command would be:

`docker run --rm -v /mnt/d/Projects/SimulationsFramework/shared:/app/shared simulation-framework 
-r simulation -cf config_example.json`

## Project structure

(to-do)