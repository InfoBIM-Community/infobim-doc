# Referencia de módulos

Consulte la organización del paquete `infobim` por componente. Cada componente muestra las superficies de plugin que declara y cuántos comandos registra.

<div class="module-reference-index" markdown="1">

| Módulo | Descripción | Superficies de plugin | Comandos |
| --- | --- | --- | ---: |
| [`2d`](cli.md#component-2d) | Abre el visor 2D opcional (PySide6) para dibujos DXF/DWG y permite seleccionar puntos para anotaciones y elementos IFC. | `capability`, `command` | 2 |
| [`annotation`](cli.md#component-annotation) | Crea, actualiza, lista, exporta y elimina anotaciones de estilo W3C de un proyecto InfoBIM, incluso a partir de puntos seleccionados en un dibujo DXF. | `command` | 8 |
| [`cli`](cli.md#component-cli) | Puntos de entrada principales del ejecutable InfoBIM: inicializa un workspace, ejecuta el servidor local e informa la versión instalada. | `capability`, `check`, `command`, `machine` | 4 |
| [`context`](cli.md#component-context) | Inspecciona valores almacenados en el diccionario de contexto de ejecución. | `command` | 1 |
| [`dev`](cli.md#component-dev) | Delega comandos de desarrollo, como la generación de documentación, a la CLI independiente del workspace ontobdc-dev. | `command` | 1 |
| [`drawing`](cli.md#component-drawing) | Clasifica y extrae vistas semánticas de dibujos CAD — viewports, títulos, clústeres, referencias y relaciones — incluyendo la conversión de DWG a DXF. | `capability`, `check`, `command`, `machine` | 1 |
| [`ifc`](cli.md#component-ifc) | Reporta la salud de los modelos IFC de un proyecto y crea elementos IFC en puntos seleccionados en un dibujo DXF o DWG. | `capability`, `check`, `command`, `machine`, `resolver` | 3 |
| [`project`](cli.md#component-project) | Crea, adjunta, actualiza, inspecciona y mantiene proyectos InfoBIM y sus entidades. | `capability`, `check`, `command`, `machine`, `parameter` | 14 |
| [`run`](cli.md#component-run) | Ejecuta una máquina de estados finitos en un proyecto InfoBIM, a partir del YAML de su statechart. | `command` | 1 |

</div>
