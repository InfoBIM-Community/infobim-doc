# Documentação InfoBIM

**Informação de construção conectada por semântica.**

InfoBIM é a interface de linha de comando OpenBIM do ecossistema OntoBDC. Organiza modelos IFC, desenhos DXF/DWG, PDFs, imagens e planilhas em projetos descritos por um grafo semântico. Os arquivos permanecem em seus formatos originais.

## Explore a documentação

- [Primeiros passos](getting-started.md): instale o InfoBIM e crie seu primeiro projeto.
- [Referência CLI](cli.md): consulte os comandos de projetos e modelos IFC.

## Conceitos principais

| Conceito | Responsabilidade |
| --- | --- |
| Raiz de armazenamento | Pasta inicializada com `infobim init`; mantém o índice dos projetos. |
| Projeto | Contêiner OntoBDC com o dataset reservado `.__infobim__/` e uma declaração IfcProject. |
| Identidade | GlobalId do IfcProject, utilizado para identificar o projeto. |
| Atualização | `project --refresh` reconcilia arquivos e metadados do projeto. |

## Ecossistema

OntoBDC fornece armazenamento, contêineres, datasets, manifestos e verificações de integridade. InfoBIM acrescenta as regras ligadas a IFC e buildingSMART. As ontologias vêm do pacote BrasidataCenter. A mesma CLI também é executada no navegador por meio de Pyodide no databim.tech.

Use o seletor no cabeçalho para mudar o idioma e o botão de tema para alternar entre os modos claro e escuro.
