# Installation

This guide covers how to install and set up BigDataViewer Playground in Fiji.

## System Requirements

- **Fiji**: Latest version recommended
- **Java**: Java 11 or higher (bundled with Fiji)
- **Memory**: 8 GB RAM minimum, 16+ GB recommended for large datasets
- **GPU** (optional): OpenCL-compatible GPU for deconvolution features

## Quick Installation

### Step 1: Download Fiji

Download Fiji from [fiji.sc](https://fiji.sc/) and extract it to your preferred location.

### Step 2: Add the PTBIOP Update Site

1. Open Fiji
2. Go to `Help > Update...`
3. Click `Manage update sites`
4. Find and check **PTBIOP** in the list
5. Click `Close`
6. Click `Apply changes`
7. Restart Fiji

That's it! BigDataViewer Playground is now installed.

---

## Optional Components

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

### Fast CZI File Reading

For improved performance when working with Zeiss CZI files:

1. Go to `Help > Update... > Manage update sites`
2. Check **Quick Start CZI Reader**
3. Click `Close`, then `Apply changes`
4. Restart Fiji

This significantly speeds up opening and navigating large CZI datasets.

### Elastix/Transformix (Automated Registration)

Elastix is required for automated 2D registration workflows. It must be installed separately from Fiji.

#### Download Elastix

1. Download elastix version 5.2.0 from [GitHub releases](https://github.com/SuperElastix/elastix/releases/tag/5.2.0)
2. Choose the version for your operating system
3. Extract to a convenient location (e.g., `C:\elastix` or `/opt/elastix`)

#### Platform-Specific Setup

**Windows:**
- Install the Visual C++ Redistributable from [Microsoft](https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist)
- Download and run `vc_redist.x64.exe` for 64-bit systems

**macOS:**
- You may need to allow the executables in Security settings
- See [Apple's guidance](https://support.apple.com/en-hk/guide/mac-help/mh40616/mac) for opening apps from unidentified developers

**Linux:**
- No additional setup required
- Ensure the executables have execute permissions: `chmod +x elastix transformix`

#### Configure in Fiji

1. Go to `Plugins > BIOP > Elastix > Test elastix`
2. Set the paths to the `elastix` and `transformix` executables
3. Click OK to verify the installation

Successful setup will show 3 windows with a successful registration.

---

## Summary of Update Sites

| Update Site                      | Purpose                       | Required? |
|----------------------------------|-------------------------------|-----------|
| **PTBIOP**                       | Core BigDataViewer Playground | Yes       |
| clij, clij2, clijx-deconvolution | GPU deconvolution             | Optional  |
| Quick Start CZI Reader           | Fast CZI file handling        | Optional  |

| External Tool       | Purpose                   | Required? |
|---------------------|---------------------------|-----------|
| Elastix/Transformix | Automated 2D registration | Optional  |

---

## Troubleshooting

### Elastix Not Working

- Verify paths point to the actual executables, not the folder
- On Windows, ensure Visual C++ Redistributable is installed
- On macOS, check Security & Privacy settings
- Check the Fiji console for specific error messages
