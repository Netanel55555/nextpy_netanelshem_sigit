class Pixel:

    def __init__(self, x=0, y=0, red=0, green=0, blue=0):
        self._x = x
        self._y = y
        self._red = red
        self._green = green
        self._blue = blue

    def set_coords(self, x, y):
        self._x = x
        self._y = y

    def set_grayscale(self):
        sum = self._red + self._green + self._blue
        self._red = sum / 3
        self._green = sum / 3
        self._blue = sum / 3

    def print_pixel_info(self):
        print("X:%d Y:%d, color: (%d,%d,%d)", self._x, self._y, self._red, self._green, self._blue)


def main():
    p = Pixel(5, 6, 250)
    p.print_pixel_info()
    p.set_grayscale()
    p.print_pixel_info()


if __name__ == "__main__":
    main()
