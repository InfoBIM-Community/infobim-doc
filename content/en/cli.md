# CLI reference

Browse the `infobim` command line by component. Each command includes its syntax and accepted arguments.

<div class="cli-reference-summary" markdown="1">

**35 commands** · **9 components**

```text
infobim <command> [flags/parameters]
```

</div>

## Command index

<div class="cli-reference-index" markdown="1">

| Component | Description | Commands |
| --- | --- | ---: |
| [`2d`](#component-2d) | Launch the optional PySide6 2D viewer to open DXF/DWG drawings and pick points for annotations and IFC elements. | 2 |
| [`annotation`](#component-annotation) | Create, update, list, export and delete W3C-style annotations on an InfoBIM project, including picking points on a DXF drawing. | 8 |
| [`cli`](#component-cli) | Core entry points of the InfoBIM executable: initialize a workspace, run the local server and report the installed version. | 4 |
| [`context`](#component-context) | Inspect values held in the execution context dictionary. | 1 |
| [`dev`](#component-dev) | Delegate development commands, such as documentation generation, to the separate ontobdc-dev workspace CLI. | 1 |
| [`drawing`](#component-drawing) | Classify and extract semantic views from CAD drawings — viewports, titles, clusters, references and relationships — including DWG to DXF conversion. | 1 |
| [`ifc`](#component-ifc) | Report the health of a project's IFC models and create IFC elements at points picked on a DXF or DWG drawing. | 3 |
| [`project`](#component-project) | Create, attach, update, inspect and maintain InfoBIM projects and their entities. | 14 |
| [`run`](#component-run) | Run a finite-state machine on an InfoBIM project, from the YAML of its statechart. | 1 |

</div>


## 2d { #component-2d }


<div class="cli-reference-command" markdown="1">

### Base 2D command handler. { #component-2d-command-1 }

<div class="cli-reference-label">Syntax</div>

```bash
infobim 2d --help
```


| Argument | Description | Aliases | Value |
| --- | --- | --- | --- |
| `--help` | Print the status of the optional 2D stack and the tree of every 2D command registered in the active executable. | `-h` | No value |


</div>


<div class="cli-reference-command" markdown="1">

### Install the optional 2D viewer extra (PySide6 / Qt DXF viewer). { #component-2d-command-2 }

<div class="cli-reference-label">Syntax</div>

```bash
infobim 2d --enable
```


| Argument | Description | Aliases | Value |
| --- | --- | --- | --- |
| `--enable` | Install the optional InfoBIM 2D extra, which brings PySide6 and the Qt-backed interactive DXF viewer. Equivalent to manually running 'python -m pip install --upgrade 'infobim\[2d\]''. | — | No value |


</div>



## annotation { #component-annotation }


<div class="cli-reference-command" markdown="1">

### Base annotation component command handler. { #component-annotation-command-1 }

<div class="cli-reference-label">Syntax</div>

```bash
infobim annotation --help
```


| Argument | Description | Aliases | Value |
| --- | --- | --- | --- |
| `--help` | Print the tree of commands registered under the \`annotation\` logical component of InfoBIM. | `-h` | No value |


</div>


<div class="cli-reference-command" markdown="1">

### Empty optional fields of an annotation of an InfoBIM project. { #component-annotation-command-2 }

<div class="cli-reference-label">Syntax</div>

```bash
infobim annotation --global-id <value> --guid <value> --clear <value>
```


| Argument | Description | Aliases | Value |
| --- | --- | --- | --- |
| `--global-id` | Resolve the GlobalId of an IfcProject to the InfoBIM project that carries it, and to the container underneath it. | — | `str` |
| `--guid` | Global id of the annotation to change. | — | `str` |
| `--clear` | Field to empty: text, author or related. Repeat it for each field. | — | `str` |


</div>


<div class="cli-reference-command" markdown="1">

### Create an annotation of a given type in an InfoBIM project. { #component-annotation-command-3 }

<div class="cli-reference-label">Syntax</div>

```bash
infobim annotation --global-id <value> --type <value> --title <value> --related <value> --text <value> --author <value>
```


| Argument | Description | Aliases | Value |
| --- | --- | --- | --- |
| `--global-id` | Resolve the GlobalId of an IfcProject to the InfoBIM project that carries it, and to the container underneath it. | — | `str` |
| `--type` | Type of the annotation, by its IRI or by a label or identifier in any language, such as note, issue or question. Optional: a note when omitted. | — | `str` |
| `--title` | Title of the annotation. | — | `str` |
| `--related` | File of the container the annotation refers to, other than the one it was made on. Optional; repeat it for each file. | — | `Path` |
| `--text` | Text of the annotation. Optional. | — | `str` |
| `--author` | Author of the annotation. Optional. | — | `str` |


</div>


<div class="cli-reference-command" markdown="1">

### Remove an annotation of an InfoBIM project. { #component-annotation-command-4 }

<div class="cli-reference-label">Syntax</div>

```bash
infobim annotation --global-id <value> --guid <value> --delete
```


| Argument | Description | Aliases | Value |
| --- | --- | --- | --- |
| `--global-id` | Resolve the GlobalId of an IfcProject to the InfoBIM project that carries it, and to the container underneath it. | — | `str` |
| `--guid` | Global id of the annotation to remove. | — | `str` |
| `--delete` | Remove the annotation. | — | No value |


</div>


<div class="cli-reference-command" markdown="1">

### Export the annotations of one type of an InfoBIM project, as an Excel workbook. { #component-annotation-command-5 }

<div class="cli-reference-label">Syntax</div>

```bash
infobim annotation --global-id <value> --export <value> --type <value> --output <value> --language <value>
```


| Argument | Description | Aliases | Value |
| --- | --- | --- | --- |
| `--global-id` | Resolve the GlobalId of an IfcProject to the InfoBIM project that carries it, and to the container underneath it. | — | `str` |
| `--export` | Format of the export. The only one is: excel. | — | `str` |
| `--type` | Annotation type whose annotations are exported. | — | `str` |
| `--output` | Where to write the file. | — | `Path` |
| `--language` | Language of the words in the file (en, pt-br, es-es). | — | `str` |


</div>


<div class="cli-reference-command" markdown="1">

### List the annotations of an InfoBIM project, grouped by the annotation types the ontology declares. { #component-annotation-command-6 }

<div class="cli-reference-label">Syntax</div>

```bash
infobim annotation --global-id <value> --list
```


| Argument | Description | Aliases | Value |
| --- | --- | --- | --- |
| `--global-id` | Resolve the GlobalId of an IfcProject to the InfoBIM project that carries it, and to the container underneath it. | — | `str` |
| `--list` | List the annotations of the project, grouped by type. | — | No value |


</div>


<div class="cli-reference-command" markdown="1">

### Create an annotation of a given type at points picked on a DXF drawing of an InfoBIM project. { #component-annotation-command-7 }

<div class="cli-reference-label">Syntax</div>

```bash
infobim annotation --type <value> --point <value>
```


| Argument | Description | Aliases | Value |
| --- | --- | --- | --- |
| `--type` | Type of the annotation, by its IRI or by a label or identifier in any language, such as note, issue or question. | — | `str` |
| `--point` | Drawing on which the annotation points are picked. | — | `Path` |


</div>


<div class="cli-reference-command" markdown="1">

### Change the data of an annotation of an InfoBIM project, by its global id. { #component-annotation-command-8 }

<div class="cli-reference-label">Syntax</div>

```bash
infobim annotation --global-id <value> --guid <value> --type <value> --title <value> --text <value> --author <value> --related <value>
```


| Argument | Description | Aliases | Value |
| --- | --- | --- | --- |
| `--global-id` | Resolve the GlobalId of an IfcProject to the InfoBIM project that carries it, and to the container underneath it. | — | `str` |
| `--guid` | Global id of the annotation to change. | — | `str` |
| `--type` | New type of the annotation. | — | `str` |
| `--title` | New title of the annotation. | — | `str` |
| `--text` | New text of the annotation. | — | `str` |
| `--author` | New author of the annotation. | — | `str` |
| `--related` | File of the container the annotation refers to; repeat it for each file. They replace the related documents. | — | `Path` |


</div>



## cli { #component-cli }


<div class="cli-reference-command" markdown="1">

### Base CLI component command handler. { #component-cli-command-1 }

<div class="cli-reference-label">Syntax</div>

```bash
infobim --help
```


| Argument | Description | Aliases | Value |
| --- | --- | --- | --- |
| `--help` | Print the tree of commands registered under the \`cli\` logical component of InfoBIM. | `-h` | No value |


</div>


<div class="cli-reference-command" markdown="1">

### Initialize OntoBDC and InfoBIM in the current directory. { #component-cli-command-2 }

<div class="cli-reference-label">Syntax</div>

```bash
infobim init
```


</div>


<div class="cli-reference-command" markdown="1">

### Run the local InfoBIM server. { #component-cli-command-3 }

<div class="cli-reference-label">Syntax</div>

```bash
infobim serve
```


</div>


<div class="cli-reference-command" markdown="1">

### Display the version of InfoBIM. { #component-cli-command-4 }

<div class="cli-reference-label">Syntax</div>

```bash
infobim --version
```


| Argument | Description | Aliases | Value |
| --- | --- | --- | --- |
| `--version` | Print the version string reported by the active InfoBIM Python distribution installed in the current environment. | `-v` | No value |


</div>



## context { #component-context }


<div class="cli-reference-command" markdown="1">

### Inspect a value in the context dictionary. { #component-context-command-1 }

<div class="cli-reference-label">Syntax</div>

```bash
infobim context --term <value> --inspect
```


| Argument | Description | Aliases | Value |
| --- | --- | --- | --- |
| `--term` | Term or value to inspect in the context dictionary. | — | `str` |
| `--inspect` | Run the context dictionary inspection pipeline. | — | No value |


</div>



## dev { #component-dev }


<div class="cli-reference-command" markdown="1">

### Delegate dev commands to the ontobdc-dev workspace CLI. { #component-dev-command-1 }

<div class="cli-reference-label">Syntax</div>

```bash
infobim dev
```


</div>



## drawing { #component-drawing }


<div class="cli-reference-command" markdown="1">

### Base drawing component command handler. { #component-drawing-command-1 }

<div class="cli-reference-label">Syntax</div>

```bash
infobim drawing --help
```


| Argument | Description | Aliases | Value |
| --- | --- | --- | --- |
| `--help` | Print the tree of commands registered under the \`drawing\` logical component of InfoBIM. | `-h` | No value |


</div>



## ifc { #component-ifc }


<div class="cli-reference-command" markdown="1">

### Base IFC component command handler. { #component-ifc-command-1 }

<div class="cli-reference-label">Syntax</div>

```bash
infobim ifc --help
```


| Argument | Description | Aliases | Value |
| --- | --- | --- | --- |
| `--help` | Print the tree of commands registered under the \`ifc\` logical component of InfoBIM. | `-h` | No value |


</div>


<div class="cli-reference-command" markdown="1">

### Report the health of the IFC models of an InfoBIM project. { #component-ifc-command-2 }

<div class="cli-reference-label">Syntax</div>

```bash
infobim ifc --global-id <value> --health --ifc-model-path <value>
```


| Argument | Description | Aliases | Value |
| --- | --- | --- | --- |
| `--global-id` | Resolve the GlobalId of an IfcProject to the InfoBIM project that carries it, and to the container underneath it. | — | `str` |
| `--health` | Report, model by model, which verifications of the geometric health of an IFC model hold and why the others do not. | — | No value |
| `--ifc-model-path` | The one IFC model to report on. When omitted, every IFC model the project declares. | — | `Path` |


</div>


<div class="cli-reference-command" markdown="1">

### Create IFC elements of the kind a term names at points picked on a DXF or DWG drawing. { #component-ifc-command-3 }

<div class="cli-reference-label">Syntax</div>

```bash
infobim ifc --global-id <value> --term <value> --point <value> --ifc-model-path <value>
```


| Argument | Description | Aliases | Value |
| --- | --- | --- | --- |
| `--global-id` | Resolve the GlobalId of an IfcProject to the InfoBIM project that carries it, and to the container underneath it. | — | `str` |
| `--term` | Name of the element kind, in natural language. | — | `str` |
| `--point` | DXF or DWG drawing on which the element points are picked. | — | `Path` |
| `--ifc-model-path` | IFC model of the project to create the elements in. When omitted, the project's own model, named after its IfcProject GlobalId, created if it does not exist yet. | — | `Path` |


</div>



## project { #component-project }


<div class="cli-reference-command" markdown="1">

### Attach an imported InfoBIM project onto the current storage root. { #component-project-command-1 }

<div class="cli-reference-label">Syntax</div>

```bash
infobim project --project-path <value> --attach <value>
```


| Argument | Description | Aliases | Value |
| --- | --- | --- | --- |
| `--project-path` | Resolve an InfoBIM project path from \`--project-path\`, \`--project\`, or the current working directory to the project container underneath it. | `--project` | `Path` |
| `--attach` | Validate the project container's metadata, register it in the root storage index and then run the project refresh pipeline so datasets, manifests and RO-Crate agree with what the container actually holds. | — | `bool` |


</div>


<div class="cli-reference-command" markdown="1">

### Base project component command handler. { #component-project-command-2 }

<div class="cli-reference-label">Syntax</div>

```bash
infobim project --help
```


| Argument | Description | Aliases | Value |
| --- | --- | --- | --- |
| `--help` | Print the tree of commands registered under the \`project\` logical component of InfoBIM. | `-h` | No value |


</div>


<div class="cli-reference-command" markdown="1">

### Create a new InfoBIM Project with the given name. { #component-project-command-3 }

<div class="cli-reference-label">Syntax</div>

```bash
infobim project --create <value>
```


| Argument | Description | Aliases | Value |
| --- | --- | --- | --- |
| `--create` | Title of the new InfoBIM project to create. A filesystem slug is derived from this title and used as the container folder name; the pipeline then writes the container metadata, initializes the reserved InfoBIM dataset and registers the project in the storage index. | — | `str` |


</div>


<div class="cli-reference-command" markdown="1">

### Refresh an existing InfoBIM Project container. { #component-project-command-4 }

<div class="cli-reference-label">Syntax</div>

```bash
infobim project --global-id <value> --refresh
```


| Argument | Description | Aliases | Value |
| --- | --- | --- | --- |
| `--global-id` | Resolve the GlobalId of an IfcProject to the InfoBIM project that carries it, and to the container underneath it. | — | `str` |
| `--refresh` | Run the project refresh pipeline on the selected InfoBIM project. Refreshing rebuilds datasets, datapackage and RO-Crate from the files the project container actually holds; it never writes values into metadata fields (use \`project --update &lt;source&gt;\` instead). | — | No value |


</div>


<div class="cli-reference-command" markdown="1">

### Create a new dataset inside a selected InfoBIM Project. { #component-project-command-5 }

<div class="cli-reference-label">Syntax</div>

```bash
infobim project --global-id <value> --create-dataset <value>
```


| Argument | Description | Aliases | Value |
| --- | --- | --- | --- |
| `--global-id` | Resolve the GlobalId of an IfcProject to the InfoBIM project that carries it, and to the container underneath it. | — | `str` |
| `--create-dataset` | Title of the new dataset to create inside the selected project. When --global-id is omitted the project is resolved from the current working directory. | — | `str` |


</div>


<div class="cli-reference-command" markdown="1">

### Delete an InfoBIM Project from the index. { #component-project-command-6 }

<div class="cli-reference-label">Syntax</div>

```bash
infobim project --global-id <value> --delete <value>
```


| Argument | Description | Aliases | Value |
| --- | --- | --- | --- |
| `--global-id` | Resolve the GlobalId of an IfcProject to the InfoBIM project that carries it, and to the container underneath it. | — | `str` |
| `--delete` | Storage identifier of the project to unregister. The project is first checked against the InfoBIM contract so a plain container cannot be removed through this command. | — | `str` |


</div>


<div class="cli-reference-command" markdown="1">

### List the entities of an InfoBIM Project. { #component-project-command-7 }

<div class="cli-reference-label">Syntax</div>

```bash
infobim project --global-id <value> --entity
```


| Argument | Description | Aliases | Value |
| --- | --- | --- | --- |
| `--global-id` | Resolve the GlobalId of an IfcProject to the InfoBIM project that carries it, and to the container underneath it. | — | `str` |
| `--entity` | List every entity the project holds, grouped by the dataset of the container that keeps it. | — | No value |


</div>


<div class="cli-reference-command" markdown="1">

### Remove an entity of an InfoBIM Project. { #component-project-command-8 }

<div class="cli-reference-label">Syntax</div>

```bash
infobim project --global-id <value> --entity <value> --delete
```


| Argument | Description | Aliases | Value |
| --- | --- | --- | --- |
| `--global-id` | Resolve the GlobalId of an IfcProject to the InfoBIM project that carries it, and to the container underneath it. | — | `str` |
| `--entity` | Global id of the entity to remove. | — | `str` |
| `--delete` | Remove the entity. | — | No value |


</div>


<div class="cli-reference-command" markdown="1">

### Change the fields of an entity of an InfoBIM Project. { #component-project-command-9 }

<div class="cli-reference-label">Syntax</div>

```bash
infobim project --global-id <value> --entity <value> --update <value>
```


| Argument | Description | Aliases | Value |
| --- | --- | --- | --- |
| `--global-id` | Resolve the GlobalId of an IfcProject to the InfoBIM project that carries it, and to the container underneath it. | — | `str` |
| `--entity` | Global id of the entity to change. | — | `str` |
| `--update` | The values to write: a path to a .json or .csv file, a JSON object, or key=value assignments separated by commas. | — | `str` |


</div>


<div class="cli-reference-command" markdown="1">

### Report the health of a registered InfoBIM Project. { #component-project-command-10 }

<div class="cli-reference-label">Syntax</div>

```bash
infobim project --global-id <value> --health
```


| Argument | Description | Aliases | Value |
| --- | --- | --- | --- |
| `--global-id` | Resolve the GlobalId of an IfcProject to the InfoBIM project that carries it, and to the container underneath it. | — | `str` |
| `--health` | Run the InfoBIM Project health check capability on the selected project. Health compares what the project declares in metadata, index, manifests and its IfcProject against the files it actually holds and reports every verification that fails. | — | No value |


</div>


<div class="cli-reference-command" markdown="1">

### Inspect a registered InfoBIM Project. { #component-project-command-11 }

<div class="cli-reference-label">Syntax</div>

```bash
infobim project --global-id <value> --inspect
```


| Argument | Description | Aliases | Value |
| --- | --- | --- | --- |
| `--global-id` | Resolve the GlobalId of an IfcProject to the InfoBIM project that carries it, and to the container underneath it. | — | `str` |
| `--inspect` | Print the project's registered metadata along with a static tree summarizing its reserved InfoBIM dataset, linkset and any additional datasets. | — | No value |


</div>


<div class="cli-reference-command" markdown="1">

### Inspect a registered InfoBIM Project in the interactive Textual tree viewer. { #component-project-command-12 }

<div class="cli-reference-label">Syntax</div>

```bash
infobim project --global-id <value> --inspect --interactive
```


| Argument | Description | Aliases | Value |
| --- | --- | --- | --- |
| `--global-id` | Resolve the GlobalId of an IfcProject to the InfoBIM project that carries it, and to the container underneath it. | — | `str` |
| `--inspect` | Open the project's registered metadata along with a tree summarizing its reserved InfoBIM dataset, linkset and any additional datasets inside the interactive Textual viewer. | — | No value |
| `--interactive` | Open the project tree in the interactive Textual viewer with keyboard/mouse collapse and expand, native search, keyboard navigation (e=expand all, c=collapse all, q=quit, ↑/↓=navigate, Enter/Space=toggle a node). | `-i` | No value |


</div>


<div class="cli-reference-command" markdown="1">

### List every storage container registered as an InfoBIM Project. { #component-project-command-13 }

<div class="cli-reference-label">Syntax</div>

```bash
infobim project --list
```


| Argument | Description | Aliases | Value |
| --- | --- | --- | --- |
| `--list` | Print the list of every storage container currently registered as an InfoBIM Project. Containers that do not match the Project contract are excluded from the result instead of being reported as errors. | `-l` | No value |


</div>


<div class="cli-reference-command" markdown="1">

### Update a registered InfoBIM Project from a declared source. { #component-project-command-14 }

<div class="cli-reference-label">Syntax</div>

```bash
infobim project --global-id <value> --update <value>
```


| Argument | Description | Aliases | Value |
| --- | --- | --- | --- |
| `--global-id` | Resolve the GlobalId of an IfcProject to the InfoBIM project that carries it, and to the container underneath it. | — | `str` |
| `--update` | Source of values to write into the project's metadata and dataset fields. Accepts a path to a .csv file, a path to a .json file, or inline key=value assignments separated by commas. | — | `str` |


</div>



## run { #component-run }


<div class="cli-reference-command" markdown="1">

### Run a finite state machine on an InfoBIM project, from the YAML of its statechart. { #component-run-command-1 }

<div class="cli-reference-label">Syntax</div>

```bash
infobim run --global-id <value> --fsm <value>
```


| Argument | Description | Aliases | Value |
| --- | --- | --- | --- |
| `--global-id` | Resolve the GlobalId of an IfcProject to the InfoBIM project that carries it, and to the container underneath it. | — | `str` |
| `--fsm` | Path of the statechart YAML of the machine to run, or its path inside an installed package. | — | `Path` |


</div>
