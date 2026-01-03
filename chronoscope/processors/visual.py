"""
Temporal Visual Processor
=========================

Applies visual transformations to simulate viewing through different
temporal layers. Each epoch has distinct visual characteristics that
evoke its historical period.

The transformations include:
- Sepia toning (age simulation)
- Gaussian blur (memory degradation)
- Film grain noise (analog artifacts)
- Vignetting (period photography)
- Color desaturation (temporal distance)
- Edge fading (dissolution at boundaries)
"""

import numpy as np
from PIL import Image, ImageFilter, ImageEnhance, ImageDraw
from typing import Tuple, Optional, Union
from dataclasses import dataclass

from ..epochs import VisualParams, get_epoch_params, interpolate_epochs


class TemporalVisualProcessor:
    """
    Processes images through temporal visual transformations.
    
    Usage:
        processor = TemporalVisualProcessor()
        result = processor.process(image, temporal_level=3)
    """
    
    def __init__(self):
        """Initialize the visual processor."""
        self._cache = {}
    
    def process(
        self,
        image: Image.Image,
        temporal_level: Union[int, float],
        params: Optional[VisualParams] = None
    ) -> Image.Image:
        """
        Apply temporal transformations to an image.
        
        Args:
            image: PIL Image to process
            temporal_level: Epoch level (0-6) or float for interpolation
            params: Optional custom VisualParams (overrides epoch defaults)
            
        Returns:
            Transformed PIL Image
        """
        # Get parameters
        if params is None:
            if isinstance(temporal_level, float) and temporal_level % 1 != 0:
                params = interpolate_epochs(temporal_level)
            else:
                params = get_epoch_params(int(temporal_level))
        
        if params is None:
            return image
        
        # Ensure RGB mode
        if image.mode != 'RGB':
            image = image.convert('RGB')
        
        # Apply transformations in sequence
        result = image.copy()
        
        # 1. Apply blur (temporal distance)
        if params.blur > 0:
            result = self._apply_blur(result, params.blur)
        
        # 2. Apply sepia toning
        if params.sepia > 0:
            result = self._apply_sepia(result, params.sepia)
        
        # 3. Adjust saturation
        if params.saturation != 1.0:
            result = self._apply_saturation(result, params.saturation)
        
        # 4. Adjust contrast
        if params.contrast != 1.0:
            result = self._apply_contrast(result, params.contrast)
        
        # 5. Add film grain noise
        if params.noise > 0:
            result = self._apply_noise(result, params.noise)
        
        # 6. Apply vignette
        if params.vignette > 0:
            result = self._apply_vignette(result, params.vignette)
        
        # 7. Apply fade/dissolution
        if params.fade > 0:
            result = self._apply_fade(result, params.fade)
        
        return result
    
    def _apply_sepia(self, image: Image.Image, intensity: float) -> Image.Image:
        """Apply sepia toning effect."""
        # Convert to numpy for matrix operations
        img_array = np.array(image, dtype=np.float32)
        
        # Sepia transformation matrix
        sepia_matrix = np.array([
            [0.393, 0.769, 0.189],
            [0.349, 0.686, 0.168],
            [0.272, 0.534, 0.131]
        ])
        
        # Apply sepia
        sepia_img = img_array @ sepia_matrix.T
        sepia_img = np.clip(sepia_img, 0, 255)
        
        # Blend with original based on intensity
        result = img_array * (1 - intensity) + sepia_img * intensity
        result = np.clip(result, 0, 255).astype(np.uint8)
        
        return Image.fromarray(result)
    
    def _apply_blur(self, image: Image.Image, radius: float) -> Image.Image:
        """Apply Gaussian blur."""
        return image.filter(ImageFilter.GaussianBlur(radius=radius))
    
    def _apply_noise(self, image: Image.Image, intensity: float) -> Image.Image:
        """Add film grain noise."""
        img_array = np.array(image, dtype=np.float32)
        
        # Generate noise
        noise = np.random.normal(0, intensity * 50, img_array.shape)
        
        # Add noise
        noisy = img_array + noise
        noisy = np.clip(noisy, 0, 255).astype(np.uint8)
        
        return Image.fromarray(noisy)
    
    def _apply_vignette(self, image: Image.Image, intensity: float) -> Image.Image:
        """Apply vignette effect (darkened corners)."""
        width, height = image.size
        
        # Create radial gradient
        x = np.linspace(-1, 1, width)
        y = np.linspace(-1, 1, height)
        X, Y = np.meshgrid(x, y)
        
        # Distance from center
        distance = np.sqrt(X**2 + Y**2)
        
        # Vignette mask (1 at center, 0 at corners)
        vignette = 1 - (distance * intensity)
        vignette = np.clip(vignette, 0, 1)
        
        # Expand to RGB
        vignette_rgb = np.stack([vignette] * 3, axis=-1)
        
        # Apply to image
        img_array = np.array(image, dtype=np.float32)
        result = img_array * vignette_rgb
        result = np.clip(result, 0, 255).astype(np.uint8)
        
        return Image.fromarray(result)
    
    def _apply_saturation(self, image: Image.Image, factor: float) -> Image.Image:
        """Adjust color saturation."""
        enhancer = ImageEnhance.Color(image)
        return enhancer.enhance(factor)
    
    def _apply_contrast(self, image: Image.Image, factor: float) -> Image.Image:
        """Adjust contrast."""
        enhancer = ImageEnhance.Contrast(image)
        return enhancer.enhance(factor)
    
    def _apply_fade(self, image: Image.Image, intensity: float) -> Image.Image:
        """Apply overall fade/dissolution effect."""
        img_array = np.array(image, dtype=np.float32)
        
        # Create fog color (warm gray for aged look)
        fog_color = np.array([245, 240, 230], dtype=np.float32)
        
        # Blend with fog
        result = img_array * (1 - intensity) + fog_color * intensity
        result = np.clip(result, 0, 255).astype(np.uint8)
        
        return Image.fromarray(result)
    
    def _apply_edge_fade(
        self,
        image: Image.Image,
        intensity: float,
        margin: float = 0.15
    ) -> Image.Image:
        """Fade edges of the image (temporal boundary dissolution)."""
        width, height = image.size
        img_array = np.array(image, dtype=np.float32)
        
        # Create edge mask
        x = np.linspace(0, 1, width)
        y = np.linspace(0, 1, height)
        
        # Smooth falloff at edges
        def edge_falloff(t, margin):
            return np.minimum(t / margin, (1 - t) / margin).clip(0, 1)
        
        mask_x = edge_falloff(x, margin)
        mask_y = edge_falloff(y, margin)
        
        X, Y = np.meshgrid(mask_x, mask_y)
        mask = X * Y
        
        # Apply intensity
        mask = mask ** (1 / (1 - intensity * 0.8 + 0.2))
        mask_rgb = np.stack([mask] * 3, axis=-1)
        
        # Fog color for edges
        fog = np.array([250, 245, 235], dtype=np.float32)
        
        result = img_array * mask_rgb + fog * (1 - mask_rgb)
        result = np.clip(result, 0, 255).astype(np.uint8)
        
        return Image.fromarray(result)


def process_image(
    image_path: str,
    output_path: str,
    temporal_level: int = 3
) -> None:
    """
    Convenience function to process an image file.
    
    Args:
        image_path: Path to input image
        output_path: Path for output image
        temporal_level: Epoch level (0-6)
    """
    processor = TemporalVisualProcessor()
    image = Image.open(image_path)
    result = processor.process(image, temporal_level)
    result.save(output_path)
