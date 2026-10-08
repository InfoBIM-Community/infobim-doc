# Module reference

Browse the `infobim` package layout by component. Each component lists the plugin surfaces it declares and how many commands it registers.

<div class="module-reference-index" markdown="1">

| Module | Description | Plugin surfaces | Commands |
| --- | --- | --- | ---: |
| [`2d`](cli.md#component-2d) | Launch the optional PySide6 2D viewer to open DXF/DWG drawings and pick points for annotations and IFC elements. | `capability`, `command` | 2 |
| [`annotation`](cli.md#component-annotation) | Create, update, list, export and delete W3C-style annotations on an InfoBIM project, including picking points on a DXF drawing. | `command` | 8 |
| [`cli`](cli.md#component-cli) | Core entry points of the InfoBIM executable: initialize a workspace, run the local server and report the installed version. | `capability`, `check`, `command`, `machine` | 4 |
| [`context`](cli.md#component-context) | Inspect values held in the execution context dictionary. | `command` | 1 |
| [`dev`](cli.md#component-dev) | Delegate development commands, such as documentation generation, to the separate ontobdc-dev workspace CLI. | `command` | 1 |
| [`drawing`](cli.md#component-drawing) | Classify and extract semantic views from CAD drawings — viewports, titles, clusters, references and relationships — including DWG to DXF conversion. | `capability`, `check`, `command`, `machine` | 1 |
| [`ifc`](cli.md#component-ifc) | Report the health of a project's IFC models and create IFC elements at points picked on a DXF or DWG drawing. | `capability`, `check`, `command`, `machine`, `resolver` | 3 |
| [`project`](cli.md#component-project) | Create, attach, update, inspect and maintain InfoBIM projects and their entities. | `capability`, `check`, `command`, `machine`, `parameter` | 14 |
| [`run`](cli.md#component-run) | Run a finite-state machine on an InfoBIM project, from the YAML of its statechart. | `command` | 1 |

</div>
