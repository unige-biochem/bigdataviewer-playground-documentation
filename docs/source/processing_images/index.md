# Processing Images

This section covers the commands for transforming, fusing, classifying, deconvolving, and managing your sources in BigDataViewer Playground.

A key principle: most processing in BigDataViewer Playground is **lazy**. When you fuse, resample, classify, or deconvolve sources, the result is a new virtual source — pixels are only computed when you look at them or export them. This means you can set up complex processing pipelines on terabyte-scale data without waiting for the whole volume to be computed.

All processing commands are found under:

{menuselection}`Plugins > BigDataViewer-Playground > Process`

```{toctree}
:maxdepth: 1

fuse_resample
pixel_classification
deconvolution
spatial_transforms
source_utilities
```