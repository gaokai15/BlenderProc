# BlenderProc

This repository, forked from [BlenderProc](https://github.com/DLR-RM/BlenderProc), is used to synthesize a dataset of desktop scenes with a set of YCB objects.

## Usage
''' console
$ python3 config_generator.py [number of objects in each scene] [number of scenes]
'''

''' console
$ cd examples/desk_pose/
$ python3 config_generator.py 2 2
'''

The BOP data and COCO data are stored in "/Path/to/BlenderProc/examples/desk_pose/output"