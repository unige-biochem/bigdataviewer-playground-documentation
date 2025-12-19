# Organizing Sources (Groups and Metadata)

As projects grow, managing many sources becomes challenging. BigDataViewer Playground provides tools to organize sources into groups and attach metadata for filtering and selection.

## The Source Tree

The SourceAndConverter Service window displays all sources in a tree structure. You can:
- **Group sources** logically (by sample, channel, condition, etc.)
- **Filter sources** based on metadata
- **Select multiple sources** for batch operations

<!-- TODO:MISSING_CONTENT: [type: screenshot] - SourceAndConverter service window showing organized tree structure -->

---

## Creating Groups

### Make a Group

**Command**: `Sources - Create group`
**Class**: `sc.fiji.bdvpg.scijava.command.source.MakeGroupCommand`

Creates a node in the source tree that selects a specific set of sources. Groups make it easy to work with related sources together.

**Parameters**:
| Parameter | Description |
|-----------|-------------|
| `sacs` | Source(s) to include in the group |
| `groupname` | Name for the new group |
| `displaysources` | Show sources when selecting the group |

<!-- TODO:MISSING_CONTENT: [type: screenshot] - Creating a group in the tree view -->

### Use Cases for Groups

| Group Type | Example |
|------------|---------|
| **By Sample** | "Sample_001", "Sample_002" |
| **By Channel** | "DAPI", "GFP", "mCherry" |
| **By Condition** | "Control", "Treatment_A", "Treatment_B" |
| **By Processing** | "Raw", "Registered", "Filtered" |

### Example: Organizing a Multi-Sample Experiment

```
Experiment/
├── Sample_001/
│   ├── DAPI
│   ├── GFP
│   └── RFP
├── Sample_002/
│   ├── DAPI
│   ├── GFP
│   └── RFP
└── All_DAPI/  (cross-sample group)
    ├── Sample_001_DAPI
    └── Sample_002_DAPI
```

<!-- TODO:MISSING_CONTENT: [type: script] - Groovy script creating an organized group structure -->

:::{tip}
Create both hierarchical groups (Sample > Channel) AND cross-cutting groups (All DAPI channels) for maximum flexibility.
:::

---

## Working with Metadata

### Add Metadata to Sources

**Command**: `Sources - Add metadata`
**Class**: `sc.fiji.bdvpg.scijava.command.source.AddMetadataCommand`

Attaches key-value metadata to sources. Metadata can later be used for filtering and selecting sources programmatically.

**Parameters**:
| Parameter | Description |
|-----------|-------------|
| `sacs` | Source(s) to tag |
| `key` | Metadata key (e.g., "channel", "sample", "treatment") |
| `value` | Metadata value (e.g., "DAPI", "Sample_001", "Control") |

<!-- TODO:MISSING_CONTENT: [type: screenshot] - Adding metadata to sources -->

### Common Metadata Keys

| Key | Example Values | Use |
|-----|---------------|-----|
| `channel` | "DAPI", "GFP", "Transmitted" | Filter by imaging channel |
| `sample` | "Sample_001", "Control_A" | Filter by sample ID |
| `treatment` | "Vehicle", "Drug_10uM" | Filter by experimental condition |
| `timepoint` | "T0", "T24h", "T48h" | Filter by time |
| `replicate` | "Rep1", "Rep2", "Rep3" | Filter by replicate |
| `quality` | "Good", "Poor", "Review" | Filter by QC status |

:::{note}
Metadata is stored with the source and can be saved/loaded with the session state.
:::

---

## Filtering by Metadata

### Create a Metadata Filter Node

**Command**: `Sources - Create metadata filter`
**Class**: `sc.fiji.bdvpg.scijava.command.source.MakeMetadataFilterNodeCommand`

Creates a dynamic node in the tree that automatically selects sources matching specific metadata criteria. Unlike static groups, filter nodes update automatically as sources are added or modified.

**Parameters**:
| Parameter | Description |
|-----------|-------------|
| `groupname` | Name for the filter node |
| `key` | Metadata key to filter on |
| `valueregex` | Regular expression to match values (`.*` matches everything) |

<!-- TODO:MISSING_CONTENT: [type: screenshot] - Metadata filter node in action -->

### Regular Expression Examples

| Pattern | Matches |
|---------|---------|
| `DAPI` | Exactly "DAPI" |
| `.*` | Everything (any value) |
| `Sample_00[1-3]` | "Sample_001", "Sample_002", "Sample_003" |
| `Control.*` | "Control", "Control_A", "Control_B" |
| `.*GFP.*` | Anything containing "GFP" |
| `^T[0-9]+$` | "T0", "T1", "T24", etc. |

### Dynamic Filtering

Filter nodes are **dynamic**:
1. Add new sources with matching metadata → they appear in the filter
2. Change source metadata → filter updates automatically
3. No need to manually update groups

:::{tip}
Use filter nodes for criteria that may change. Use static groups for fixed collections of sources.
:::

---

## Organizing Workflow

### Setting Up a Well-Organized Project

1. **Define your metadata schema** before importing:
   - What keys will you use?
   - What values are valid?

2. **Add metadata during/after import**:
   ```
   Import sources
   Add metadata: channel = "DAPI"
   Add metadata: sample = "Sample_001"
   Add metadata: treatment = "Control"
   ```

3. **Create filter nodes** for common selections:
   - "All DAPI" (key: channel, regex: DAPI)
   - "All Controls" (key: treatment, regex: Control)

4. **Create static groups** for specific analyses:
   - "Analysis_Set_1" containing specific sources

<!-- TODO:MISSING_CONTENT: [type: script] - Complete organization workflow script -->

---

## Practical Examples

### Multi-Channel Time-Lapse Organization

```
Metadata scheme:
- channel: DAPI, GFP, RFP
- timepoint: T00, T06, T12, T24

Filter nodes:
- "All DAPI" → channel = DAPI
- "All T24" → timepoint = T24
- "GFP time series" → channel = GFP
```

### Batch Processing Setup

When you need to process specific subsets:

1. Create filter node for the subset
2. Select the filter node (selects all matching sources)
3. Apply batch operation to selection

<!-- TODO:MISSING_CONTENT: [type: example] - Batch processing with filtered selection -->

---

## Tips for Effective Organization

1. **Be consistent**: Use the same metadata keys and value formats throughout
2. **Plan ahead**: Define your schema before starting
3. **Use prefixes**: "Sample_001" sorts better than "1_Sample"
4. **Document your schema**: Keep a reference of what keys and values mean
5. **Regular expressions**: Learn basic regex for powerful filtering

:::{warning}
Metadata keys and values are case-sensitive. "DAPI" and "dapi" are different values.
:::

---

## Summary

| Command | Purpose |
|---------|---------|
| `MakeGroupCommand` | Create static group of sources |
| `AddMetadataCommand` | Attach key-value metadata |
| `MakeMetadataFilterNodeCommand` | Create dynamic filter based on metadata |
