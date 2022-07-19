# TGA to DDS Batch Converter (For Transport Fever 2)
A simple TGA to DDS in-place batch-converter written in Python and leveraging ImageMagick's `mogrify` command.

**Windows Only, Requires ImageMagick and Python >3.6**

## Getting Started
### Pre-Requisites:
- Install Imagick (https://imagemagick.org/index.php)
- Install Python > 3.6 (https://www.python.org/)
### Config
This script can be configured in the "constants" section at the top of `tga2dds.py`.

This script was designed for use by Transport Fever 2 modders however it also has a "generic" mode, for converting all TGA files in a folder in-place. This is enabled by default. \
If you would like to keep the .tga files after conversion to DDS, this can be set here also.
`keepOriginalFiles = True`

### Executing 
Open a Command Prompt window, navigate to the folder where `tga2dds.py` is located and run `python tga2dds.py` (or use IDLE if you have it installed).

You will then be presented with a prompt to enter the path to the folder which should be batch-converted. Note that this MUST be the full path at this time. I am not liable for any accidental loss of files. Press enter and the conversion will take place.

## Example of usage
Consider a folder `myFolder` laid out as follows:

myFolder \
|-myOtherFolder \
| |-myfileInsideOtherFolder.tga \
|-myfile.tga

If you enter the path to `myfolder` into the script, `myFolder` will now be:

myFolder \
|-myOtherFolder \
| |-myfileInsideOtherFolder.dds \
|-myfile.dds 

## Info for TpF2 Modders
In TRANSPORT_FEVER_2 mode, this script doesn't touch any of the ui icon files as they don't support DDS, as far as I am aware.


Happy converting!
Best,
Aidan
