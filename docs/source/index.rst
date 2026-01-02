BigDataViewer Playground
========================

BigDataViewer Playground extends `BigDataViewer <https://imagej.net/plugins/bdv/>`_ with tools for manipulating, processing, and analyzing large-scale image data in Fiji.

**Key Features:**

* Multi-dimensional visualization (2D, 3D, time-series, multi-channel)
* Lazy loading for terabyte-scale datasets
* Registration workflows (BigWarp, Warpy, SIFT, Elastix)
* GPU-accelerated deconvolution
* Export to OME-TIFF, XML/HDF5, QuPath

**Getting Started:** Install via the :doc:`installation guide <installation/installation>`, then explore :doc:`opening images <opening_images/opening_images>`.

**Support:** `GitHub <https://github.com/bigdataviewer/bigdataviewer-playground>`_ · `Image.sc Forum <https://forum.image.sc/>`_

----

.. toctree::
   :maxdepth: 2
   :caption: Getting Started

   installation/installation
   opening_images/opening_images
   visualizing_images/visualizing_images

.. toctree::
   :maxdepth: 2
   :caption: Workflows

   workflows/index

.. toctree::
   :maxdepth: 2
   :caption: Processing & Analysis

   processing_images/index
   registration/index

.. toctree::
   :maxdepth: 2
   :caption: Advanced Topics

   special_datasets/index
   advanced_transforms/index
   interactive_tools/index

.. toctree::
   :maxdepth: 2
   :caption: Commands Reference

   commands/index
   commands/viewers
   commands/sources_display
   commands/sources_appearance
   commands/transformations
   commands/bigwarp
   commands/navigation_overlays
   commands/synchronization
   commands/import_export
   commands/organizing_sources
   commands/state_management
