# Undocumented Commands

This file tracks commands from `sc.fiji:bigdataviewer-playground:0.13.0` that are not included in the user documentation.

## Excluded Commands

### Test Commands

These are development/testing commands not intended for end users:

| Command | Class | Reason |
|---------|-------|--------|
| Test Interactive Command | `sc.fiji.bdvpg.scijava.command.TestInteractiveCommand` | Testing only |
| Test Widget Demo | `sc.fiji.bdvpg.scijava.command.TestWidgetDemoCommand` | Widget demonstration |

### Internal/Service Commands

These are internal commands used by the service infrastructure:

| Command | Class | Reason |
|---------|-------|--------|
| Clear Service | `sc.fiji.bdvpg.scijava.command.ClearSourceAndConverterService` | Destructive internal operation |
| Select BDV Window | `sc.fiji.bdvpg.scijava.command.bdv.BdvSelectCommand` | UI helper, not user action |

### Debug Commands

These commands are for debugging and development:

| Command | Class | Reason |
|---------|-------|--------|
| Debug Overlay | `sc.fiji.bdvpg.scijava.command.bdv.BdvDebugOverlayAdderCommand` | Debug tool |
| View Logger | `sc.fiji.bdvpg.scijava.command.bdv.BdvViewLoggerCommand` | Debug logging |

### Unknown/Unclear Commands

These commands need clarification about their purpose and user relevance:

| Command | Class | Notes |
|---------|-------|-------|
| BigDataBrowser Plugin | `sc.fiji.bdvpg.scijava.command.spimdata.BigDataBrowserPlugInCommand` | Purpose unclear - possibly deprecated |

### Developer-Focused Commands

These commands are primarily for scripting/development rather than interactive use:

| Command | Class | Reason |
|---------|-------|--------|
| Transformed Source Wrapper | `sc.fiji.bdvpg.scijava.command.source.TransformedSourceWrapperCommand` | Low-level wrapper operation |
| New Source | `sc.fiji.bdvpg.scijava.command.source.NewSourceCommand` | Creates empty sources - advanced use |
| Sample Source Creator | `sc.fiji.bdvpg.scijava.command.source.SampleSourceCreatorCommand` | Creates sample data - testing/demo |

---

## Commands Documentation Status

### Documented (40 commands)

#### Viewers (11 commands)
- [x] BdvCreatorCommand
- [x] BdvOrthoCreatorCommand
- [x] BvvWindowCreatorCommand
- [x] BvvOrthoWindowCreatorCommand
- [x] BdvDefaultViewerSetterCommand
- [x] BdvTitleSetterCommand
- [x] RenameBdv (mentioned as duplicate)
- [x] BdvSettingsCommand
- [x] MultiBdvTimepointsSetterCommand
- [x] MultiBdvTimepointAdapterCommand
- [x] BvvSetTimepointsNumberCommand
- [x] MultiBdvCloseCommand

#### Sources Display (11 commands)
- [x] BdvSourcesShowCommand
- [x] BdvSourcesAdderCommand
- [x] BdvSourcesRemoverCommand
- [x] MultiBdvSourcesAdderCommand
- [x] MultiBdvSourcesRemoverCommand
- [x] BvvSourcesAdderCommand
- [x] BvvSourcesRemoverCommand
- [x] SourcesDuplicatorCommand
- [x] SourcesRemoverCommand
- [x] SourcesVisibleMakerCommand
- [x] SourcesInvisibleMakerCommand

#### Sources Appearance (5 commands)
- [x] SourceColorChangerCommand
- [x] ColorSourceCreatorCommand
- [x] LUTSourceCreatorCommand
- [x] BrightnessAdjusterCommand
- [x] InteractiveBrightnessAdjusterCommand

#### Transformations (4 commands)
- [x] BasicTransformerCommand
- [x] SourceTransformerCommand
- [x] ManualTransformCommand
- [x] SourcesResamplerCommand

#### BigWarp (1 command)
- [x] BigWarpLauncherCommand

#### Navigation & Overlays (6 commands)
- [x] BdvViewAdjustOnSourcesCommand
- [x] BdvViewTransformatorCommand
- [x] MultiBdvCrossAdderCommand
- [x] MultiBdvSourceNameOverlayAdderCommand
- [x] MultiBdvZSliderAdderCommand
- [x] MultiBdvSourceNavigatorSliderAdderCommand

#### Synchronization (2 commands)
- [x] ViewSynchronizerCommand
- [x] StateSynchronizerCommand

#### Import/Export (4 commands)
- [x] MultipleSpimDataImporterCommand
- [x] SpimdataBigDataServerImportCommand
- [x] SpimDataExporterCommand
- [x] XmlHDF5ExporterCommand

#### Organizing (3 commands)
- [x] MakeGroupCommand
- [x] MakeMetadataFilterNodeCommand
- [x] AddMetadataCommand

#### State Management (4 commands)
- [x] ShowSourceAndConverterServiceWindow
- [x] SaveSourceAndConverterServiceState
- [x] LoadSourceAndConverterServiceState
- [x] CacheOptionsCommand

### Not Documented (10 commands)

- [ ] TestInteractiveCommand (test)
- [ ] TestWidgetDemoCommand (test)
- [ ] ClearSourceAndConverterService (internal)
- [ ] BdvSelectCommand (UI helper)
- [ ] BdvDebugOverlayAdderCommand (debug)
- [ ] BdvViewLoggerCommand (debug)
- [ ] BigDataBrowserPlugInCommand (unclear)
- [ ] TransformedSourceWrapperCommand (developer)
- [ ] NewSourceCommand (advanced)
- [ ] SampleSourceCreatorCommand (demo)

---

## Notes for Future Documentation

### Commands that might benefit from documentation later:

1. **NewSourceCommand** - Could be useful for advanced users creating synthetic data or masks
2. **TransformedSourceWrapperCommand** - Relevant for scripting tutorials
3. **BdvViewLoggerCommand** - Could be useful for reproducibility documentation

### Questions to resolve:

1. Is `BigDataBrowserPlugInCommand` still maintained/relevant?
2. Should debug tools be documented for power users?
3. Are there plans for new commands in future versions?

---

*Last updated: Document creation*
*Based on: sc.fiji:bigdataviewer-playground:0.13.0*
