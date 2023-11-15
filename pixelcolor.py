import ctypes

def get_pixel_color(x, y):
    """Gets the pixel color at the specified coordinate.

    Args:
        x: The x-coordinate of the pixel.
        y: The y-coordinate of the pixel.

    Returns:
        A tuple of (red, green, blue, alpha) values.
    """

    CGSMainDisplayID = ctypes.c_uint.in_dll(ctypes.cdll.CoreGraphics, "CGSMainDisplayID")
    CGSGetDC = ctypes.c_void_p.in_dll(ctypes.cdll.CoreGraphics, "CGSGetDC")
    CGGetPixelColor = ctypes.c_uint32.in_dll(ctypes.cdll.CoreGraphics, "CGGetPixelColor")

    display_id = CGSMainDisplayID()
    dc = CGSGetDC(display_id)

    pixel_color = CGGetPixelColor(dc, x, y)

    red = (pixel_color >> 16) & 0xFF
    green = (pixel_color >> 8) & 0xFF
    blue = (pixel_color) & 0xFF
    # alpha = (pixel_color >> 24) & 0xFF

    return (red, green, blue)