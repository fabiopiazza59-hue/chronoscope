"""
Chronoscope - Basic Usage Example
=================================

This example demonstrates how to use the Chronoscope library
programmatically to process images and generate soundscapes.
"""

from PIL import Image
from pathlib import Path

from chronoscope import (
    TemporalVisualProcessor,
    SoundscapeGenerator,
    EPOCHS,
    get_epoch_by_level,
    interpolate_epochs
)


def main():
    """Demonstrate basic Chronoscope usage."""
    
    print("=" * 60)
    print("🔭 CHRONOSCOPE - Basic Usage Example")
    print("=" * 60)
    
    # ═══════════════════════════════════════════════════════════════════════
    # 1. Explore available epochs
    # ═══════════════════════════════════════════════════════════════════════
    
    print("\n📅 Available Temporal Epochs:")
    print("-" * 40)
    
    for level, epoch in EPOCHS.items():
        print(f"  {level}. {epoch.name} ({epoch.period})")
        print(f"     {epoch.description}")
    
    # ═══════════════════════════════════════════════════════════════════════
    # 2. Process an image through different epochs
    # ═══════════════════════════════════════════════════════════════════════
    
    print("\n🖼️ Image Processing:")
    print("-" * 40)
    
    # Create a sample image (or load your own)
    # image = Image.open("your_image.jpg")
    image = Image.new('RGB', (400, 300), color='lightblue')
    
    # Initialize the processor
    processor = TemporalVisualProcessor()
    
    # Process through several epochs
    for level in [0, 2, 4, 6]:
        epoch = get_epoch_by_level(level)
        result = processor.process(image, level)
        
        # Save the result
        output_path = f"output_epoch_{level}.png"
        result.save(output_path)
        
        print(f"  Level {level} ({epoch.name}): Saved to {output_path}")
        print(f"    Sepia: {epoch.visual.sepia:.0%}, Blur: {epoch.visual.blur:.1f}px")
    
    # ═══════════════════════════════════════════════════════════════════════
    # 3. Interpolate between epochs for smooth transitions
    # ═══════════════════════════════════════════════════════════════════════
    
    print("\n🎚️ Interpolated Processing:")
    print("-" * 40)
    
    # Process at level 2.5 (between "Génération précédente" and "L'entre-deux-guerres")
    level = 2.5
    params = interpolate_epochs(level)
    result = processor.process(image, level)
    result.save("output_interpolated.png")
    
    print(f"  Level {level}: Interpolated parameters")
    print(f"    Sepia: {params.sepia:.2f}, Blur: {params.blur:.2f}px")
    
    # ═══════════════════════════════════════════════════════════════════════
    # 4. Generate soundscapes
    # ═══════════════════════════════════════════════════════════════════════
    
    print("\n🔊 Soundscape Generation:")
    print("-" * 40)
    
    # Initialize generators for both languages
    sound_gen_fr = SoundscapeGenerator(language="fr")
    sound_gen_en = SoundscapeGenerator(language="en")
    
    # Generate soundscape for epoch 3
    level = 3
    soundscape = sound_gen_en.generate(level)
    
    print(f"  Epoch: {soundscape.epoch_name} ({soundscape.period})")
    print(f"  Intensity: {soundscape.intensity:.0%}")
    print(f"  Clarity: {soundscape.clarity:.0%}")
    print(f"  Elements:")
    for element in soundscape.elements:
        print(f"    • {element}")
    
    print(f"\n  Audio Generation Prompt:")
    print(f"    {soundscape.audio_prompt[:100]}...")
    
    # ═══════════════════════════════════════════════════════════════════════
    # 5. Export soundscape as dictionary (for JSON APIs)
    # ═══════════════════════════════════════════════════════════════════════
    
    print("\n📤 Export to Dictionary:")
    print("-" * 40)
    
    data = sound_gen_en.to_dict(level)
    print(f"  Keys: {list(data.keys())}")
    
    # ═══════════════════════════════════════════════════════════════════════
    # 6. Full description output
    # ═══════════════════════════════════════════════════════════════════════
    
    print("\n📜 Full Soundscape Description:")
    print("-" * 40)
    print(sound_gen_en.get_description(level))
    
    # ═══════════════════════════════════════════════════════════════════════
    # Done
    # ═══════════════════════════════════════════════════════════════════════
    
    print("\n" + "=" * 60)
    print("✅ Example complete!")
    print("=" * 60)
    print("\n\"L'image se dissout si l'émotion est trop intense.")
    print(" Respirez. Le passé est patient.\"\n")


if __name__ == "__main__":
    main()
