import fire
from PIL import Image


def _get_tiled_image(img: Image, num_tiles: float) -> Image:
    """
    Tiles a PIL Image and repeats by num_tiles
    :param img: PIL Image
    :param num_tiles: Number of tiles to generate
    :return: PIL Image
    """
    out_size = tuple(int(i * num_tiles) for i in img.size)
    out_img = Image.new(mode=img.mode, size=out_size)

    for i in range(0, out_size[0], img.size[0]):
        for j in range(0, out_size[1], img.size[1]):
            out_img.paste(img, box=(i, j))

    return out_img


def tile_and_save(inp_path: str, out_path: str, num_tiles: float):
    """
    Tiles img at inp_path and saves at out_path
    :param inp_path: Input image path
    :param out_path: Output image path
    :param num_tiles: Number of tiles to generate
    :return: None
    """
    if num_tiles <= 0:
        raise ValueError('num_tiles should be > 0')

    img = Image.open(inp_path)
    tiled_img = _get_tiled_image(img, num_tiles)
    tiled_img.save(out_path)


if __name__ == '__main__':
    fire.Fire(tile_and_save)
