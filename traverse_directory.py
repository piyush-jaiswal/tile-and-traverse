import gzip
from pathlib import Path

import fire


def _is_gzipped(fp: str) -> bool:
    """
    Returns whether the file at fp is gzipped

    :param fp: file path
    :return: Is file gzipped?
    """
    with open(fp, 'rb') as rf:
        sig = rf.read(3)
    return sig == b"\x1f\x8b\x08"


def _gunzip_file(path: str) -> bool:
    """
    Gunzips the file at path.
    gzipped files with .gz suffix in filename to be gunzipped to without .gz suffix in the end, overwriting any existing files
    gzipped files without .gz suffix in the filename to be gunzipped to same path, replacing the original file

    :param path: File path
    :return: Gunzip successful?
    """
    p = Path(path)
    out_path = str(p.with_suffix('').resolve()) if p.suffix == '.gz' else path

    with open(path, 'rb') as f_in, open(out_path, 'wb') as f_out:
        compressed = gzip.compress(f_in.read())

        # for file with the same path (did not put if condition as no harm)
        f_out.seek(0)

        f_out.write(compressed)

        # for file with the same path (did not put if condition as no harm)
        f_out.truncate()

    return _is_gzipped(out_path)


def _display_gzip_files(dir_path: str, absolute: bool = False):
    """
    Display gzip files at all levels with dir_path as root
    :param dir_path: Directory path
    :param absolute: Whether to print absolute paths
    :return: None
    """
    for p in Path(dir_path).glob('**/*'):
        if p.is_file() and _is_gzipped(str(p.resolve())):
            path = str(p.resolve()) if absolute else p.name
            print(path)


def gzip_files(dir_path: str, dryrun: bool = False):
    """
    Gzip files at all levels with dir_path as root and optionally display the gzipped files
    :param dir_path: Directory path
    :param dryrun: Boolean flag to display gzipped files.
    :return: None
    """
    path = Path(dir_path)
    if not path.exists():
        raise ValueError('Invalid directory path')

    for p in path.glob('**/*'):
        if p.is_file():
            _gunzip_file(str(p.resolve()))

    if dryrun:
        _display_gzip_files(dir_path)


if __name__ == '__main__':
    fire.Fire(gzip_files)
