import numpy as np
from PIL import Image


def read_label(path, dtype=np.uint8):
    """Read an label image from a file.

    This function reads an label image from given file. If reading label
    doesn't work collectly, try :func:`~chainercv.utils.read_image` with
    a parameter :obj:`color=True`.

    Args:
        path (string): A path of image file.
        dtype: The type of array. The default value is :obj:`~numpy.uint8`.
        color (bool): This option determines the number of channels.
            If :obj:`True`, the number of channels is three. In this case,
            the order of the channels is RGB. This is the default behaviour.
            If :obj:`False`, this function returns a grayscale image.

    Returns:
        ~numpy.ndarray: An image.
    """

    f = Image.open(path)
    try:
        img = f.convert('P')
        img = np.asarray(img, dtype=dtype)
    finally:
        if hasattr(f, 'close'):
            f.close()

    if img.ndim == 2:
        # reshape (H, W) -> (1, H, W)
        return img[np.newaxis]
    else:
        # transpose (H, W, C) -> (C, H, W)
        return img.transpose((2, 0, 1))
