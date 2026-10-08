# Referência de módulos

Consulte a organização do pacote `infobim` por componente. Cada componente mostra as superfícies de plugin que declara e quantos comandos registra.

<div class="module-reference-index" markdown="1">

| Módulo | Descrição | Superfícies de plugin | Comandos |
| --- | --- | --- | ---: |
| [`2d`](cli.md#component-2d) | Abre o visualizador 2D opcional (PySide6) para desenhos DXF/DWG e permite selecionar pontos para anotações e elementos IFC. | `capability`, `command` | 2 |
| [`annotation`](cli.md#component-annotation) | Cria, atualiza, lista, exporta e remove anotações no padrão W3C de um projeto InfoBIM, inclusive a partir de pontos selecionados em um desenho DXF. | `command` | 8 |
| [`cli`](cli.md#component-cli) | Pontos de entrada principais do executável InfoBIM: inicializa um workspace, executa o servidor local e informa a versão instalada. | `capability`, `check`, `command`, `machine` | 4 |
| [`context`](cli.md#component-context) | Inspeciona valores armazenados no dicionário de contexto de execução. | `command` | 1 |
| [`dev`](cli.md#component-dev) | Delega comandos de desenvolvimento, como a geração de documentação, para a CLI separada do workspace ontobdc-dev. | `command` | 1 |
| [`drawing`](cli.md#component-drawing) | Classifica e extrai views semânticas de desenhos CAD — viewports, títulos, clusters, referências e relacionamentos — incluindo a conversão de DWG para DXF. | `capability`, `check`, `command`, `machine` | 1 |
| [`ifc`](cli.md#component-ifc) | Reporta a integridade dos modelos IFC de um projeto e cria elementos IFC em pontos selecionados em um desenho DXF ou DWG. | `capability`, `check`, `command`, `machine`, `resolver` | 3 |
| [`project`](cli.md#component-project) | Cria, anexa, atualiza, inspeciona e mantém projetos InfoBIM e suas entidades. | `capability`, `check`, `command`, `machine`, `parameter` | 14 |
| [`run`](cli.md#component-run) | Executa uma máquina de estado finito em um projeto InfoBIM, a partir do YAML do seu statechart. | `command` | 1 |

</div>
