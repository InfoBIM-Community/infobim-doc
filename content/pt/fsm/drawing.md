# Referência de FSM — drawing

Máquinas de estado finito declaradas por `drawing` em `infobim`.


<div class="fsm-reference-index" markdown="1">

| Nome | Descrição |
| --- | --- |
| [`StandardDrawingViewDiscovery`](#fsm-standarddrawingviewdiscovery) | Statechart for discovering the Drawing Views of a sheet, extracting each one into a DXF of its own. |
| [`StandardInfoBIMDwgToDxf`](#fsm-standardinfobimdwgtodxf) | Converte o arquivo DWG solicitado em um payload DXF armazenado no dataset reservado InfoBIM do projeto. |

</div>


<div class="fsm-reference-machine" markdown="1">

### `StandardDrawingViewDiscovery` { #fsm-standarddrawingviewdiscovery }



<div class="cli-reference-label">Descrição</div>

Statechart for discovering the Drawing Views of a sheet, extracting each one into a DXF of its own.


<div class="cli-reference-label">Estados</div>

<div class="fsm-reference-states" markdown="1">


<div class="fsm-reference-state" markdown="1">

Indefinido

<span class="fsm-reference-value">`__undefined__`</span>

<span class="fsm-reference-description">Estado inicial, antes da leitura da prancha.</span>



</div>

<span class="fsm-reference-arrow">↓</span>



<div class="fsm-reference-state" markdown="1">

Viewports da Prancha Descobertos

<span class="fsm-reference-value">`__drawing_viewports_discovered__`</span>

<span class="fsm-reference-description">A prancha foi carregada e as regioes mostradas pelos seus viewports abriram os candidatos a vista.</span>


<span class="fsm-reference-capability"><span class="fsm-reference-capability-label">Capability</span>: `src/ontobdc/storage/plugin/capability/transformation/single_file_metadata_extracted.py`, `src/ontobdc/storage/plugin/capability/transformation/single_file_metadata_extracted.py`, `src/infobim/drawing/plugin/capability/loader/sheet_entities.py`, `src/infobim/drawing/plugin/capability/transformation/drawing_viewports_discovered.py`</span>


</div>

<span class="fsm-reference-arrow">↓</span>



<div class="fsm-reference-state" markdown="1">

Titulos das Vistas Resolvidos

<span class="fsm-reference-value">`__drawing_view_titles_resolved__`</span>

<span class="fsm-reference-description">Os titulos e escalas escritos na prancha foram atribuidos aos candidatos.</span>


<span class="fsm-reference-capability"><span class="fsm-reference-capability-label">Capability</span>: `src/infobim/drawing/plugin/capability/transformation/drawing_view_titles_resolved.py`</span>


</div>

<span class="fsm-reference-arrow">↓</span>



<div class="fsm-reference-state" markdown="1">

Molduras das Vistas Detectadas

<span class="fsm-reference-value">`__drawing_view_frames_detected__`</span>

<span class="fsm-reference-description">As molduras desenhadas em volta das vistas delimitaram os candidatos.</span>


<span class="fsm-reference-capability"><span class="fsm-reference-capability-label">Capability</span>: `src/infobim/drawing/plugin/capability/transformation/drawing_view_frames_detected.py`</span>


</div>

<span class="fsm-reference-arrow">↓</span>



<div class="fsm-reference-state" markdown="1">

Referencias das Vistas Detectadas

<span class="fsm-reference-value">`__drawing_view_references_detected__`</span>

<span class="fsm-reference-description">Rotulos de corte, bolhas de detalhe e marcas de vista foram associados aos candidatos.</span>


<span class="fsm-reference-capability"><span class="fsm-reference-capability-label">Capability</span>: `src/infobim/drawing/plugin/capability/transformation/drawing_view_references_detected.py`</span>


</div>

<span class="fsm-reference-arrow">↓</span>



<div class="fsm-reference-state" markdown="1">

Agrupamentos das Vistas Detectados

<span class="fsm-reference-value">`__drawing_view_clusters_detected__`</span>

<span class="fsm-reference-description">Agrupamentos espaciais delimitaram o que a evidencia explicita nao delimitou.</span>


<span class="fsm-reference-capability"><span class="fsm-reference-capability-label">Capability</span>: `src/infobim/drawing/plugin/capability/transformation/drawing_view_clusters_detected.py`</span>


</div>

<span class="fsm-reference-arrow">↓</span>



<div class="fsm-reference-state" markdown="1">

Vistas Classificadas

<span class="fsm-reference-value">`__drawing_views_classified__`</span>

<span class="fsm-reference-description">Cada candidato delimitado virou uma vista classificada.</span>


<span class="fsm-reference-capability"><span class="fsm-reference-capability-label">Capability</span>: `src/infobim/drawing/plugin/capability/transformation/drawing_views_classified.py`</span>


</div>

<span class="fsm-reference-arrow">↓</span>



<div class="fsm-reference-state" markdown="1">

Vistas Extraidas

<span class="fsm-reference-value">`__drawing_views_extracted__`</span>

<span class="fsm-reference-description">Cada vista foi gravada em um DXF proprio dentro do projeto.</span>


<span class="fsm-reference-capability"><span class="fsm-reference-capability-label">Capability</span>: `src/infobim/drawing/plugin/capability/transformation/drawing_views_extracted.py`</span>


</div>

<span class="fsm-reference-arrow">↓</span>



<div class="fsm-reference-state" markdown="1">

Relacoes das Vistas Modeladas <span class="fsm-reference-final">final</span>

<span class="fsm-reference-value">`__drawing_view_relationships_modeled__`</span>

<span class="fsm-reference-description">A prancha e suas vistas estao modeladas como documentos e links ICDD e como entidades de apresentacao OntoSTEP, conformes ao SHACL.</span>


<span class="fsm-reference-capability"><span class="fsm-reference-capability-label">Capability</span>: `src/infobim/drawing/plugin/capability/transformation/drawing_view_relationships_modeled.py`</span>


</div>



</div>

</div>

<div class="fsm-reference-machine" markdown="1">

### `StandardInfoBIMDwgToDxf` { #fsm-standardinfobimdwgtodxf }

<div class="fsm-reference-title" markdown="1">DWG para DXF InfoBIM</div>

<div class="cli-reference-label">Descrição</div>

Converte o arquivo DWG solicitado em um payload DXF armazenado no dataset reservado InfoBIM do projeto.


<div class="cli-reference-label">Estados</div>

<div class="fsm-reference-states" markdown="1">


<div class="fsm-reference-state" markdown="1">

Indefinido

<span class="fsm-reference-value">`__undefined__`</span>

<span class="fsm-reference-description">Estado inicial antes da conversão do arquivo DWG.</span>



</div>

<span class="fsm-reference-arrow">↓</span>



<div class="fsm-reference-state" markdown="1">

DWG Convertido para DXF <span class="fsm-reference-final">final</span>

<span class="fsm-reference-value">`__dwg_converted_to_dxf__`</span>

<span class="fsm-reference-description">O arquivo DWG foi convertido em um arquivo DXF nomeado pelo SHA-256 do conteúdo do DWG, em .\_\_infobim\_\_/payload/document/etl/format/dwg/dxf/.</span>



</div>



</div>

</div>
