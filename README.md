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

class `G2VSunbrick(serial_obj)`
##### ARGS:
- `serial_obj`: The serial object that contains the port connected to the Sunbrick


