# GMD (Gemini Markdown) v1.0GA
**The Practitioner’s Atomic Logging & Editing Environment**
Updated: 2026-03-01 10:00

GMD is a high-fidelity, identity-blind markdown environment designed for speed, portability, and temporal resilience. It is built to be a "ghost" in the system—inheriting authority from the execution environment and staying out of the way of the data.



## Key Features
---
| Status | Feature | In Detail |
|---|---|---|
| ✅ | **Atomic Versioning** | High-resolution `%H%M%S` timestamps for collision-free iterative journaling. |
| ✅ | **Fluid Palette** | Geometry-agnostic icon/snippet engine; adapts to any `.pal` file without code changes. |
| ✅ | **Safe Recursion** | `create` command with deep-blue status interlock for verified directory/file initialization. |
| ✅ | **Hybrid Architecture** | Combines `prompt_toolkit` for interactive editing with `rich` for professional rendering. |
| ✅ | **Multilingual Flow** | Native support for Emoji, Kanji, and Devanagari (Sanskrit) via hot-swappable substrates. |

## Usage
- `gmd ls`: List the archive with temporal sorting and title-case formatting.
- `gmd new <title>`: Create a new timestamped log entry. Supports multiple entries with the same title.
- `gmd read <path>`: View rendered markdown with syntax highlighting in the native pager.
- `gmd edit <path>`: Modify existing notes using the internal buffer.
- `gmd create <path>`: Initialize a new directory structure and file with a `y/n` confirmation gate.
- `gmd find`: Interactively search across the entirety of your markdown archive.

## The Philosophy of Temporal Collision
The most potent feature of GMD is an emergent property of its filename structure: `YYYYMMDD_HHMMSS_title.md`. Because resolution is down to the **second**, the filesystem acts as a version-control engine. 

You can fire `gmd new dev_log` ten times in a minute; GMD simply creates ten unique, chronological artifacts. It isn't what the code does; it's how you use the side effect to manage project pulses, research streams, and work logs.



## Installation
1. Ensure you have Python 3.10+ installed.
2. Install dependencies: `pip install prompt_toolkit rich`
3. Alias the script: `chmod +x gmd.py && ln -s $(pwd)/gmd.py /usr/local/bin/gmd`

## The Palette Library
GMD prioritizes any `.pal` file in the current working directory. To switch modes, simply swap the active file:
* `standard.pal`: Tasks, Dev, and Brainstorming.
* `kanji_essentials.pal`: Japanese ideogram insertion without IME overhead.
* `sanskrit_devanagari.pal`: Classical Sanskrit script support.

  ***NOTE: don't put more than one palette file in a working directory at the time, as the editor will only use the first that it encounters***
---
**Vibe Coded by James G. Stallings II**
*With technical effector logic provided by Google LLC's Gemini 3 Flash (Web/Paid Tier).*

This tool is a signatory example of what can be accomplished when you treat an LLM as a slightly hung-over, highly competent co-worker. Don't gab. Express desires in *doublets of opposition*: "Add Feature X; under no circumstances disturb Y." 

Natural language is an inefficient tool for coding, yet it is the primary interface for "vibe coding." A careful balance must be struck: stay focused, be concise, and treat the model as a peer-collaborator, not a digital advisor.

GMD puts the polish on the project. It is a sharp blade—use it well.

Cheers! 🔥
