# Referencia de FSM — drawing

Máquinas de estados finitos declaradas por `drawing` en `infobim`.


<div class="fsm-reference-index" markdown="1">

| Nombre | Descripción |
| --- | --- |
| [`StandardDrawingViewDiscovery`](#fsm-standarddrawingviewdiscovery) | Statechart for discovering the Drawing Views of a sheet, extracting each one into a DXF of its own. |
| [`StandardInfoBIMDwgToDxf`](#fsm-standardinfobimdwgtodxf) | Convert the requested DWG file into a DXF payload cached under the project's reserved InfoBIM dataset. |

</div>


<div class="fsm-reference-machine" markdown="1">

### `StandardDrawingViewDiscovery` { #fsm-standarddrawingviewdiscovery }



<div class="cli-reference-label">Descripción</div>

Statechart for discovering the Drawing Views of a sheet, extracting each one into a DXF of its own.


<div class="cli-reference-label">Estados</div>

<div class="fsm-reference-states" markdown="1">


<div class="fsm-reference-state" markdown="1">

Undefined

<span class="fsm-reference-value">`__undefined__`</span>

<span class="fsm-reference-description">Initial state, before the sheet was read.</span>



</div>

<span class="fsm-reference-arrow">↓</span>



<div class="fsm-reference-state" markdown="1">

Drawing Viewports Discovered

<span class="fsm-reference-value">`__drawing_viewports_discovered__`</span>

<span class="fsm-reference-description">The sheet is loaded and the regions its viewports show opened the Drawing View candidates.</span>


<span class="fsm-reference-capability"><span class="fsm-reference-capability-label">Capability</span>: `src/ontobdc/storage/plugin/capability/transformation/single_file_metadata_extracted.py`, `src/ontobdc/storage/plugin/capability/transformation/single_file_metadata_extracted.py`, `src/infobim/drawing/plugin/capability/loader/sheet_entities.py`, `src/infobim/drawing/plugin/capability/transformation/drawing_viewports_discovered.py`</span>


</div>

<span class="fsm-reference-arrow">↓</span>



<div class="fsm-reference-state" markdown="1">

Drawing View Titles Resolved

<span class="fsm-reference-value">`__drawing_view_titles_resolved__`</span>

<span class="fsm-reference-description">The titles and scales written on the sheet were given to the candidates.</span>


<span class="fsm-reference-capability"><span class="fsm-reference-capability-label">Capability</span>: `src/infobim/drawing/plugin/capability/transformation/drawing_view_titles_resolved.py`</span>


</div>

<span class="fsm-reference-arrow">↓</span>



<div class="fsm-reference-state" markdown="1">

Drawing View Frames Detected

<span class="fsm-reference-value">`__drawing_view_frames_detected__`</span>

<span class="fsm-reference-description">The frames drawn around views delimited the candidates.</span>


<span class="fsm-reference-capability"><span class="fsm-reference-capability-label">Capability</span>: `src/infobim/drawing/plugin/capability/transformation/drawing_view_frames_detected.py`</span>


</div>

<span class="fsm-reference-arrow">↓</span>



<div class="fsm-reference-state" markdown="1">

Drawing View References Detected

<span class="fsm-reference-value">`__drawing_view_references_detected__`</span>

<span class="fsm-reference-description">Section labels, detail bubbles and view marks were attached to the candidates.</span>


<span class="fsm-reference-capability"><span class="fsm-reference-capability-label">Capability</span>: `src/infobim/drawing/plugin/capability/transformation/drawing_view_references_detected.py`</span>


</div>

<span class="fsm-reference-arrow">↓</span>



<div class="fsm-reference-state" markdown="1">

Drawing View Clusters Detected

<span class="fsm-reference-value">`__drawing_view_clusters_detected__`</span>

<span class="fsm-reference-description">Spatial clusters delimited what the explicit evidence did not.</span>


<span class="fsm-reference-capability"><span class="fsm-reference-capability-label">Capability</span>: `src/infobim/drawing/plugin/capability/transformation/drawing_view_clusters_detected.py`</span>


</div>

<span class="fsm-reference-arrow">↓</span>



<div class="fsm-reference-state" markdown="1">

Drawing Views Classified

<span class="fsm-reference-value">`__drawing_views_classified__`</span>

<span class="fsm-reference-description">Each delimited candidate settled into a classified Drawing View.</span>


<span class="fsm-reference-capability"><span class="fsm-reference-capability-label">Capability</span>: `src/infobim/drawing/plugin/capability/transformation/drawing_views_classified.py`</span>


</div>

<span class="fsm-reference-arrow">↓</span>



<div class="fsm-reference-state" markdown="1">

Drawing Views Extracted

<span class="fsm-reference-value">`__drawing_views_extracted__`</span>

<span class="fsm-reference-description">Each Drawing View was written into a DXF of its own inside the project.</span>


<span class="fsm-reference-capability"><span class="fsm-reference-capability-label">Capability</span>: `src/infobim/drawing/plugin/capability/transformation/drawing_views_extracted.py`</span>


</div>

<span class="fsm-reference-arrow">↓</span>



<div class="fsm-reference-state" markdown="1">

Drawing View Relationships Modeled <span class="fsm-reference-final">final</span>

<span class="fsm-reference-value">`__drawing_view_relationships_modeled__`</span>

<span class="fsm-reference-description">The sheet and its views are modelled as ICDD documents and links and as OntoSTEP presentation entities, conforming to SHACL.</span>


<span class="fsm-reference-capability"><span class="fsm-reference-capability-label">Capability</span>: `src/infobim/drawing/plugin/capability/transformation/drawing_view_relationships_modeled.py`</span>


</div>



</div>

</div>

<div class="fsm-reference-machine" markdown="1">

### `StandardInfoBIMDwgToDxf` { #fsm-standardinfobimdwgtodxf }

<div class="fsm-reference-title" markdown="1">InfoBIM DWG to DXF</div>

<div class="cli-reference-label">Descripción</div>

Convert the requested DWG file into a DXF payload cached under the project's reserved InfoBIM dataset.


<div class="cli-reference-label">Estados</div>

<div class="fsm-reference-states" markdown="1">


<div class="fsm-reference-state" markdown="1">

Undefined

<span class="fsm-reference-value">`__undefined__`</span>

<span class="fsm-reference-description">Initial state before the DWG file is converted.</span>



</div>

<span class="fsm-reference-arrow">↓</span>



<div class="fsm-reference-state" markdown="1">

DWG Converted to DXF <span class="fsm-reference-final">final</span>

<span class="fsm-reference-value">`__dwg_converted_to_dxf__`</span>

<span class="fsm-reference-description">The DWG file was converted into a DXF file named by the SHA-256 of the DWG content, under .\_\_infobim\_\_/payload/document/etl/format/dwg/dxf/.</span>



</div>



</div>

</div>
