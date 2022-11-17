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
from g2v_sunbrick import G2VSunbrick

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
### get_avg_temperature()
#### RETURNS:
- `float`: average temperature of all nodes
_____
### get_all_temperatures()
#### RETURNS:
- `list`: list containing the individual temperature of each node (first element is the average)
____
### get_channel_value(channel, node=1)
#### ARGS:
- `channel`: The channel number in the range of [1, `channel_count`].
- `node`: The node of the channel in the range of [1, 'node_count`]. Default value of 1.
#### RETURNS:
- `float`: channel value in as a percentage.
____
### set_channel_value(channel, value, node=0)
#### ARGS:
- `channel`: The channel number in the range of [1, `channel_count`].
- `value`: The percentage that the channel should be set to in the range of [0.0, 100.0]
- `node`: The node of the channel in the range of [0, `node_count`] where 0 means all nodes. Default value is 0.
#### RETURNS:
- `True`: value has been set successfully
- `False`: value was not set successfully
- `None`: operation could not be completed
____
### get_intensity_factor(node=1)
The intensity factor is a percentage value that is used to control all channels on a node or nodes. The resulting value on a Sunbrick channel is the channel value x intensity factor.
#### ARGS:
- `node`: The node of the channel in the range of [1, 'node_count`]. Default value of 1.
#### RESULTS:
- `float`: intensity factor in the range of [0.0, 100.0]
____
### set_intensity_factor(value, node=0)
#### ARGS:
- `value`: The percentage that the intensity factor should be set to in the range of [0.0, 100.0]
- `node`: The node of the channel in the range of [0, `node_count`] where 0 means all nodes. Default value is 0.
#### RESULTS:
- `True`: intensity factor has been set successfully
- `False`: intensity factor was not set successfully
- `None`: operation could not be completed
____
### turn_off()
Method to set all channels on all nodes to a value of 0.
#### RESULTS:
- `bool`: Always returns `True`
____
### get_spectrum(node=1)
A spectrum is a set of values that have been applied to specific channels together.
#### ARGS:
- `node`: The node of the channel in the range of [1, 'node_count`]. Default value of 1.
#### RESULTS:
- `list`: Returns a list of `dict` items where each `dict` has a `Channel` and `Value` key.
____
### set_spectrum(spectrum_file)
#### ARGS:
- `spectrum_file`: a JSON file that contains a list of `dict` objects where each `dict` is of the form `{"Channel":<channel>, "Value":<value>}`
#### RESULTS:
- `bool`: Always returns `True`
____
