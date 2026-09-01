# BUMP_DOC.md — moving the docs to a new upstream release

Runbook for retargeting this documentation at a new `ch.epfl.biop:bigdataviewer-biop-tools`
release. Read `CLAUDE.md` first for the toolchain paths, the CLI invocation and the page
conventions; this file is only the procedure.

Throughout, `<NEW>` is the new release (e.g. `0.23.0`) and `<OLD>` the one currently tracked
by the **Current Version** section of `CLAUDE.md`.

Check what is actually released before starting — do not assume the next number exists:

```bash
curl -s -L "https://maven.scijava.org/content/groups/public/ch/epfl/biop/bigdataviewer-biop-tools/maven-metadata.xml" | grep -E "<latest>|<release>"
```

`<release>` is the newest non-SNAPSHOT version. Use that.

---

## 1. Generate the CLI outputs for `<NEW>`

Create `cli-outputs/<NEW>/` and generate, for **both** packages `sc.fiji.bdvpg` and
`ch.epfl.biop`:

- `snapshot-<package>.json`
- `tree-<package>.txt`

then diff `<OLD>` against `<NEW>` into `cli-outputs/<NEW>/diff-<package>.json`.

The invocation, its mandatory flags and the jgo gotchas are in **CLAUDE.md → CLI Introspection
Tool**. The `diff` subcommand takes two snapshot paths and needs no `+` dependency.

Capture the payload without corrupting it — the CLI writes results to stdout and logging to
stderr, so discard stderr and write the bytes yourself rather than using shell redirection:

```powershell
$o = jgo --lenient --class-path-only $ep snapshot $pkg 2>$null
[IO.File]::WriteAllText($path, ($o -join "`n") + "`n", (New-Object Text.UTF8Encoding $false))
```

> **Regenerate a whole version directory with one tool build.** Snapshots produced by
> different `scijava-introspect` builds are not comparable: a diff taken across a tool change
> reports parameter additions that no upstream release actually made. If the tool itself
> changed since `<OLD>` was generated, re-run `<OLD>` too, then recompute its diff.

## 2. Read the diff before touching any page

For each package, report added / removed / modified commands, then classify:

| Diff entry | Action |
|---|---|
| **added** | Needs a new section or page. Pull the parameter table from the new snapshot. |
| **modified** | Run `describe-command` against **both** versions, identify exactly which parameters changed, update that command's table. |
| **removed** | Mark the section deprecated, or delete it. |
| **unchanged** | Nothing to do. |

Then check whether each affected command is referenced in `docs/source/**/*.md` at all — many
commands are not documented yet, so a change may need no work. Grep by class name, not by
menu label.

Agree the resulting plan before editing pages.

## 3. Update the pages

Follow **CLAUDE.md → Multi-language code tabs** exactly: parameter table and admonitions above
the tab-set, four tabs (GUI / IJ Macro / Groovy / Python), `imagej-groovy` fence for Groovy,
`:::::`/`::::` nesting, grids outside the tab-set.

Class names and parameter names come from `cli-outputs/<NEW>/snapshot-*.json` — look them all
up in a single pass, per **CLAUDE.md → Looking Up Command Signatures**.

## 4. Regenerate the command dialog screenshots

Every GUI tab carries a PNG of the real dialog, in `docs/source/command_dialogs/`. They are
generated offscreen by the **`scijava-screenshots`** skill — read its `SKILL.md` for the tool
itself; this is the invocation for these docs.

**Only re-shoot what the diff changed.** A command whose parameters did not move produces the
same PNG, so the usual bump touches a handful of files, not all 68. A full regeneration is only
needed when the theme or the tool changes.

Build the classpath from a throwaway Maven project pinned to `<NEW>`, **not** from a local
`bigdataviewer-biop-tools` checkout — a working tree is normally a `-SNAPSHOT` ahead of the
release the docs claim to document:

```bash
# pom.xml with the single dependency ch.epfl.biop:bigdataviewer-biop-tools:<NEW>,
# plus com.formdev:flatlaf and the scijava.public repository
mvn -B -q dependency:build-classpath -Dmdep.outputFile=cp.txt
tr '\\' '/' < cp.txt > cp_fwd.txt
printf -- '-cp "%s"\n' "$(cat cp_fwd.txt)" > args.txt
javac -nowarn @args.txt -d shot-classes ~/.claude/skills/scijava-screenshots/ShotCommands.java
printf -- '-cp "shot-classes;%s"\n' "$(cat cp_fwd.txt)" > runargs.txt

java -Dscijava.log.level=error --add-opens=java.base/java.lang=ALL-UNNAMED @runargs.txt \
  ShotCommands --out docs/source/command_dialogs --theme dark --scale 2 \
  --only "<Class>=<slug>,<Class>=<slug>,..."
```

`-Dscijava.log.level=error` matters: at the default level the SciJava event bus buries the
tool's own `OK` / `FAIL` lines under thousands of DEBUG lines.

**Naming.** The slug is the tool's own derivation from the class name
(`SourcesFuseAndResampleCommand` → `sources-fuse-and-resample`). Get the exact pairs from
`ShotCommands --list`, which prints `slug<TAB>class<TAB>dialog title` — never hand-write them.
One shared directory rather than the per-section `images/` dirs, so a command documented on two
pages has one file and a regeneration is a single command.

**Referencing.** In the GUI tab, one blank line under the `{menuselection}` line:

```markdown
![<dialog title> dialog](../command_dialogs/<slug>.png)
```

The alt text is the dialog title from `--list`. Every page with GUI tabs is one level below
`docs/source/`, so `../` is always right.

**Commands with no dialog.** 24 of the documented commands take only `SourceAndConverter[]` or
`BdvHandle`, which are filled from context and have no widget — their dialog is an empty box
with OK/Cancel. They get no screenshot and their GUI tab keeps the menu path alone. The tell is
the image height: a parameter-less dialog comes out exactly 240px tall at `--scale 2`. Do not
threshold above that — `Source - Set Color` is only 246px and is a real dialog.

To find which classes a page needs, take the first `sc.fiji.bdvpg`/`ch.epfl.biop` `Command`
import inside each `{tab-set}`. A GUI-only section has no scripting tab; match the last segment
of its `{menuselection}` path against the dialog title from `--list` instead.

Check the PNGs afterwards. The defect this catches most often is an HTML message parameter with
no width constraint, which Swing renders with huge blank bands — fix it in the command, not
here, per the skill's **Reviewing the output**.

## 5. Update the version references

- `docs/source/conf.py`: `version` and `release` to `<NEW>`.
- `docs/source/conf.py`: the `extlinks` version strings — `_bdvpg_version`,
  `_biop_bdv_tools_version`, `_bdv_image_loaders_version`, `_bdvpg_display_version`,
  `_ijp_kheops_version`.

  **These do not move in lockstep with `bigdataviewer-biop-tools`.** At 0.21.0 they were
  0.21.0, 0.21.0, 0.21.1, 0.20.1 and 0.20.0 respectively. Read each companion version out of
  the `bigdataviewer-biop-tools:<NEW>` POM (or its parent's properties) rather than guessing,
  and confirm every resulting GitHub tag URL resolves — a wrong value produces a source link
  that 404s silently, which Sphinx will not catch:

  ```bash
  curl -s -o /dev/null -w "%{http_code}" -L "https://github.com/<org>/<repo>/blob/<repo>-<version>/"
  ```

- `CLAUDE.md`: the **Current Version** line.
- Anywhere else `<OLD>` is hardcoded: `grep -rn "<OLD>" --include=*.md --include=*.py .`

## 6. Build, verify, commit

```powershell
& "$env:LOCALAPPDATA\miniforge3\envs\bdvpg-documentation\python.exe" -m sphinx -b html `
  docs\source docs\build\html
```

The build must stay at **zero warnings**. If you added cross-page anchor links, verify the
generated `href` in `docs/build/html/` — see **CLAUDE.md → Editing Gotchas** for why a clean
build is not sufficient proof.

Commit the CLI outputs and the page updates together, so the snapshot that justifies a
parameter table lands with it.

## 7. Publish

`latest` on ReadTheDocs tracks `main`, so pushing publishes the update. For a frozen snapshot,
tag `<NEW>.0` (the 4-segment `MAJOR.MINOR.PATCH.DOC` scheme in **CLAUDE.md → Versioning /
tagging scheme**) and activate the tag once in the RTD admin Versions tab, or it will not
build.
