# Primeros pasos

## Instalación

Utilice **Python 3.11 o superior** e instale los tres paquetes del ecosistema:

```bash
pip install brasidatacenter ontobdc infobim
infobim --help
```

## Cree un proyecto

```bash
mkdir obras
cd obras
infobim init
infobim project --create "Hospital Norte"
cd hospital-norte
```

Copie sus archivos IFC, DXF, PDF u hojas de cálculo en la carpeta del proyecto. Después, regístrelos y compruebe el estado del proyecto:

```bash
infobim project --refresh
infobim project --inspect
infobim project --health
```

La raíz contiene `.__ontobdc__/`, con la configuración y el índice. El proyecto contiene sus propios metadatos y el dataset reservado `.__infobim__/`. El GlobalId de IfcProject identifica el proyecto.

## Funciones opcionales

```bash
pip install 'infobim[2d]'
pip install 'infobim[3d]'
```

El extra `infobim[all]` instala ambos visualizadores. Para leer DWG, instale ODA File Converter y añádalo al `PATH` o configure `INFOBIM_ODA_FILE_CONVERTER`.

[Consulte los comandos disponibles](cli.md).
