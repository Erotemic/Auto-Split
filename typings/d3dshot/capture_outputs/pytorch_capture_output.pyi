"""  # noqa: Y021
This type stub file was generated by pyright.
"""

from PIL import Image
from d3dshot.capture_output import CaptureOutput


class PytorchCaptureOutput(CaptureOutput):
    def __init__(self) -> None:
        ...

    def process(self, pointer, pitch, size, width, height, region, rotation):
        ...

    def to_pil(self, frame) -> Image:
        ...

    def stack(self, frames, stack_dimension):
        ...