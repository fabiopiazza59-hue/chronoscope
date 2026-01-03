"""
Tests for Chronoscope processors
"""

import pytest
import numpy as np
from PIL import Image

from chronoscope.epochs import (
    EPOCHS,
    get_epoch_by_level,
    get_epoch_params,
    interpolate_epochs,
    list_epochs,
    VisualParams
)
from chronoscope.processors.visual import TemporalVisualProcessor
from chronoscope.processors.sound import SoundscapeGenerator


# ═══════════════════════════════════════════════════════════════════════════════
# FIXTURES
# ═══════════════════════════════════════════════════════════════════════════════

@pytest.fixture
def sample_image():
    """Create a sample RGB image for testing."""
    return Image.new('RGB', (100, 100), color='blue')


@pytest.fixture
def visual_processor():
    """Create a visual processor instance."""
    return TemporalVisualProcessor()


@pytest.fixture
def sound_generator():
    """Create a sound generator instance."""
    return SoundscapeGenerator(language="en")


# ═══════════════════════════════════════════════════════════════════════════════
# EPOCHS TESTS
# ═══════════════════════════════════════════════════════════════════════════════

class TestEpochs:
    """Tests for epoch definitions and utilities."""
    
    def test_all_epochs_defined(self):
        """All 7 epochs should be defined."""
        assert len(EPOCHS) == 7
        for i in range(7):
            assert i in EPOCHS
    
    def test_epoch_has_required_fields(self):
        """Each epoch should have all required fields."""
        for level, epoch in EPOCHS.items():
            assert epoch.level == level
            assert epoch.name
            assert epoch.name_en
            assert epoch.period
            assert epoch.description
            assert epoch.visual is not None
            assert len(epoch.soundscape) > 0
            assert epoch.audio_prompt
    
    def test_get_epoch_by_level(self):
        """get_epoch_by_level should return correct epoch."""
        epoch = get_epoch_by_level(0)
        assert epoch.name == "Présent"
        
        epoch = get_epoch_by_level(6)
        assert epoch.name == "Les temps anciens"
        
        epoch = get_epoch_by_level(99)
        assert epoch is None
    
    def test_get_epoch_params(self):
        """get_epoch_params should return VisualParams."""
        params = get_epoch_params(0)
        assert isinstance(params, VisualParams)
        assert params.sepia == 0.0
        
        params = get_epoch_params(6)
        assert params.sepia == 0.95
    
    def test_interpolate_epochs(self):
        """interpolate_epochs should blend between levels."""
        # At exact levels, should match those levels
        params_0 = interpolate_epochs(0.0)
        assert params_0.sepia == 0.0
        
        params_6 = interpolate_epochs(6.0)
        assert params_6.sepia == 0.95
        
        # Midpoint should be interpolated
        params_mid = interpolate_epochs(3.0)
        assert 0.0 < params_mid.sepia < 0.95
        
        # Between 0 and 1
        params_half = interpolate_epochs(0.5)
        expected_sepia = 0.0 * 0.5 + 0.15 * 0.5  # Blend of level 0 and 1
        assert abs(params_half.sepia - expected_sepia) < 0.01
    
    def test_interpolate_clamps_values(self):
        """interpolate_epochs should clamp out-of-range values."""
        params_neg = interpolate_epochs(-5.0)
        assert params_neg.sepia == 0.0
        
        params_high = interpolate_epochs(100.0)
        assert params_high.sepia == 0.95
    
    def test_list_epochs(self):
        """list_epochs should return formatted strings."""
        epochs = list_epochs()
        assert len(epochs) == 7
        assert "Présent" in epochs[0]
        assert "2020-2025" in epochs[0]


# ═══════════════════════════════════════════════════════════════════════════════
# VISUAL PROCESSOR TESTS
# ═══════════════════════════════════════════════════════════════════════════════

class TestVisualProcessor:
    """Tests for the visual processor."""
    
    def test_process_returns_image(self, visual_processor, sample_image):
        """Processing should return a PIL Image."""
        result = visual_processor.process(sample_image, 3)
        assert isinstance(result, Image.Image)
    
    def test_process_preserves_dimensions(self, visual_processor, sample_image):
        """Processing should preserve image dimensions."""
        result = visual_processor.process(sample_image, 3)
        assert result.size == sample_image.size
    
    def test_process_level_0_minimal_change(self, visual_processor, sample_image):
        """Level 0 (present) should have minimal transformation."""
        result = visual_processor.process(sample_image, 0)
        
        # Convert to arrays for comparison
        original = np.array(sample_image)
        processed = np.array(result)
        
        # Should be very similar (allowing for minor float rounding)
        assert np.allclose(original, processed, atol=5)
    
    def test_process_level_6_significant_change(self, visual_processor, sample_image):
        """Level 6 should have significant transformation."""
        result = visual_processor.process(sample_image, 6)
        
        original = np.array(sample_image)
        processed = np.array(result)
        
        # Should be significantly different
        diff = np.abs(original.astype(float) - processed.astype(float)).mean()
        assert diff > 50  # Substantial change
    
    def test_process_with_custom_params(self, visual_processor, sample_image):
        """Should accept custom VisualParams."""
        custom_params = VisualParams(
            sepia=1.0,
            blur=0.0,
            noise=0.0,
            vignette=0.0,
            saturation=1.0,
            contrast=1.0,
            fade=0.0
        )
        
        result = visual_processor.process(sample_image, 0, params=custom_params)
        assert isinstance(result, Image.Image)
    
    def test_process_handles_grayscale(self, visual_processor):
        """Should handle grayscale images by converting to RGB."""
        gray_image = Image.new('L', (50, 50), color=128)
        result = visual_processor.process(gray_image, 3)
        
        assert result.mode == 'RGB'
        assert result.size == (50, 50)
    
    def test_process_handles_rgba(self, visual_processor):
        """Should handle RGBA images."""
        rgba_image = Image.new('RGBA', (50, 50), color=(255, 0, 0, 128))
        result = visual_processor.process(rgba_image, 3)
        
        assert result.mode == 'RGB'


# ═══════════════════════════════════════════════════════════════════════════════
# SOUNDSCAPE GENERATOR TESTS
# ═══════════════════════════════════════════════════════════════════════════════

class TestSoundscapeGenerator:
    """Tests for the soundscape generator."""
    
    def test_generate_returns_soundscape(self, sound_generator):
        """Should return a Soundscape object."""
        from chronoscope.processors.sound import Soundscape
        
        result = sound_generator.generate(3)
        assert isinstance(result, Soundscape)
    
    def test_generate_has_elements(self, sound_generator):
        """Generated soundscape should have elements."""
        result = sound_generator.generate(3)
        assert len(result.elements) > 0
        assert result.audio_prompt
    
    def test_intensity_decreases_with_level(self, sound_generator):
        """Intensity should decrease as we go back in time."""
        result_0 = sound_generator.generate(0)
        result_6 = sound_generator.generate(6)
        
        assert result_0.intensity > result_6.intensity
    
    def test_clarity_decreases_with_level(self, sound_generator):
        """Clarity should decrease as we go back in time."""
        result_0 = sound_generator.generate(0)
        result_6 = sound_generator.generate(6)
        
        assert result_0.clarity > result_6.clarity
    
    def test_language_french(self):
        """French language should return French elements."""
        generator = SoundscapeGenerator(language="fr")
        result = generator.generate(2)
        
        # Should contain French text
        assert any("Moteurs" in e or "Accordéon" in e for e in result.elements)
    
    def test_language_english(self):
        """English language should return English elements."""
        generator = SoundscapeGenerator(language="en")
        result = generator.generate(2)
        
        # Should contain English text
        assert any("engines" in e.lower() or "accordion" in e.lower() for e in result.elements)
    
    def test_get_description(self, sound_generator):
        """get_description should return formatted string."""
        result = sound_generator.get_description(3)
        
        assert "Soundscape" in result
        assert "Intensity" in result
        assert "Clarity" in result
    
    def test_to_dict(self, sound_generator):
        """to_dict should return dictionary."""
        result = sound_generator.to_dict(3)
        
        assert isinstance(result, dict)
        assert "epoch_level" in result
        assert "elements" in result
        assert "audio_prompt" in result
    
    def test_get_all_soundscapes(self, sound_generator):
        """get_all_soundscapes should return 7 soundscapes."""
        result = sound_generator.get_all_soundscapes()
        assert len(result) == 7


# ═══════════════════════════════════════════════════════════════════════════════
# INTEGRATION TESTS
# ═══════════════════════════════════════════════════════════════════════════════

class TestIntegration:
    """Integration tests for the full pipeline."""
    
    def test_full_pipeline(self, sample_image):
        """Test complete processing pipeline."""
        processor = TemporalVisualProcessor()
        sound_gen = SoundscapeGenerator()
        
        # Process through all levels
        for level in range(7):
            image_result = processor.process(sample_image, level)
            sound_result = sound_gen.generate(level)
            
            assert image_result is not None
            assert sound_result is not None
    
    def test_interpolated_levels(self, sample_image):
        """Test processing with interpolated levels."""
        processor = TemporalVisualProcessor()
        
        for level in [0.5, 1.5, 2.5, 3.5, 4.5, 5.5]:
            result = processor.process(sample_image, level)
            assert result is not None


# ═══════════════════════════════════════════════════════════════════════════════
# RUN TESTS
# ═══════════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
