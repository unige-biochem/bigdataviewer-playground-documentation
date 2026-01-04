# PSF Acquisition for LLS7 Deconvolution

This guide explains how to acquire and process a Point Spread Function (PSF) for deconvolving LLS7 lattice light-sheet data.

## Why a Proper PSF Matters

For optimal deconvolution results, the PSF must:
- Be acquired on the **same microscope** as your data
- Be in the **same skewed geometry** as the raw LLS7 data
- Match the **wavelength** of your fluorophores
- Use the **same acquisition settings** (Z-spacing, etc.)

Since the LLS7 always acquires a skewed plane, **the PSF must be measured in 3D** using beads embedded in a gel.

## Quick Option: Pre-measured PSFs

If you cannot acquire your own PSF, BIOP provides pre-measured PSFs from their LLS7 system:

**Download from Zenodo**: [https://zenodo.org/records/11396388](https://zenodo.org/records/11396388)

Available Z-spacings:
- 200 nm
- 300 nm
- 400 nm

:::{warning}
Pre-measured PSFs from a different system may not perfectly match your microscope's optical properties. For best results, acquire your own PSF.
:::

---

## Sample Preparation

### Materials

| Item | Specification | Notes |
|------|---------------|-------|
| Agarose | 2% solution | Keep warm at 90°C |
| Fluorescent beads | 200 nm diameter | [ThermoFisher F8811](https://www.thermofisher.com/order/catalog/product/F8811) |
| Bead stock dilution | 1000× | |
| PBS | Standard | For dilution |
| Slide | Clean glass slide | |
| Coverslip | 22×22 mm, clean | |
| Nail polish | Clear | For sealing |

### Protocol

1. **Warm the agarose** at 90°C until liquid

2. **Prepare bead dilution**:
   - Vortex the bead stock thoroughly
   - Dilute 100× in PBS (10 µL beads in 1 mL PBS)
   - Vortex again

3. **Mix agarose with beads**:
   - Take 90 µL of warm agarose into a 1.5 mL tube
   - Add 10 µL of the diluted beads
   - Vortex to mix

4. **Mount the sample**:
   - Pipette 50 µL of the agarose-bead mixture onto a clean slide
   - Immediately place the coverslip on top
   - Refrigerate for a few minutes to solidify

5. **Seal the sample**:
   - Apply nail polish around the coverslip edges
   - Wait for nail polish to dry completely

The resulting gel should be approximately **100 µm thick**.

:::{tip}
**Focusing aid**: Consider adding a small amount of free far-red dye (e.g., Alexa 647) to the gel. This helps with focusing the light sheet during imaging.
:::

---

## Imaging the Beads

### Acquisition Settings

| Parameter | Value |
|-----------|-------|
| Number of slices | ~500 |
| Z-spacing | 0.2 µm |
| Same objective as experiments | Required |
| Same laser wavelength as experiments | Required |

Acquire Z-stacks of isolated beads. Ensure beads are well-separated from each other.

Example raw bead stacks are available at: [https://zenodo.org/records/11396388](https://zenodo.org/records/11396388)

---

## PSF Analysis

Computing the PSF from bead images involves three steps:

### Step 1: Crop the Stack

Crop the bead image stack to a manageable size:
- **256 × 256 × 128** pixels (X × Y × Z) is typically sufficient

### Step 2: Detect Bead Centers

Use the **DetectBeads** script to find bead positions and generate a "points" image:

```{code-block} imagej-groovy
:caption: DetectBeads.groovy

// DetectBeads script
// Detects center positions of beads in a 3D stack
// Source: https://gist.github.com/NicoKiaru/5371ff696d34a5d87d6e2bf8249e7c5b
```

**Full script**: [DetectBeads.groovy on GitHub Gist](https://gist.github.com/NicoKiaru/5371ff696d34a5d87d6e2bf8249e7c5b)

### Step 3: Compute the PSF (Distillation)

Use the **ComputePSF** script to solve the deconvolution problem:

```
points ⊗ PSF = bead_image
```

This "distillation" process extracts the average PSF from multiple beads.

```{code-block} imagej-groovy
:caption: ComputePSF.groovy

// ComputePSF script
// Computes PSF by solving: points convolved by PSF = bead image
// Source: https://gist.github.com/NicoKiaru/7769f139c988dbdabc3f5dc5f0120daa
```

**Full script**: [ComputePSF.groovy on GitHub Gist](https://gist.github.com/NicoKiaru/7769f139c988dbdabc3f5dc5f0120daa)

---

## Using the PSF

Once you have computed your PSF, load it into BigDataViewer Playground:

---

## Summary

| Step | Action | Output |
|------|--------|--------|
| 1 | Prepare agarose gel with beads | Sample ready for imaging |
| 2 | Acquire Z-stack (~500 slices, 0.2 µm) | Raw bead images |
| 3 | Crop stack (256×256×128) | Manageable data size |
| 4 | Run DetectBeads script | Points image |
| 5 | Run ComputePSF script | Final PSF |

---

## Additional Resources

- [BIOP LLS7 Equipment Page](https://www.epfl.ch/research/facilities/ptbiop/equipment/lattice-lightsheet-7/)
- [Lattice Light Sheet User Meeting Report 2023](https://go.epfl.ch/lls7)
- [Pre-measured PSFs on Zenodo](https://zenodo.org/records/11396388)
- [DetectBeads Script](https://gist.github.com/NicoKiaru/5371ff696d34a5d87d6e2bf8249e7c5b)
- [ComputePSF Script](https://gist.github.com/NicoKiaru/7769f139c988dbdabc3f5dc5f0120daa)

---

## Related Topics

- [LLS7 Timelapse Workflow](lls7_timelapse.md) - Complete processing workflow
- [Installation](../installation/installation.md) - Required update sites
