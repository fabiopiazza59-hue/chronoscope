"""
Soundscape Generator
====================

Generates descriptions and prompts for temporal soundscapes.
Each epoch has a distinct auditory signature reflecting its historical period.

Note: This module provides soundscape descriptions and AI audio generation prompts.
Actual audio synthesis requires external services (ElevenLabs, Stable Audio, etc.)
"""

from dataclasses import dataclass
from typing import List, Optional, Dict, Any
from ..epochs import EPOCHS, Epoch


@dataclass
class Soundscape:
    """Represents a temporal soundscape."""
    epoch_level: int
    epoch_name: str
    period: str
    elements: List[str]
    audio_prompt: str
    intensity: float  # 0-1, how "present" the sounds are
    clarity: float    # 0-1, how distinct the sounds are


class SoundscapeGenerator:
    """
    Generates soundscape descriptions for different temporal layers.
    
    The soundscapes become progressively more muffled and indistinct
    as we move further back in time, reflecting the degradation of
    temporal imprints.
    """
    
    def __init__(self, language: str = "fr"):
        """
        Initialize the soundscape generator.
        
        Args:
            language: "fr" for French, "en" for English
        """
        self.language = language
    
    def generate(self, temporal_level: int) -> Soundscape:
        """
        Generate a soundscape for a specific temporal level.
        
        Args:
            temporal_level: Epoch level (0-6)
            
        Returns:
            Soundscape object with descriptions and prompts
        """
        epoch = EPOCHS.get(temporal_level)
        if epoch is None:
            epoch = EPOCHS[0]
        
        # Calculate intensity and clarity based on temporal distance
        intensity = 1.0 - (temporal_level * 0.12)
        clarity = 1.0 - (temporal_level * 0.15)
        
        elements = (
            epoch.soundscape if self.language == "fr" 
            else epoch.soundscape_en
        )
        
        return Soundscape(
            epoch_level=epoch.level,
            epoch_name=epoch.name if self.language == "fr" else epoch.name_en,
            period=epoch.period,
            elements=elements,
            audio_prompt=self._enhance_prompt(epoch.audio_prompt, temporal_level),
            intensity=max(0.1, intensity),
            clarity=max(0.1, clarity)
        )
    
    def _enhance_prompt(self, base_prompt: str, level: int) -> str:
        """
        Enhance the audio generation prompt with temporal effects.
        
        Args:
            base_prompt: Base description of the soundscape
            level: Temporal level (affects processing)
            
        Returns:
            Enhanced prompt for AI audio generation
        """
        # Add temporal quality modifiers based on level
        if level == 0:
            quality = "crystal clear, high fidelity, present-day"
        elif level <= 2:
            quality = "slightly muffled, warm analog quality, nostalgic"
        elif level <= 4:
            quality = "distant, echoing, as if through old walls, ghostly"
        else:
            quality = "barely audible whispers, dreamlike, fragmentary, ancient"
        
        # Add reverb and processing hints
        reverb = min(level * 15, 80)  # Increase reverb with age
        lowpass = max(20000 - (level * 3000), 2000)  # Reduce high frequencies
        
        enhanced = (
            f"{base_prompt}. "
            f"Audio quality: {quality}. "
            f"Processing: reverb {reverb}%, low-pass filter at {lowpass}Hz, "
            f"slight tape hiss and analog warmth."
        )
        
        return enhanced
    
    def get_description(self, temporal_level: int) -> str:
        """
        Get a human-readable description of the soundscape.
        
        Args:
            temporal_level: Epoch level (0-6)
            
        Returns:
            Formatted description string
        """
        soundscape = self.generate(temporal_level)
        
        if self.language == "fr":
            header = f"🔊 Paysage sonore — {soundscape.epoch_name} ({soundscape.period})"
            elements_header = "Éléments sonores:"
            intensity_label = "Intensité"
            clarity_label = "Clarté"
        else:
            header = f"🔊 Soundscape — {soundscape.epoch_name} ({soundscape.period})"
            elements_header = "Sound elements:"
            intensity_label = "Intensity"
            clarity_label = "Clarity"
        
        elements_list = "\n".join(f"  • {e}" for e in soundscape.elements)
        
        return f"""
{header}

{elements_header}
{elements_list}

{intensity_label}: {'█' * int(soundscape.intensity * 10)}{'░' * (10 - int(soundscape.intensity * 10))} {soundscape.intensity:.0%}
{clarity_label}: {'█' * int(soundscape.clarity * 10)}{'░' * (10 - int(soundscape.clarity * 10))} {soundscape.clarity:.0%}
"""
    
    def get_all_soundscapes(self) -> List[Soundscape]:
        """Get soundscapes for all epochs."""
        return [self.generate(level) for level in range(7)]
    
    def to_dict(self, temporal_level: int) -> Dict[str, Any]:
        """
        Export soundscape as dictionary (for JSON serialization).
        
        Args:
            temporal_level: Epoch level (0-6)
            
        Returns:
            Dictionary representation
        """
        soundscape = self.generate(temporal_level)
        return {
            "epoch_level": soundscape.epoch_level,
            "epoch_name": soundscape.epoch_name,
            "period": soundscape.period,
            "elements": soundscape.elements,
            "audio_prompt": soundscape.audio_prompt,
            "intensity": soundscape.intensity,
            "clarity": soundscape.clarity
        }


# ═══════════════════════════════════════════════════════════════════════════════
# AUDIO GENERATION INTEGRATION HELPERS
# ═══════════════════════════════════════════════════════════════════════════════

def get_elevenlabs_prompt(temporal_level: int) -> str:
    """
    Generate a prompt suitable for ElevenLabs sound effects API.
    
    Args:
        temporal_level: Epoch level (0-6)
        
    Returns:
        Prompt string for ElevenLabs
    """
    generator = SoundscapeGenerator(language="en")
    soundscape = generator.generate(temporal_level)
    return soundscape.audio_prompt


def get_stable_audio_prompt(temporal_level: int) -> Dict[str, Any]:
    """
    Generate parameters suitable for Stable Audio API.
    
    Args:
        temporal_level: Epoch level (0-6)
        
    Returns:
        Dictionary with prompt and parameters
    """
    generator = SoundscapeGenerator(language="en")
    soundscape = generator.generate(temporal_level)
    
    return {
        "prompt": soundscape.audio_prompt,
        "duration": 30.0,
        "cfg_scale": 7.0,
        "seed": None,  # Random
        "steps": 100
    }
