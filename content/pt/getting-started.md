# Primeiros passos

## Instalação

Use **Python 3.11 ou superior** e instale os três pacotes do ecossistema:

```bash
pip install brasidatacenter ontobdc infobim
infobim --help
```

## Crie um projeto

```bash
mkdir obras
cd obras
infobim init
infobim project --create "Hospital Norte"
cd hospital-norte
```

Copie seus arquivos IFC, DXF, PDFs ou planilhas para a pasta do projeto. Em seguida, registre-os e verifique o estado do projeto:

```bash
infobim project --refresh
infobim project --inspect
infobim project --health
```

A raiz contém `.__ontobdc__/`, com configuração e índice. O projeto contém seus próprios metadados e o dataset reservado `.__infobim__/`. O GlobalId de IfcProject identifica o projeto.

## Recursos opcionais

```bash
pip install 'infobim[2d]'
pip install 'infobim[3d]'
```

O extra `infobim[all]` instala os dois visualizadores. Para ler DWG, instale o ODA File Converter e disponibilize-o no `PATH` ou configure `INFOBIM_ODA_FILE_CONVERTER`.

[Consulte os comandos disponíveis](cli.md).
