# Tile and Traverse

### Tile Image
Generate and save a tiled image from an input image. Command line inputs:
- path to an image file as input
- number of tiles to be generated
- path to output the tiled imag

### Traverse directory and gzip
Display all gzipped files under the directory at any level (file can be gzipped regardless of having
.gz suffix in the filename). Gunzip the files inplace:

- gzipped files with .gz suffix in filename to be gunzipped to without .gz suffix in the end,
overwriting any existing files
- gzipped files without .gz suffix in the filename to be gunzipped to same path, replacing the
original file

Command line input:
- path to a directory
- `--dryrun` flag to just display gzipped files with out extracting the files


# Requirements
```bash
pip install -r requirements.txt
```

# Usage
The project is written in <b>python 3.7</b>.
### Tile Image
The num_tiles parameter is taken in `float` format and repeats the input image as many times as possible.
```python
python tile_image.py <--inp_path INP_PATH> <--out_path OUT_PATH> <--num_tiles NUM_TILES>
```

### Traverse Directory
Assumption: Files are gunzipped regardless of whether they are already gunzipped. This can potentially be avoided by doing a check first.
```python
python traverse_directory.py <--dir_path DIR_PATH> [--dryrun]
```

### Help
```python
python tile_image.py --help
python traverse_directory.py --help
```
