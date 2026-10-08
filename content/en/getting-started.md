# Getting started

## Installation

Use **Python 3.11 or later** and install the three ecosystem packages:

```bash
pip install brasidatacenter ontobdc infobim
infobim --help
```

## Create a project

```bash
mkdir obras
cd obras
infobim init
infobim project --create "Hospital Norte"
cd hospital-norte
```

Copy your IFC, DXF, PDF or spreadsheet files into the project folder. Then register them and check the project status:

```bash
infobim project --refresh
infobim project --inspect
infobim project --health
```

The root contains `.__ontobdc__/`, with configuration and an index. The project contains its own metadata and the reserved `.__infobim__/` dataset. The IfcProject GlobalId identifies the project.

## Optional features

```bash
pip install 'infobim[2d]'
pip install 'infobim[3d]'
```

The `infobim[all]` extra installs both viewers. To read DWG files, install the ODA File Converter and make it available on `PATH` or configure `INFOBIM_ODA_FILE_CONVERTER`.

[Explore the available commands](cli.md).
