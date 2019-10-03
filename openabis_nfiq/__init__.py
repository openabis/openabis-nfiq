import os
import subprocess
import tempfile
from io import BytesIO

from PIL import Image

NFIQ_DEFAULT_VALUE = -1


class NFIQPlugin:
    def __init__(self, config):
        self.nfiq = os.path.join(os.path.dirname(os.path.realpath(__file__)), "nfiq")
        self.image_dpi = config.get("DEFAULT_FINGERPRINT_DPI", 0)

    def compute(self, fingerprint):

        if fingerprint.image is None:
            return

        dpi = self.image_dpi
        if fingerprint.imageDpi:
            dpi = fingerprint.imageDpi

        nfiq_value = NFIQ_DEFAULT_VALUE
        try:
            # TODO: Do not store the file on disk
            with tempfile.NamedTemporaryFile("wb", suffix=".ppm", delete=True) as image_file:
                width, height, data = self.to_grayscale_and_resize(fingerprint.image, dpi)
                image_file.write(data)
                process = subprocess.Popen(
                    [self.nfiq, "-raw", "%s,%s,8" % (width, height), image_file.name], stdout=subprocess.PIPE
                )
                nfiq_value = int(process.communicate()[0])
        except Exception as e:
            print(e)

        score = fingerprint.scores.add()
        score.score = nfiq_value
        score.algorithm = "nfiq"
        return nfiq_value

    def to_grayscale_and_resize(self, image, dpi):
        """
        Convert image to 8-bit grayscale buffer

        receive image and then convert it to grayscale image
        to be used as input for extraction process. Most of the extraction
        algorithm works only with grayscale.

        :param image: byte array

        :return:
            width: width of the input image
            height: height of the input image
            image buffer: buffer of output 8-bit grayscale image
        """
        fin = BytesIO()
        fin.write(image)
        img = Image.open(fin)
        img_out = img.convert("L")

        if dpi != 500:
            width, height = img_out.size
            new_size = (int(width / (dpi / 500)), int(height / (dpi / 500)))
            img_out = img_out.resize(new_size, Image.NEAREST)

        width, height = img_out.size
        fout = BytesIO()
        img_out.save(fout, "PPM")
        fout.seek(0)
        return width, height, fout.read()
