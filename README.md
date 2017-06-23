# media-sorter
Python script to sort JPEG files using EXIF data. It uses the `EXIF DateTimeOriginal` tag to determine the time at which the picture was taken. Requires `exifread` and `argparse`.

```
python main.py source_dir target_dir
```

`source_dir` is the directory where your JPEG files are located.

`target_dir` is the directory to store the sorted files.

