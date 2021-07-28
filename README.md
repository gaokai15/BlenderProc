# BlenderProc

This repository, forked from [BlenderProc](https://github.com/DLR-RM/BlenderProc), is used to synthesize a desktop scenes dataset with a set of YCB objects and generate [BOP data](https://github.com/thodan/bop_toolkit/blob/master/docs/bop_datasets_format.md) and [COCO data](https://cocodataset.org/#overview).
<p align="center">
<img src="https://user-images.githubusercontent.com/53358252/127205202-a8b657b1-dfa4-4425-95bb-b62c724cf70d.png" alt="BlenderProc rerun image" width=500>
</p>

## Usage
``` console
$ python3 config_generator.py [number of objects in each scene] [number of scenes] [output directory]
```

By default, the BOP data and COCO data will be stored at "/Path/to/BlenderProc/output"

Example:
``` console
$ cd BlenderProc
$ python3 config_generator.py 2 2 ./temp/output
```

The files will be stored at "/Path/to/BlenderProc/temp/output".

After the data is generated, the output folder structure is as below:

```
.
├── bop_data
│   ├── camera.json
│   ├── train_pbr
│   |   ├── 000000
│   |   |   ├── scene_camera.json
│   |   |   ├── scene_gt.json
│   |   |   ├── depth
│   |   |   |   ├── 000000.png
│   |   |   |   ├── 000001.png
│   |   |   |   ├── ...
│   |   |   ├── rgb
│   |   |   |   ├── 000000.png
│   |   |   |   ├── 000001.png
│   |   |   |   ├── ...
│   |   ├── 000001
│   |   ├── ...
├── coco_data
│   ├── coco_annotations.json
│   ├── rgb_0000.png
│   ├── rgb_0001.png
│   ├── ...
```

