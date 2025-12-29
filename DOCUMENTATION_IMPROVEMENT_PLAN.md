# Documentation Improvement Plan

This document outlines the plan to improve BigDataViewer Playground documentation based on analysis of the source repositories.

## Executive Summary

The current documentation covers `bigdataviewer-playground` and `bigdataviewer-image-loaders` well, but **`bigdataviewer-biop-tools` commands are largely missing** from user-facing documentation. This represents a significant gap as biop-tools contains ~70 commands for advanced functionality.

---

## Source Repository Analysis

### bigdataviewer-playground
- **Total Commands**: 57
- **Fully Documented**: 51 (with @Plugin description + @Parameter labels)
- **Partially Documented**: 6
- **Coverage**: 89%
- **Key Features**: Core BDV/BVV viewers, source management, basic transforms, BigWarp integration, state management

### bigdataviewer-image-loaders
- **Total Commands**: 10 active (4 legacy/deprecated)
- **Fully Documented**: 10
- **Coverage**: 100%
- **Key Features**: Bio-Formats bridge, OMERO integration, QuPath projects, ImagePlus conversion

### bigdataviewer-biop-tools
- **Total Commands**: ~70
- **Fully Documented**: ~65
- **Partially Documented**: ~3
- **Needs Review**: ~2
- **Coverage**: ~93%
- **Key Features**: GPU deconvolution, registration workflows (Warpy), LLS7 support, image fusion, elliptical transforms, interactive selection tools

---

## Current Documentation Structure

```
docs/source/
├── index.rst                    # Homepage
├── contents.rst                 # Master TOC
├── installation/
│   └── installation.md
├── opening_images/
│   └── opening_images.md        # Well documented (image-loaders + playground)
├── visualizing_images/
│   └── visualizing_images.md    # Partially documented
├── processing_images/
│   └── processing_images.md     # Minimal placeholder
└── commands/
    ├── index.md                 # Commands overview
    ├── viewers.md               # BDV/BVV window commands
    ├── sources_display.md       # Add/remove sources
    ├── sources_appearance.md    # Colors, LUTs, brightness
    ├── transformations.md       # Basic transforms, resampling
    ├── bigwarp.md               # BigWarp launcher
    ├── navigation_overlays.md   # Sliders, crosses, overlays
    ├── synchronization.md       # View/state sync
    ├── import_export.md         # Import/export commands
    ├── organizing_sources.md    # Groups, metadata
    └── state_management.md      # Save/load state, cache
```

---

## Identified Gaps

### Missing from Documentation (biop-tools)

#### 1. Registration Workflow (12 commands)
- `PairRegistrationCreateCommand` - Create registration pairs
- `PairRegistrationAddGUICommand` - Interactive registration GUI
- `PairRegistrationCenterCommand` - Center moving over fixed
- `PairRegistrationSift2DAffineCommand` - SIFT-based 2D affine
- `PairRegistrationElastix2DAffineCommand` - Elastix 2D affine
- `PairRegistrationElastix2DSplineCommand` - Elastix B-spline deformable
- `PairRegistrationBigWarp2DSplineCommand` - Manual landmark spline
- `PairRegistrationEditLastRegistrationCommand` - Edit last step
- `PairRegistrationRemoveLastRegistrationCommand` - Remove last step
- `PairRegistrationExportToOMETIFFCommand` - Export registered images
- `PairRegistrationExportToQuPathCommand` - Export to QuPath

#### 2. GPU Deconvolution (1 command + infrastructure)
- `SourcesDeconvolverCommand` - Richardson-Lucy GPU deconvolution
- CLIJ2-FFT backend, tiled processing, multi-GPU support

#### 3. Image Fusion & Export (3 commands)
- `FuseBigStitcherDatasetIntoOMETiffCommand` - Fuse to OME-TIFF
- `ExportToImagePlusCommand` - Export to ImagePlus
- `ExportToMultipleImagePlusCommand` - Export preserving locations

#### 4. Special Dataset Support (5 commands)
- `LLS7OpenDatasetCommand` - Zeiss LLS7 with live deskewing
- `LLS7CropCommand` - Crop 3D from LLS7
- `OpenOperettaDatasetCommand` - PerkinElmer Operetta
- `OpenImarisCommand` - Imaris .ims files
- `CreateCZIDatasetCommand` - CZI to BigStitcher XML

#### 5. Elliptical/Advanced Transforms (8 commands)
- `Elliptic3DTransformCreatorCommand` - Create elliptical transform
- `Elliptic3DTransformerCommand` - Apply elliptical transform
- `Elliptic3DTransformExporterCommand` - Export to JSON
- `Elliptic3DTransformImporterCommand` - Import from JSON
- `Optimize3DEllipticalTransformCommand` - Optimize parameters
- `DisplayEllipseFromTransformCommand` - Visualize ellipsoid
- `ExportEllipticProjection` - Export projection
- `Rotation3DTransformCommand` - Interactive 3D rotation

#### 6. Interactive Selection Tools (3 commands)
- `GetUserPointsCommand` - Interactive point selection
- `GetUserRectangleCommand` - Interactive rectangle selection
- `BoxSelectorCommand` - Interactive 3D box selection

#### 7. Source Manipulation (8 commands)
- `FilterSourcesByNameCommand` - Filter by name pattern
- `SourceTimeShiftCommand` - Time-shifted sources
- `SourcesPyramidizerCommand` - Generate pyramid levels
- `SourcesMakeModelCommand` - Create spanning model
- `SliceSourceCommand` - Oblique slice resampling
- `SourceSetAlphaCommand` - Alpha blending
- `SourcesFuserAndResamplerCommand` - Fuse and resample

#### 8. BDV View Export (3 commands)
- `BdvViewToImagePlusExportCommand` - Export current view
- `BasicBdvViewToImagePlusExportCommand` - Simple view export
- `OverviewerCommand` - Overview visualization

---

## Proposed New Structure

```
docs/source/
├── index.rst
├── contents.rst
├── installation/
│   └── installation.md
│
├── opening_images/
│   └── opening_images.md              # [KEEP] Well documented
│
├── visualizing_images/
│   └── visualizing_images.md          # [EXPAND] Add BDV view export
│
├── processing_images/                  # [MAJOR EXPANSION]
│   ├── index.md                       # Processing overview
│   ├── resampling.md                  # Resampling, pyramidization
│   ├── fusion.md                      # [NEW] Image fusion workflows
│   ├── deconvolution.md               # [NEW] GPU deconvolution guide
│   └── export_formats.md              # [NEW] OME-TIFF, ImagePlus export
│
├── registration/                       # [NEW SECTION]
│   ├── index.md                       # Registration overview
│   ├── concepts.md                    # Registration concepts
│   ├── manual_registration.md         # BigWarp (move from commands/)
│   ├── warpy_workflow.md              # [NEW] Complete Warpy guide
│   ├── automated_registration.md      # [NEW] SIFT, Elastix
│   └── exporting_results.md           # [NEW] Export to QuPath/OME-TIFF
│
├── special_datasets/                   # [NEW SECTION]
│   ├── index.md                       # Overview of special formats
│   ├── lls7_lattice.md                # [NEW] LLS7 workflow
│   ├── operetta.md                    # [NEW] Operetta datasets
│   ├── imaris.md                      # [NEW] Imaris files
│   └── bigstitcher_czi.md             # [NEW] CZI to BigStitcher
│
├── advanced_transforms/                # [NEW SECTION]
│   ├── index.md                       # Transform concepts
│   ├── elliptical_transforms.md       # [NEW] Elliptical 3D transforms
│   ├── rotation_3d.md                 # [NEW] 3D rotation tools
│   └── oblique_slicing.md             # [NEW] Oblique slice extraction
│
├── interactive_tools/                  # [NEW SECTION]
│   ├── index.md                       # Interactive tools overview
│   ├── point_selection.md             # [NEW] Point selection
│   ├── region_selection.md            # [NEW] Rectangle, 3D box
│   └── manual_transforms.md           # Manual transform mode
│
└── commands/                           # [KEEP] Reference section
    ├── index.md
    ├── viewers.md
    ├── sources_display.md
    ├── sources_appearance.md
    ├── transformations.md
    ├── navigation_overlays.md
    ├── synchronization.md
    ├── import_export.md
    ├── organizing_sources.md
    ├── state_management.md
    └── biop_tools_reference.md        # [NEW] biop-tools command reference
```

---

## Implementation Phases

### Phase 1: Foundation (Priority: High)
1. Create `docs/reference_documents/bigdataviewer-biop-tools-commands.md` - Raw command reference
2. Update `contents.rst` with new section placeholders
3. Create index pages for new sections

### Phase 2: Registration Documentation (Priority: High)
*Note: May need refactoring based on actual workflow*
1. Create `registration/` section
2. Document Warpy workflow end-to-end
3. Move BigWarp content from commands/ to registration/
4. Add SIFT and Elastix automated registration guides

### Phase 3: Processing Expansion (Priority: High)
1. Expand `processing_images/` with fusion documentation
2. Add GPU deconvolution guide with requirements
3. Document export formats (OME-TIFF, ImagePlus)

### Phase 4: Special Datasets (Priority: Medium)
1. Create `special_datasets/` section
2. Document LLS7 workflow (deskewing, cropping)
3. Add Operetta, Imaris, CZI guides

### Phase 5: Advanced Features (Priority: Medium)
1. Create `advanced_transforms/` section
2. Document elliptical transforms with use cases
3. Add 3D rotation and oblique slicing guides

### Phase 6: Interactive Tools (Priority: Low)
1. Create `interactive_tools/` section
2. Document point/region selection workflows
3. Integrate with registration and processing sections

---

## Content Guidelines

### For Each New Page

1. **Introduction**: What the feature does and when to use it
2. **Prerequisites**: Required update sites, dependencies
3. **Step-by-step workflow**: With screenshots/figures
4. **Command Reference**: Table with parameters
5. **Troubleshooting**: Common issues and solutions
6. **See Also**: Links to related documentation

### Screenshots Needed

Mark with `<!-- TODO:MISSING_CONTENT: [type: screenshot] - description -->` for:
- Registration GUI interface
- Deconvolution dialog and results
- LLS7 deskewing visualization
- Elliptical transform visualization
- Interactive selection tools in action

---

## Cross-Repository Coordination

### Source Files to Reference

When writing documentation, reference these files for accurate command information:

| Repository | Status File |
|------------|-------------|
| bigdataviewer-playground | `DOCUMENTATION_STATUS.md` |
| bigdataviewer-image-loaders | `DOCUMENTATION_STATUS.md` |
| bigdataviewer-biop-tools | `DOCUMENTATION_STATUS.md` |

### Keeping Documentation Synchronized

1. When commands are added/modified in source repos, update `DOCUMENTATION_STATUS.md`
2. Periodically review status files to identify new commands needing documentation
3. Use consistent naming between source @Plugin descriptions and documentation

---

## Notes for Registration Section

The registration section will need refactoring because:
- Current BigWarp documentation is in `commands/bigwarp.md`
- Warpy workflow builds on BigWarp but adds automation
- Need to decide if BigWarp stays in commands/ or moves to registration/
- Consider user journey: simple manual → semi-automated → fully automated

Suggested approach:
1. Keep `commands/bigwarp.md` as command reference
2. Create `registration/manual_registration.md` as tutorial that references bigwarp.md
3. Build Warpy documentation on top of this foundation

---

## Timeline Considerations

No specific timeline - work incrementally based on:
- User questions and feedback
- Feature usage statistics
- Contributor availability

Priority order based on user impact:
1. Registration (Warpy) - commonly requested
2. Deconvolution - unique GPU feature
3. LLS7 support - specific user base
4. Advanced transforms - power users

---

*Document created: 2025-12-29*
*Based on analysis of: bigdataviewer-playground, bigdataviewer-image-loaders, bigdataviewer-biop-tools*
