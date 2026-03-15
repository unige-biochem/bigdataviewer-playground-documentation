# Pixel Classification (Labkit)

Labkit integration lets you train a pixel classifier interactively and then apply it lazily to your full dataset. This is the recommended way to segment large images — you train on a small region, then the classifier is applied on-the-fly as you navigate or export.

All commands are found under:

{menuselection}`Plugins > BigDataViewer-Playground > Process > Classify (Labkit)`

---

## Source - Open Labkit

Opens the Labkit pixel classification GUI for the selected sources. Each source is treated as a separate channel input to the classifier.

{menuselection}`Plugins > BigDataViewer-Playground > Process > Classify (Labkit) > Source - Open Labkit`

| Parameter | Description |
|-----------|-------------|
| Select Source(s) | The sources to open in Labkit (each treated as a channel) |
| Resolution Level | Resolution level to use (0 = full resolution, higher = lower resolution) |

:::{tip}
For large datasets, start with a higher resolution level (e.g. 2 or 3) to train your classifier quickly. Once you're satisfied, apply it at full resolution using **Source - Apply Labkit Classifier**.
:::

---

## Source - Apply Labkit Classifier

Creates a lazy segmentation source by applying a previously saved Labkit classifier. The classification is computed on-the-fly — only the pixels you view or export are actually classified.

{menuselection}`Plugins > BigDataViewer-Playground > Process > Classify (Labkit) > Source - Apply Labkit Classifier`

| Parameter | Description |
|-----------|-------------|
| Select Source(s) | The sources to classify (each treated as a channel) |
| Classifier File | Path to the Labkit `.classifier` file |
| Resolution Level | Resolution level to use from input sources (0 = full resolution) |
| Output Name Suffix | Suffix appended to the source name for the classified output |
| Use GPU | Use GPU acceleration for classification (requires compatible GPU and OpenCL) |