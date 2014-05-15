import os
import errno

CHUNK_SIZE = 1024  # 1 KB

CUTOFF_SIZE = 1024 ** 2 * 500  # 500 MB


def chunked_file(fobj, chunk_size=CHUNK_SIZE):
    while True:
        chunk = fobj.read(chunk_size)
        if not chunk:
            break
        yield chunk


def chunked_save(fobj, to_loc):
    with open(to_loc, 'w+') as to_file:
        for chunk in chunked_file(fobj):
            to_file.write(chunk)
    return to_loc


def ensure_directory(directory):
    try:
        os.makedirs(directory)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise