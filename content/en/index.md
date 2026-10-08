# InfoBIM documentation

**Building information connected through semantics.**

InfoBIM is the OpenBIM command line interface of the OntoBDC ecosystem. It organizes IFC models, DXF/DWG drawings, PDFs, images and spreadsheets into projects described by a semantic graph. Files remain in their original formats.

## Explore the documentation

- [Getting started](getting-started.md): install InfoBIM and create your first project.
- [CLI reference](cli.md): explore project and IFC model commands.

## Core concepts

| Concept | Responsibility |
| --- | --- |
| Storage root | A folder initialized with `infobim init`; maintains the project index. |
| Project | An OntoBDC container with the reserved `.__infobim__/` dataset and an IfcProject declaration. |
| Identity | The IfcProject GlobalId used to identify the project. |
| Refresh | `project --refresh` reconciles project files and metadata. |

## Ecosystem

OntoBDC provides storage, containers, datasets, manifests and health checks. InfoBIM adds IFC and buildingSMART rules. Ontologies come from the BrasidataCenter package. The same CLI also runs in the browser through Pyodide in databim.tech.

Use the header selector to change languages and the theme button to switch between light and dark modes.
