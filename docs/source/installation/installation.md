# Installation

This guide covers how to install and set up BigDataViewer Playground in Fiji.

(system-requirements)=

## System Requirements

- **Fiji**: a recent download from [fiji.sc](https://fiji.sc/) — see the note below
- **Java**: Java 8 or higher (bundled with Fiji)
- **Memory**: 8+ GB recommended
- **GPU** (optional): OpenCL-compatible GPU for deconvolution features

:::{important}
BigDataViewer Playground requires the **latest** Fiji distribution. The older *Fiji stable*
distribution is **not** supported — the components shipped by the update site will not run there.
Download a fresh Fiji from [fiji.sc](https://fiji.sc/) if you are unsure which one you have.
:::

## Quick Installation

### Step 1: Download Fiji

Download the latest Fiji from [fiji.sc](https://fiji.sc/) and extract it to your preferred location.

### Step 2: Add the UNIGE-Biochem Update Site

1. Open Fiji
2. Go to `Help > Update...`
3. Click `Manage update sites`
4. Find and check **UNIGE-Biochem** in the list
5. Click `Close`
6. Click `Apply changes`
7. Restart Fiji

That's it! BigDataViewer Playground is now installed, together with the automated registration
tools (Elastix/Transformix) — nothing else to download or configure.

---

## Optional Components

(gpu-deconvolution-clij)=

### GPU Deconvolution (CLIJ)

For GPU-accelerated deconvolution, add the CLIJ update sites:

1. Go to `Help > Update... > Manage update sites`
2. Check the following sites:
   - **clij**
   - **clij2**
   - **clijx-deconvolution**
3. Click `Close`, then `Apply changes`
4. Restart Fiji

:::{note}
GPU deconvolution requires an OpenCL-compatible graphics card. See [Deconvolution](../processing_images/deconvolution.md) for details.
:::

(fast-czi-file-reading)=

### Fast CZI File Reading

For improved performance when working with Zeiss CZI files:

1. Go to `Help > Update... > Manage update sites`
2. Check **Quick Start CZI Reader**
3. Click `Close`, then `Apply changes`
4. Restart Fiji

Check that the new reader will be picked up:

1. Go to `Plugins › Bio-Formats › Bio-Formats Plugins Configuration`
2. In the second tab named `Formats`, navigate to the bottom of the list, click `Zeiss CZI (Quick Start)` and make sure that it is enabled

This significantly speeds up opening and navigating large CZI datasets.

(elastix-installation)=

### Elastix/Transformix (Automated Registration)

Nothing to install. The first time a registration command needs it, Fiji uses
[Appose](https://github.com/apposed/appose) to build a self-contained environment providing
[itk-elastix](https://github.com/InsightSoftwareConsortium/ITKElastix), on Windows, macOS and
Linux alike. There is nothing to download by hand, no path to configure and no system library
to add.

Building that environment happens once and takes a few minutes, so the first registration you
run is slower than the following ones. Make sure you are online the first time.

---

## Summary of Update Sites

| Update Site                      | Purpose                                          | Required? |
|----------------------------------|--------------------------------------------------|-----------|
| **UNIGE-Biochem**                | Core BigDataViewer Playground + registration tools | Yes       |
| clij, clij2, clijx-deconvolution | GPU deconvolution                                | Optional  |
| Quick Start CZI Reader           | Fast CZI file handling                           | Optional  |

---

## Troubleshooting

### Commands Are Missing After Installing

- Make sure you are running the **latest** Fiji, not *Fiji stable* — see [System Requirements](#system-requirements)
- Re-run `Help > Update...` and confirm **UNIGE-Biochem** is still checked
- Restart Fiji after applying changes

### Elastix Not Working

- Check that you have a working internet connection the first time a registration runs — Appose
  builds the itk-elastix environment on demand
- Check the Fiji console for specific error messages
