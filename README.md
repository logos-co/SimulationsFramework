# Simulations Framework

This framework is to run simulations, as well as being able to obtain plots from the results in an easy-one command manner.

Simulations supported:
- Snow family: https://github.com/logos-co/consensus-research (default)

## How to use

In order to build the image, simply run:

`docker build -t desired_name_of_docker_image .`

In order to tell the container what to do, you need to specify the options in a configuration file, as json.

Supported parameters:
- Run parameters `--run` or `-r`
  - `both` (will be default) (to-do)
  - `simulation`
  - `plotter`
- Simulation type `--protocol` or `-p` (to-do)
  - `snow-family` (default, not changeable)
- Configuration file `--configuration-file` or `-cf`
  - <configuration_file_name.json>

In order to share the information, plots, and so on between the host and the container, a shared folder as example is
given in this repository. But any path would work for this.

### Explanation of commands:

`docker run --rm -v </your/path/to/SimulationsFramework/shared>:/app/shared <desired_name_of_docker_image> 
-r <simulation> -cf <configuration_file_name.json>`

The parameters inside `< >` can be changed. Where:

- `docker run --rm` will launch a docker container, and after it finishes, it will automatically destroy itself. The 
data generated will be saved in the mount folder.
- `-v </your/path/to/desired/folder>:/app/shared` is the mount folder that will be used to share data 
between the container and the host. `/app/shared` is a internal framework
location, so this needs to remain unchanged.
- `<desired_name_of_docker_image>` is the docker image name previously created with the `build` command.
- `-r <simulation>` is the type of execution we want. It can be only simulation with `simulation`, only plotting with 
`plotter`, or simulation and plot `both` (to-do). 
- `-cf <configuration_file_name.json>` is the configuration file where we set up what we want to do in the execution. 
This file is **assumed to be in our shared host folder**, so the full path is not needed. If we want the file in a 
sub-folder like `shared/test_1/config_example.json`, you need to add the relative path from `shared`. In this
example, it would be `-cf test_1/config_example.json`

### Example of use:

So, assuming we are in the root of this repository, an example of use would be:

`docker build -t simulation-framework .`

`docker run --rm -v /mnt/d/Projects/SimulationsFramework/shared:/app/shared simulation-framework 
-r simulation -cf config_example.json`

## Project structure

(to-do)