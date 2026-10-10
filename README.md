# Shinrin CS

**English** | [Türkçe](README.tr.md)

A 2D top-down RPG built with Python and pygame. It was written as part of an
object-oriented programming course, with a game engine architecture built on the
principles of inheritance, encapsulation and polymorphism. The game is in Turkish.

## Features

- **Scene system** — title, world, inventory, pause, settings and game-over scenes
- **Turn-based battle system**, collision and dialogue systems
- **Tile-based world map** with zones and a following camera
- **Inventory** — equipment and consumable items
- **Save / load** system and persistent settings (sound, resolution, difficulty, language)
- Single-file `.exe` build with PyInstaller and an installer with Inno Setup

## Architecture

```
engine/     Game loop, scene manager, renderer, camera, input, saving, settings
entities/   GameObject → Entity → Character → Player / Enemy / NPC
            Item → Equipment / Consumable, Interactable
scenes/     Game scenes (derived from BaseScene)
systems/    Battle, collision and dialogue systems
world/      Tile, TileMap, WorldMap, Zone
utils/      Constants, helpers, logging, installation guard
tests/      Unit tests for the entity hierarchy (unittest)
```

## Controls

| Key | Action |
|---|---|
| `W A S D` / Arrow keys | Move and navigate menus |
| `Enter` / `Z` | Confirm / interact |
| `Esc` / `X` | Back / cancel |
| `P` | Pause |
| `I` | Inventory |
| `Q` / `E` | Switch inventory tabs |

## Installation and Running

```bash
pip install -r requirements.txt
python main.py
```

Tests:

```bash
python -m unittest discover tests
```

Building a Windows `.exe` (requires PyInstaller):

```bash
python packaging/build.py     # → dist/ShinrinCS.exe
```

Packaging files (PyInstaller `.spec` files, the Inno Setup script and the installer
wizard) live in `packaging/`.
