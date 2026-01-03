"""
Chronoscope - Programme ORPHÉE
==============================

Open Research Project for Historical Echo Exploration

A speculative research project exploring the possibility of observing
temporal imprints left by past events in the fabric of spacetime.

"The image dissolves if the emotion is too intense. Breathe. The past is patient."
"""

__version__ = "0.1.0"
__author__ = "Programme ORPHÉE Contributors"
__license__ = "MIT"

from .epochs import EPOCHS, get_epoch_by_level, get_epoch_params
from .processors.visual import TemporalVisualProcessor
from .processors.sound import SoundscapeGenerator

__all__ = [
    "EPOCHS",
    "get_epoch_by_level",
    "get_epoch_params",
    "TemporalVisualProcessor",
    "SoundscapeGenerator",
]
