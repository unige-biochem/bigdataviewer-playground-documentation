# Workflows

Task-oriented guides for common use cases. Each workflow walks you through a complete process from start to finish.

## Overview

Unlike feature documentation that explains what each tool does, workflows show **how to accomplish specific goals** with your data.

| Workflow | Goal | Duration |
|----------|------|----------|
| [Warpy: Large 2D Image Registration](warpy/index.md) | Register whole slide images, transfer annotations | ~90 min |
| [Process LLS7 Timelapse](lls7_timelapse.md) | Deskew, deconvolve, and export lattice data | ~30 min |
| [Fuse Multi-Tile Acquisition](fuse_tiles.md) | Combine tiled images into a single volume | ~20 min |

## Documentation

```{toctree}
:maxdepth: 2

warpy/index
lls7_timelapse
fuse_tiles
```

## How to Use These Guides

Each workflow follows a consistent structure:

1. **Goal** - What you'll achieve
2. **Prerequisites** - What you need before starting
3. **Steps** - Detailed walkthrough with screenshots/commands
4. **Expected Output** - What success looks like
5. **Troubleshooting** - Common issues and solutions

## Suggesting New Workflows

If you have a workflow you'd like documented:
- Open an issue on [GitHub](https://github.com/bigdataviewer/bigdataviewer-playground)
- Ask on the [Image.sc Forum](https://forum.image.sc/)
