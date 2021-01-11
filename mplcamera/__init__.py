from PIL import Image
import io, imageio
from matplotlib.figure import Figure


class Camera:
    """
    Adaptation from https://github.com/jwkvam/celluloid/blob/master/celluloid.py

    This makes complete snapshots of the figure, not only the new artists


    Basic Example:

    from matplotlib import pyplot as plt
    from mplcamera import Camera

    fig, ax = plt.subplots()
    ax.set_ylim(-0.25, 3.25)

    cam = Camera(fig)
    for i in range(4):
        plt.plot([i] * 10)
        cam.snap()

    cam.save('mpl_camera_animation.gif', duration=[0.25, 0.25, 1, 0.25], loop=1)

    """

    def __init__(self, figure: Figure) -> None:
        """Create camera from matplotlib figure."""
        self._figure = figure
        self._photos = []
        self._n = 0

    def snap(self, **savefig_kwargs):
        """Capture current state of the figure."""
        buf = io.BytesIO()
        self._figure.savefig(buf, **savefig_kwargs)
        img = Image.open(buf)
        self._photos.append(img)
        self._n += 1

    def save(self, filename, **mimsave_kwargs):
        """creates and saves a gif from the photos stored in self._photos

        you can define mimsave_kwargs, eg.:
            duration: int or list - duration in seconds
            loop: stop the gif after x loops

        """
        imageio.mimsave(filename, self._photos, **mimsave_kwargs)
