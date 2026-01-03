<p align="center">
  <img src="assets/logo.svg" alt="Chronoscope Logo" width="150"/>
</p>

<h1 align="center">🔭 CHRONOSCOPE</h1>

<p align="center">
  <strong>Programme ORPHÉE</strong><br/>
  <em>Open Research Project for Historical Echo Exploration</em>
</p>

<p align="center">
  <a href="https://github.com/chronoscope-project/orphee/blob/main/LICENSE">
    <img src="https://img.shields.io/badge/License-MIT-amber.svg" alt="License: MIT"/>
  </a>
  <a href="https://github.com/chronoscope-project/orphee/stargazers">
    <img src="https://img.shields.io/github/stars/chronoscope-project/orphee?style=social" alt="Stars"/>
  </a>
  <a href="https://discord.gg/chronoscope">
    <img src="https://img.shields.io/badge/Discord-Join%20us-7289da" alt="Discord"/>
  </a>
</p>

<p align="center">
  <a href="#-about">About</a> •
  <a href="#-theoretical-foundations">Theory</a> •
  <a href="#-prototypes">Prototypes</a> •
  <a href="#-quick-start">Quick Start</a> •
  <a href="#-contributing">Contributing</a>
</p>

---

## 📜 About

The **Chronoscope** project explores a fascinating hypothesis: what if past events leave informational imprints in the fabric of spacetime, and we could develop technology to observe them?

This isn't pure science fiction. The project builds upon real physical phenomena—gravitational memory effect, dynamical Casimir effect, the block universe concept—and extrapolates them toward speculative applications.

> *"Space keeps a trace. The question is not whether the information exists, but whether we can develop the technology to read it."*

### The Origin

The project was born from a simple reflection:

> "Sometimes I think that if there were no time dimension and I'm walking down the street, there are millions of people walking in the same place as me."

This intuition connects to what physicists call the **block universe**: a conception of reality where past, present, and future coexist simultaneously.

## 🧬 Theoretical Foundations

### 1. Gravitational Memory Effect
Gravitational waves leave a **permanent** deformation of spacetime. Predicted in 1974, this effect is currently being searched for by LIGO and will be a major target for future detectors (LISA, Einstein Telescope).

```
"Gravitational waves leave a permanent mark on the Universe, 
forever changing the distances between two points in space."
— Physical Review Letters
```

### 2. Dynamical Casimir Effect
The quantum "vacuum" isn't empty—it's filled with fluctuations. In 2011, researchers demonstrated that we can extract **real photons** from the vacuum by rapidly changing a system's boundary conditions.

### 3. Block Universe (Eternalism)
A conception of reality where past, present, and future **coexist**. Time doesn't "flow"—our consciousness traverses a 4D structure where all information is always there.

### 4. Asymptotic Symmetries & Holography
Spacetime symmetries might encode information holographically on the "edges" of the universe, connected to the black hole information paradox.

### The ORPHÉE Hypothesis

> **Conjecture**: If cosmic events (black hole mergers) leave gravitational memory, then local events might create **informational** micro-perturbations in the local fabric of spacetime.

## ⚙️ Prototypes

| Phase | Name | Description | Status |
|-------|------|-------------|--------|
| Alpha | **The Murmur** | Detects presence of imprints (intensity only) | Conceptual |
| Beta | **The Echo** | Captures sonic textures from the past | Simulable ✓ |
| Gamma | **The Window** | Produces blurry images | Conceptual |
| Mark I | **The Chronoscope** | Complete portable device | Vision |

### The Chronoscope Mark I Vision

```
┌─────────────────────────────────────────────────────────────┐
│                    CHRONOSCOPE MARK I                        │
├─────────────────────────────────────────────────────────────┤
│  Form: Large binocular, matte black titanium                │
│  Core: Hyperpurified silicon crystal at 0.01 K              │
│  Anchor: Fragment of bridge-object (old stone, wood)        │
│  Interface: Light neural headband for stabilization         │
│                                                              │
│  "The image stabilizes in 'pockets of clarity'—             │
│   epochs where many similar events occurred.                │
│   Not a sharp video, rather a watercolor in motion."        │
└─────────────────────────────────────────────────────────────┘
```

## 🧪 Proposed Experiments

| Level | Experiment | Difficulty |
|-------|------------|------------|
| 1 | Resonance detection in repetitive environments | Accessible |
| 2 | Local informational density measurement | Intermediate |
| 3 | Memorial photon extraction by resonance | Advanced |
| 4 | Image reconstruction via quantum coherence | Frontier |

See [theory/experiments.md](theory/experiments.md) for detailed protocols.

## 🚀 Quick Start

### Prerequisites

- Python 3.9+
- pip

### Installation

```bash
# Clone the repository
git clone https://github.com/chronoscope-project/orphee.git
cd orphee

# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Run the Software Prototype

```bash
# Launch the Gradio interface
python -m chronoscope.app

# Open http://localhost:7860 in your browser
```

### Run the Website Locally

```bash
cd website
python -m http.server 8000
# Open http://localhost:8000
```

## 📁 Project Structure

```
orphee/
├── chronoscope/              # Main application
│   ├── __init__.py
│   ├── app.py               # Gradio interface
│   ├── epochs.py            # Temporal epoch definitions
│   └── processors/
│       ├── __init__.py
│       ├── visual.py        # Visual transformations
│       └── sound.py         # Soundscape generation
├── website/                  # Project website
│   ├── index.html           # Main page
│   └── assets/
├── theory/                   # Theoretical documentation
│   ├── foundations.md       # Scientific foundations
│   ├── experiments.md       # Experimental protocols
│   ├── hypothesis.md        # The ORPHÉE hypothesis
│   └── references.bib       # Bibliography
├── examples/                 # Usage examples
│   └── basic_usage.py
├── tests/                    # Test suite
│   └── test_processors.py
├── .github/                  # GitHub configuration
│   ├── ISSUE_TEMPLATE/
│   └── CONTRIBUTING.md
├── requirements.txt
├── LICENSE
└── README.md
```

## 🗺️ Roadmap

- [x] **Phase 1** (2025-2026) — Software prototype, modeling
- [ ] **Phase 2** (2026-2028) — Preliminary experimental validation
- [ ] **Phase 3** (2028-2032) — Advanced sensor development
- [ ] **Phase 4** (2032+) — Toward Chronoscope Mark I

## 🤝 Contributing

We welcome contributors from all backgrounds:

| Role | Contribution |
|------|--------------|
| **Physicists** | Critique and refine the theoretical framework |
| **Engineers** | Design and test prototypes |
| **Developers** | Improve simulations and interface |
| **Historians** | Identify relevant test locations |
| **Philosophers** | Explore ethical implications |

### How to Contribute

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

Please read [CONTRIBUTING.md](.github/CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## 📚 References

### Scientific Papers

- Zeldovich, Y. B., & Polnarev, A. G. (1974). *Radiation of gravitational waves by a cluster of superdense stars*
- Goncharov, B., et al. (2024). *Gravitational memory and spacetime symmetries*
- Wilson, C. M., et al. (2011). *Observation of the dynamical Casimir effect in a superconducting circuit*
- Strominger, A., & Zhiboedov, A. (2016). *Gravitational Memory, BMS Supertranslations and Soft Theorems*

### Books

- Barbour, J. (1999). *The End of Time: The Next Revolution in Physics*
- Hawking, S. & Ellis, G. (1973). *The Large Scale Structure of Space-Time*

See [theory/references.bib](theory/references.bib) for the complete bibliography.

## ⚠️ Disclaimer

This project is **highly speculative**. The hypotheses presented have not been experimentally validated and may prove incorrect. The goal is not to promise results, but to rigorously explore a fascinating idea and document the journey.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

<p align="center">
  <em>"The image dissolves if the emotion is too intense. Breathe. The past is patient."</em>
</p>

<p align="center">
  <strong>Programme ORPHÉE</strong><br/>
  Open Research Project for Historical Echo Exploration<br/>
  2025–present
</p>
