"""
Temporal Epochs Definition
==========================

Defines the different temporal layers that the Chronoscope can observe,
each with its distinct visual and auditory characteristics.

The epochs are not tied to specific dates but to "temporal density" —
periods where many similar events occurred, creating clearer imprints.
"""

from dataclasses import dataclass
from typing import Dict, List, Optional


@dataclass
class VisualParams:
    """Visual transformation parameters for an epoch."""
    sepia: float          # Sepia intensity (0-1)
    blur: float           # Gaussian blur radius
    noise: float          # Film grain intensity (0-1)
    vignette: float       # Vignette darkness (0-1)
    saturation: float     # Color saturation (0-2, 1=normal)
    contrast: float       # Contrast adjustment (0-2, 1=normal)
    fade: float           # Overall fade/dissolution (0-1)


@dataclass
class Epoch:
    """Represents a temporal layer with its characteristics."""
    level: int
    name: str
    name_en: str
    period: str
    description: str
    description_en: str
    visual: VisualParams
    soundscape: List[str]
    soundscape_en: List[str]
    audio_prompt: str


# ═══════════════════════════════════════════════════════════════════════════════
# EPOCH DEFINITIONS
# ═══════════════════════════════════════════════════════════════════════════════

EPOCHS: Dict[int, Epoch] = {
    0: Epoch(
        level=0,
        name="Présent",
        name_en="Present",
        period="2020-2025",
        description="Net, couleurs vives, le monde tel qu'il est",
        description_en="Clear, vivid colors, the world as it is",
        visual=VisualParams(
            sepia=0.0,
            blur=0.0,
            noise=0.0,
            vignette=0.0,
            saturation=1.0,
            contrast=1.0,
            fade=0.0
        ),
        soundscape=[
            "Trafic urbain moderne",
            "Notifications de smartphones",
            "Trottinettes électriques",
            "Conversations en plusieurs langues"
        ],
        soundscape_en=[
            "Modern urban traffic",
            "Smartphone notifications", 
            "Electric scooters",
            "Multilingual conversations"
        ],
        audio_prompt="Modern city ambiance with car traffic, smartphone notification sounds, electric scooter whirring, and multilingual street conversations"
    ),
    
    1: Epoch(
        level=1,
        name="Mémoire récente",
        name_en="Recent Memory",
        period="1990-2010",
        description="Légèrement voilé, teinte de nostalgie",
        description_en="Slightly veiled, tinted with nostalgia",
        visual=VisualParams(
            sepia=0.15,
            blur=0.5,
            noise=0.05,
            vignette=0.1,
            saturation=0.9,
            contrast=0.95,
            fade=0.05
        ),
        soundscape=[
            "Moteurs de voitures plus anciens",
            "Walkman et baladeurs CD",
            "Cabines téléphoniques",
            "Sonneries de téléphones fixes"
        ],
        soundscape_en=[
            "Older car engines",
            "Walkman and CD players",
            "Phone booths",
            "Landline phone ringtones"
        ],
        audio_prompt="1990s-2000s urban ambiance with older car engines, faint music from portable CD players, phone booth sounds, and rotary phone ringing in distance"
    ),
    
    2: Epoch(
        level=2,
        name="Génération précédente",
        name_en="Previous Generation",
        period="1960-1985",
        description="Teintes dorées, grain de film argentique",
        description_en="Golden tints, silver film grain",
        visual=VisualParams(
            sepia=0.3,
            blur=1.0,
            noise=0.12,
            vignette=0.2,
            saturation=0.75,
            contrast=0.9,
            fade=0.1
        ),
        soundscape=[
            "Moteurs de 2CV et DS",
            "Postes de radio à transistors",
            "Accordéon dans les cafés",
            "Cloches d'églises",
            "Marchands ambulants"
        ],
        soundscape_en=[
            "Citroën 2CV and DS engines",
            "Transistor radios",
            "Accordion in cafés",
            "Church bells",
            "Street vendors"
        ],
        audio_prompt="1960s-70s French atmosphere with vintage Citroën engines, transistor radio playing chanson française, distant accordion music, church bells, and street vendor calls"
    ),
    
    3: Epoch(
        level=3,
        name="L'entre-deux-guerres",
        name_en="Interwar Period",
        period="1920-1955",
        description="Noir et blanc fantomatique, présences floues",
        description_en="Ghostly black and white, blurred presences",
        visual=VisualParams(
            sepia=0.5,
            blur=1.5,
            noise=0.2,
            vignette=0.35,
            saturation=0.5,
            contrast=0.85,
            fade=0.2
        ),
        soundscape=[
            "Sabots de chevaux sur pavés",
            "Tramways électriques",
            "Réverbères à gaz qui grésillent",
            "Crieur de journaux",
            "Jazz lointain"
        ],
        soundscape_en=[
            "Horse hooves on cobblestones",
            "Electric tramways",
            "Gas street lamps hissing",
            "Newspaper criers",
            "Distant jazz music"
        ],
        audio_prompt="1920s-40s urban soundscape with horse hooves on cobblestones, electric tramway bells, gas lamp hissing, newspaper boy shouting headlines, and distant jazz from a café"
    ),
    
    4: Epoch(
        level=4,
        name="La Belle Époque",
        name_en="Belle Époque",
        period="1880-1914",
        description="Sépia prononcé, silhouettes en crinolines",
        description_en="Pronounced sepia, silhouettes in crinolines",
        visual=VisualParams(
            sepia=0.7,
            blur=2.0,
            noise=0.25,
            vignette=0.45,
            saturation=0.3,
            contrast=0.8,
            fade=0.3
        ),
        soundscape=[
            "Calèches et fiacres",
            "Crieurs des rues",
            "Café-concerts",
            "Orgues de Barbarie",
            "Fontaines publiques"
        ],
        soundscape_en=[
            "Horse-drawn carriages",
            "Street criers",
            "Café-concerts",
            "Barrel organs",
            "Public fountains"
        ],
        audio_prompt="1880s-1900s Belle Époque ambiance with horse carriages, street vendors singing their wares, distant café-concert music, barrel organ melody, and fountain splashing"
    ),
    
    5: Epoch(
        level=5,
        name="Le XIXe siècle",
        name_en="19th Century",
        period="1820-1870",
        description="Image de daguerréotype, dissolution des formes",
        description_en="Daguerreotype image, dissolving forms",
        visual=VisualParams(
            sepia=0.85,
            blur=3.0,
            noise=0.35,
            vignette=0.6,
            saturation=0.15,
            contrast=0.7,
            fade=0.45
        ),
        soundscape=[
            "Travaux haussmanniens",
            "Forgerons et maréchaux-ferrants",
            "Cloches multiples",
            "Chants de travailleurs",
            "Vent dans les ruelles"
        ],
        soundscape_en=[
            "Haussmann construction work",
            "Blacksmiths and farriers",
            "Multiple church bells",
            "Workers' songs",
            "Wind in alleyways"
        ],
        audio_prompt="Mid-1800s soundscape with distant construction hammering, blacksmith anvil strikes, overlapping church bells, workers singing, and wind whistling through narrow streets"
    ),
    
    6: Epoch(
        level=6,
        name="Les temps anciens",
        name_en="Ancient Times",
        period="Avant 1820",
        description="Presque invisible, aux limites de la perception",
        description_en="Almost invisible, at the limits of perception",
        visual=VisualParams(
            sepia=0.95,
            blur=5.0,
            noise=0.5,
            vignette=0.75,
            saturation=0.05,
            contrast=0.5,
            fade=0.7
        ),
        soundscape=[
            "Cloches médiévales lointaines",
            "Marchés anciens",
            "Vent dans les pierres",
            "Murmures indistincts",
            "Silence profond"
        ],
        soundscape_en=[
            "Distant medieval bells",
            "Ancient markets",
            "Wind through stones",
            "Indistinct murmurs",
            "Deep silence"
        ],
        audio_prompt="Pre-1820 ancient atmosphere with very distant medieval church bells, faint market murmurs, wind through old stone buildings, indistinct whispered voices, and profound silence between sounds"
    )
}


def get_epoch_by_level(level: int) -> Optional[Epoch]:
    """Get an epoch by its level (0-6)."""
    return EPOCHS.get(level)


def get_epoch_params(level: int) -> Optional[VisualParams]:
    """Get visual parameters for a specific epoch level."""
    epoch = EPOCHS.get(level)
    return epoch.visual if epoch else None


def interpolate_epochs(level: float) -> VisualParams:
    """
    Interpolate between two epochs for smooth transitions.
    
    Args:
        level: Float value between 0 and 6
        
    Returns:
        Interpolated VisualParams
    """
    level = max(0, min(6, level))
    lower = int(level)
    upper = min(lower + 1, 6)
    t = level - lower
    
    p1 = EPOCHS[lower].visual
    p2 = EPOCHS[upper].visual
    
    def lerp(a: float, b: float, t: float) -> float:
        return a + (b - a) * t
    
    return VisualParams(
        sepia=lerp(p1.sepia, p2.sepia, t),
        blur=lerp(p1.blur, p2.blur, t),
        noise=lerp(p1.noise, p2.noise, t),
        vignette=lerp(p1.vignette, p2.vignette, t),
        saturation=lerp(p1.saturation, p2.saturation, t),
        contrast=lerp(p1.contrast, p2.contrast, t),
        fade=lerp(p1.fade, p2.fade, t)
    )


def list_epochs() -> List[str]:
    """Return a list of epoch names for UI display."""
    return [f"{e.level}. {e.name} ({e.period})" for e in EPOCHS.values()]


def list_epochs_en() -> List[str]:
    """Return a list of epoch names in English for UI display."""
    return [f"{e.level}. {e.name_en} ({e.period})" for e in EPOCHS.values()]
