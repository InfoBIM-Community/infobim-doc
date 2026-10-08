# Documentación InfoBIM

**Información de construcción conectada mediante semántica.**

InfoBIM es la interfaz de línea de comandos OpenBIM del ecosistema OntoBDC. Organiza modelos IFC, dibujos DXF/DWG, PDF, imágenes y hojas de cálculo en proyectos descritos por un grafo semántico. Los archivos conservan sus formatos originales.

## Explore la documentación

- [Primeros pasos](getting-started.md): instale InfoBIM y cree su primer proyecto.
- [Referencia CLI](cli.md): consulte los comandos de proyectos y modelos IFC.

## Conceptos principales

| Concepto | Responsabilidad |
| --- | --- |
| Raíz de almacenamiento | Carpeta inicializada con `infobim init`; mantiene el índice de proyectos. |
| Proyecto | Contenedor OntoBDC con el dataset reservado `.__infobim__/` y una declaración IfcProject. |
| Identidad | GlobalId de IfcProject, utilizado para identificar el proyecto. |
| Actualización | `project --refresh` reconcilia los archivos y metadatos del proyecto. |

## Ecosistema

OntoBDC proporciona almacenamiento, contenedores, datasets, manifiestos y verificaciones de integridad. InfoBIM añade las reglas de IFC y buildingSMART. Las ontologías proceden del paquete BrasidataCenter. La misma CLI también se ejecuta en el navegador mediante Pyodide en databim.tech.

Utilice el selector del encabezado para cambiar el idioma y el botón de tema para alternar entre los modos claro y oscuro.
