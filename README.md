# BlenderProc

This repository, forked from [BlenderProc](https://github.com/DLR-RM/BlenderProc), is used to synthesize a desktop scenes dataset with a set of YCB objects.

## Usage
``` console
$ python3 config_generator.py [number of objects in each scene] [number of scenes]
```
Example:
``` console
$ cd examples/desk_pose/
$ python3 config_generator.py 2 2
```

The BOP data and COCO data will be stored at "/Path/to/BlenderProc/examples/desk_pose/output"
