# G2VSunbrick
Python API for interaction with the G2V Sunbrick

## Installation
```bash
pip install git+https://git@github.com/g2v-optics/G2VSunbrick.git@main
```
## Examples
Example scripts are available in the _examples_ directory.  
Please note that the _examples_ directory will not be installed with the setup but can be downloaded through GitHub.

## Required Information Before Starting

The Python API requires that you know the serial COM port that was assigned by
the computer to the Sunbrick.

Please note that you can only have one connection to a Sunbrick at a time.

## Simple Demo

```
import serial
from g2vsunbrick import G2VSunbrick

# Create a serial object with the port name (in this case 'COM3')
serial_obj = serial.Serial("COM3")

# Create a Sunbrick instance with the previously created serial_obj
sunbrick = G2VSunbrick(serial_obj)

# Set channel 1 to 50%
sunbrick.set_channel_value(1, 50.0)

# Set channel 1 to 0%
sunbrick.set_channel_value(1, 0.0)

# Get the value of channel 2
sunbrick.get_channel_value(2)

# Close the serial port when finished
serial_obj.close()
```
## G2VSunbrick module

### `G2VSunbrick(serial_obj)`
A class used to represent a single G2V Sunbrick
##### ARGS:
- `serial_obj`: The serial object that contains the port connected to the Sunbrick
____
## PROPERTIES
### brick_id
#### RETURNS:
- `string`: ID of the Sunbrick
____
### channel_count
#### RETURNS:
- `int`: number channels in the Sunbrick
____
### channel_list
#### RETURNS:
- `list`: list of channels in the Sunbrick
____
### node_count
#### RETURNS:
- `int`: number of nodes in the Sunbrick
____
### node_list
#### RETURNS:
- `list`: list of nodes in the Sunbrick
____
### firmware_version
#### RETURNS:
- `string`: the firmware version of the Sunbrick
____
### address
The address used to communicate with a Sunbrick when in array. An address of 1 implies the Sunbrick is the master Sunbrick.
#### RETURNS:
- `int`: address of the Sunbrick
____
## METHODS
### get_channel_value(channel, node=1)
#### ARGS:
- `channel`: The channel number in the range of [1, `channel_count`].
- `node`: The node of the channel in the range of [`, 'node_count`]. Default value of 1.
#### RETURNS:
- `float`: channel value in as a percentage.
