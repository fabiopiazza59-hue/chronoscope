"""
Chronoscope - Main Application
==============================

Gradio-based interface for the Chronoscope temporal viewer prototype.
This software simulation demonstrates the visual and auditory transformations
that would be produced by a functional Chronoscope device.

"The image dissolves if the emotion is too intense. Breathe. The past is patient."
"""

import gradio as gr
from PIL import Image
from typing import Tuple, Optional

from .epochs import EPOCHS, list_epochs
from .processors.visual import TemporalVisualProcessor
from .processors.sound import SoundscapeGenerator


# ═══════════════════════════════════════════════════════════════════════════════
# CONFIGURATION
# ═══════════════════════════════════════════════════════════════════════════════

TITLE = "🔭 CHRONOSCOPE — La Fenêtre d'Orphée"
DESCRIPTION = """
<div style="text-align: center; max-width: 800px; margin: 0 auto;">
    <h3 style="color: #d97706;">Programme ORPHÉE</h3>
    <p style="color: #94a3b8; font-style: italic;">
        Open Research Project for Historical Echo Exploration
    </p>
    <p style="color: #64748b; font-size: 0.9em;">
        Ce prototype logiciel simule les transformations visuelles et sonores 
        que produirait un Chronoscope fonctionnel. Chargez une image et 
        naviguez à travers les couches temporelles.
    </p>
</div>
"""

FOOTER = """
<div style="text-align: center; margin-top: 2rem; padding: 1rem; 
            border-top: 1px solid #374151; color: #64748b;">
    <p style="font-style: italic; margin-bottom: 0.5rem;">
        "L'image se dissout si l'émotion est trop intense. Respirez. Le passé est patient."
    </p>
    <p style="font-size: 0.8em;">
        Programme ORPHÉE — Open Source — MIT License
    </p>
</div>
"""

CSS = """
.gradio-container {
    font-family: 'Crimson Pro', Georgia, serif !important;
    background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%) !important;
}
.gr-button-primary {
    background: linear-gradient(135deg, #92400e, #78350f) !important;
    border: none !important;
}
.gr-button-primary:hover {
    background: linear-gradient(135deg, #b45309, #92400e) !important;
}
.gr-input, .gr-box {
    border-color: #374151 !important;
    background: #1e293b !important;
}
.gr-panel {
    background: #0f172a !important;
    border-color: #374151 !important;
}
footer {
    display: none !important;
}
"""


# ═══════════════════════════════════════════════════════════════════════════════
# APPLICATION LOGIC
# ═══════════════════════════════════════════════════════════════════════════════

# Initialize processors
visual_processor = TemporalVisualProcessor()
sound_generator = SoundscapeGenerator(language="fr")


def process_image(
    image: Optional[Image.Image],
    temporal_level: int
) -> Tuple[Optional[Image.Image], str, str]:
    """
    Process an image through the temporal viewer.
    
    Args:
        image: Input PIL Image
        temporal_level: Selected epoch level (0-6)
        
    Returns:
        Tuple of (processed image, epoch info, soundscape description)
    """
    if image is None:
        return None, "", ""
    
    # Get epoch information
    epoch = EPOCHS.get(temporal_level, EPOCHS[0])
    
    # Process image
    processed = visual_processor.process(image, temporal_level)
    
    # Generate soundscape description
    soundscape = sound_generator.get_description(temporal_level)
    
    # Create epoch info text
    epoch_info = f"""
## {epoch.name} ({epoch.period})

*{epoch.description}*

### Paramètres visuels
- Sépia: {epoch.visual.sepia:.0%}
- Flou: {epoch.visual.blur:.1f}px
- Grain: {epoch.visual.noise:.0%}
- Vignette: {epoch.visual.vignette:.0%}
- Saturation: {epoch.visual.saturation:.0%}
- Dissolution: {epoch.visual.fade:.0%}
"""
    
    return processed, epoch_info, soundscape


def create_interface() -> gr.Blocks:
    """Create and configure the Gradio interface."""
    
    with gr.Blocks(
        title="Chronoscope",
        css=CSS,
        theme=gr.themes.Base(
            primary_hue="amber",
            secondary_hue="slate",
            neutral_hue="slate",
        )
    ) as app:
        
        # Header
        gr.HTML(f"<h1 style='text-align: center; color: #fcd34d;'>{TITLE}</h1>")
        gr.HTML(DESCRIPTION)
        
        with gr.Row():
            # Left column: Input
            with gr.Column(scale=1):
                gr.Markdown("### 📷 Image source")
                input_image = gr.Image(
                    label="Charger une image",
                    type="pil",
                    height=400
                )
                
                gr.Markdown("### ⏱️ Profondeur temporelle")
                temporal_slider = gr.Slider(
                    minimum=0,
                    maximum=6,
                    step=1,
                    value=0,
                    label="Niveau temporel",
                    info="0 = Présent, 6 = Temps anciens"
                )
                
                # Epoch selection dropdown
                epoch_dropdown = gr.Dropdown(
                    choices=list_epochs(),
                    value=list_epochs()[0],
                    label="Époque",
                    interactive=True
                )
                
                process_btn = gr.Button(
                    "🔭 Observer",
                    variant="primary",
                    size="lg"
                )
            
            # Right column: Output
            with gr.Column(scale=1):
                gr.Markdown("### 👁️ Vision temporelle")
                output_image = gr.Image(
                    label="Image transformée",
                    type="pil",
                    height=400,
                    interactive=False
                )
                
                with gr.Accordion("📜 Informations de l'époque", open=True):
                    epoch_info = gr.Markdown("")
                
                with gr.Accordion("🔊 Paysage sonore", open=True):
                    soundscape_info = gr.Markdown("")
        
        # Footer
        gr.HTML(FOOTER)
        
        # ═══════════════════════════════════════════════════════════════════════
        # EVENT HANDLERS
        # ═══════════════════════════════════════════════════════════════════════
        
        def sync_dropdown_to_slider(dropdown_value: str) -> int:
            """Extract level from dropdown selection."""
            try:
                return int(dropdown_value.split(".")[0])
            except (ValueError, IndexError):
                return 0
        
        def sync_slider_to_dropdown(slider_value: int) -> str:
            """Get dropdown value from slider."""
            epochs = list_epochs()
            return epochs[int(slider_value)] if 0 <= slider_value < len(epochs) else epochs[0]
        
        # Sync slider and dropdown
        epoch_dropdown.change(
            fn=sync_dropdown_to_slider,
            inputs=[epoch_dropdown],
            outputs=[temporal_slider]
        )
        
        temporal_slider.change(
            fn=sync_slider_to_dropdown,
            inputs=[temporal_slider],
            outputs=[epoch_dropdown]
        )
        
        # Process image on button click
        process_btn.click(
            fn=process_image,
            inputs=[input_image, temporal_slider],
            outputs=[output_image, epoch_info, soundscape_info]
        )
        
        # Also process on slider change (live preview)
        temporal_slider.release(
            fn=process_image,
            inputs=[input_image, temporal_slider],
            outputs=[output_image, epoch_info, soundscape_info]
        )
        
        # Process on image upload
        input_image.change(
            fn=process_image,
            inputs=[input_image, temporal_slider],
            outputs=[output_image, epoch_info, soundscape_info]
        )
    
    return app


# ═══════════════════════════════════════════════════════════════════════════════
# ENTRY POINT
# ═══════════════════════════════════════════════════════════════════════════════

def main():
    """Launch the Chronoscope application."""
    app = create_interface()
    app.launch(
        server_name="0.0.0.0",
        server_port=7860,
        share=False,
        show_error=True
    )


if __name__ == "__main__":
    main()
