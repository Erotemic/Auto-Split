"""  # noqa: Y021
This type stub file was generated by pyright.
"""

from d3dshot.capture_outputs.pytorch_capture_output import PytorchCaptureOutput
from PIL import Image

#


class PytorchGPUCaptureOutput(PytorchCaptureOutput):
    def __init__(self) -> None:
        ...

    def process(self, pointer, pitch, size, width, height, region, rotation):
        ...

    def to_pil(self, frame) -> Image:
        ...