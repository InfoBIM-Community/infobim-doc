# Documentação InfoBIM

**Informação de construção conectada por semântica.**

InfoBIM é a interface de linha de comando OpenBIM do ecossistema OntoBDC. Organiza modelos IFC, desenhos DXF/DWG, PDFs, imagens e planilhas em projetos descritos por um grafo semântico — os arquivos permanecem em seus formatos originais.

Este repositório é a fonte da documentação publicada em GitHub Pages. O site publicado tem busca, navegação lateral e seletor de idioma/tema; este README é um menu para ler o mesmo conteúdo direto aqui no GitHub, em markdown puro.

**Idiomas:** [Português](content/pt/index.md) · [English](content/en/index.md) · [Español](content/es/index.md)

## Primeiros passos

- [Visão geral](content/pt/index.md) — o que é o InfoBIM e os conceitos principais.
- [Primeiros passos](content/pt/getting-started.md) — instalação e criação do primeiro projeto.

## Referência

- [Referência CLI](content/pt/cli.md) — todos os comandos do executável `infobim`, por componente, com sintaxe e argumentos.
- [Referência de módulos](content/pt/module.md) — organização do pacote por componente: superfícies de plugin e quantos comandos cada um registra.

### Módulos

| Módulo | Descrição |
| --- | --- |
| [`2d`](content/pt/cli.md#component-2d) | Visualizador 2D opcional (PySide6) para desenhos DXF/DWG; seleção de pontos para anotações e elementos IFC. |
| [`annotation`](content/pt/cli.md#component-annotation) | Cria, atualiza, lista, exporta e remove anotações no padrão W3C de um projeto InfoBIM. |
| [`cli`](content/pt/cli.md#component-cli) | Pontos de entrada principais: inicializa um workspace, executa o servidor local, informa a versão. |
| [`context`](content/pt/cli.md#component-context) | Inspeciona valores armazenados no dicionário de contexto de execução. |
| [`dev`](content/pt/cli.md#component-dev) | Delega comandos de desenvolvimento para a CLI separada do workspace `ontobdc-dev`. |
| [`drawing`](content/pt/cli.md#component-drawing) | Classifica e extrai views semânticas de desenhos CAD, incluindo conversão de DWG para DXF. |
| [`ifc`](content/pt/cli.md#component-ifc) | Reporta a integridade de modelos IFC e cria elementos em pontos selecionados em um desenho. |
| [`project`](content/pt/cli.md#component-project) | Cria, anexa, atualiza, inspeciona e mantém projetos InfoBIM e suas entidades. |
| [`run`](content/pt/cli.md#component-run) | Executa uma máquina de estado finito em um projeto, a partir do YAML de um statechart. |

### Máquinas de estado (FSM)

- [2D](content/pt/fsm/2d.md)
- [3D](content/pt/fsm/3d.md)
- [Annotation](content/pt/fsm/annotation.md)
- [CLI](content/pt/fsm/cli.md)
- [Context](content/pt/fsm/context.md)
- [Drawing](content/pt/fsm/drawing.md)
- [IFC](content/pt/fsm/ifc.md)
- [Project](content/pt/fsm/project.md)

## Ecossistema

OntoBDC fornece armazenamento, contêineres, datasets, manifestos e verificações de integridade. InfoBIM acrescenta as regras ligadas a IFC e buildingSMART. As ontologias vêm do pacote BrasidataCenter. A mesma CLI também é executada no navegador por meio de Pyodide em [databim.tech](https://databim.tech).

## Sobre este repositório

O conteúdo publicado vem de `content/<idioma>/`, montado como site [MkDocs](https://www.mkdocs.org/) com [mkdocs-material](https://squidfunk.github.io/mkdocs-material/) e [mkdocs-static-i18n](https://ultrabug.github.io/mkdocs-static-i18n/). O deploy para GitHub Pages roda em [`.github/workflows/deploy-docs.yml`](.github/workflows/deploy-docs.yml) a cada push em `master`.
