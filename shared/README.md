# Structure

The configuration file is divided in 3 main blocks,
- `arguments`
- `simulation`
- `plotting`

These blocks will be explained below. Also, an example of a configuration file is given under the `shared` folder.

## `arguments` block
___
Here we can establish the parameters related with the results of the simulation.


### `output-format`

**Description**: Format of the resulting data of the simulation. This will be used to set the name of the files created 
by the simulation in the manner output-file + "_seedUsed." + output-format.

**Possible values**:
  - `csv`
  - `parquet`
  - `json`

**Type**: *string*

**Required**: *Yes*

**Example**:
```json
{
  "output-format": "csv"
}
```
### `output-file`

**Description**: Name of the file that will contain the results. It will be created inside the host shared folder. 
This will be used to set the name of the files created by the simulation in the manner output-file + "_seedUsed." + 
output-format.

If an [output folder](#output-folder) is given, the files will be created inside that folder.

**Type**: *string*

**Required**: *Yes*

**Example**:
```json
{
  "output-file": "test"
}
```

### `output-folder`

**Description**: Folder to save the results and/or plots of the execution. It will be created inside the host shared 
folder. 

Note /!\: *If a folder will the same name exists, it will be deleted with all it's content.*

**Type**: *string*

**Example**:
```json
{
  "output-folder": "results"
}
```

### `number-of-simulations`

**Description**: Number of simulations that will be done under the same configuration. Each simulation will be different,
as a different seed will be used per simulation.

**Type**: *integer*

**Required**: *Yes*

**Example**:
```json
{
    "number-of-simulations": 100
}
```

### Full [arguments](#arguments) example:

```json
{
    "output-format": "csv",
    "output-file": "test",
    "output-folder": "folder",
    "number-of-simulations": 3
}
```
___
## `simulation`

Here we will set the simulation parameters, depending on the simulation we want to do. These parameters are explained in
their own repository.


- [Snow family](https://github.com/logos-co/consensus-research/tree/main/simulations/snow-family#simulationsettings) (default)

___
## Plotting (to-do)

Plotting part of the configuration file. These plots are being done with [Seaborn](https://seaborn.pydata.org/).

First example:

**Description**: Scatter plot. 

**Possible values**: Any value will be mapped to the [scatterplot](https://seaborn.pydata.org/generated/seaborn.scatterplot.html) method.

**Type**: *dict*

**Example**:
```json
{
  "scatterplot": {
    "plot_options": {
      "x": "id",
      "y": "vote"
    },
    "save_options": {
      "name": "test2.png"
    }
  }
}
```



TEMPLATE:

**Description**: 

**Possible values**:
  - ``
  - ``

**Type**: **

**Required**: **

**Default value**: ``

**Example**:
```json
{

}
```