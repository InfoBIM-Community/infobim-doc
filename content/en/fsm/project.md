# FSM reference — project

Finite-state machines declared by `project` in `infobim`.


<div class="fsm-reference-index" markdown="1">

| Name | Description |
| --- | --- |
| [`StandardInfoBIMProjectCreate`](#fsm-standardinfobimprojectcreate) | Statechart for InfoBIM project creation over an OntoBDC container. |
| [`StandardInfoBIMProjectRefresh`](#fsm-standardinfobimprojectrefresh) | Statechart for the InfoBIM-specific project refresh stage, which runs ONLY AFTER the standard OntoBDC container refresh state machine has already completed successfully. |

</div>


<div class="fsm-reference-machine" markdown="1">

### `StandardInfoBIMProjectCreate` { #fsm-standardinfobimprojectcreate }



<div class="cli-reference-label">Description</div>

Statechart for InfoBIM project creation over an OntoBDC container.


<div class="cli-reference-label">States</div>

<div class="fsm-reference-states" markdown="1">


<div class="fsm-reference-state" markdown="1">

Undefined

<span class="fsm-reference-value">`__undefined__`</span>

<span class="fsm-reference-description">Initial state before the target project directory exists.</span>



</div>

<span class="fsm-reference-arrow">↓</span>



<div class="fsm-reference-state" markdown="1">

Invalid Path <span class="fsm-reference-final">final</span>

<span class="fsm-reference-value">`__invalid_path__`</span>

<span class="fsm-reference-description">The target path points to an existing file and cannot be used as a project directory.</span>



</div>

<span class="fsm-reference-arrow">↓</span>



<div class="fsm-reference-state" markdown="1">

Directory Ready

<span class="fsm-reference-value">`__directory_ready__`</span>

<span class="fsm-reference-description">The target project directory exists and is ready for the next creation steps.</span>



</div>

<span class="fsm-reference-arrow">↓</span>



<div class="fsm-reference-state" markdown="1">

Container Metadata Ready

<span class="fsm-reference-value">`__container_metadata_ready__`</span>

<span class="fsm-reference-description">The container metadata file exists and describes the project container.</span>



</div>

<span class="fsm-reference-arrow">↓</span>



<div class="fsm-reference-state" markdown="1">

Container Storage Index Ready

<span class="fsm-reference-value">`__container_storage_index_ready__`</span>

<span class="fsm-reference-description">The storage index entry for the project container is synchronized.</span>



</div>

<span class="fsm-reference-arrow">↓</span>



<div class="fsm-reference-state" markdown="1">

Container Manifest Synced

<span class="fsm-reference-value">`__container_manifest_synced__`</span>

<span class="fsm-reference-description">The container manifest lists the project container files.</span>



</div>

<span class="fsm-reference-arrow">↓</span>



<div class="fsm-reference-state" markdown="1">

Project Dataset Ready

<span class="fsm-reference-value">`__project_dataset_ready__`</span>

<span class="fsm-reference-description">The container holds the reserved .\_\_infobim\_\_ dataset and indexes it.</span>



</div>

<span class="fsm-reference-arrow">↓</span>



<div class="fsm-reference-state" markdown="1">

IfcProject Ready <span class="fsm-reference-final">final</span>

<span class="fsm-reference-value">`__ifc_project_ready__`</span>

<span class="fsm-reference-description">The reserved dataset declares the IfcProject the model hangs from.</span>



</div>



</div>

</div>

<div class="fsm-reference-machine" markdown="1">

### `StandardInfoBIMProjectRefresh` { #fsm-standardinfobimprojectrefresh }

<div class="fsm-reference-title" markdown="1">InfoBIM Project Refresh</div>

<div class="cli-reference-label">Description</div>

Statechart for the InfoBIM-specific project refresh stage, which runs ONLY AFTER the standard OntoBDC container refresh state machine has already completed successfully.


<div class="cli-reference-label">States</div>

<div class="fsm-reference-states" markdown="1">


<div class="fsm-reference-state" markdown="1">

Undefined

<span class="fsm-reference-value">`__undefined__`</span>

<span class="fsm-reference-description">Initial state before the refresh stages of the InfoBIM project layer are evaluated.</span>



</div>

<span class="fsm-reference-arrow">↓</span>



<div class="fsm-reference-state" markdown="1">

Project Dataset Refreshed

<span class="fsm-reference-value">`__project_dataset_refreshed__`</span>

<span class="fsm-reference-description">The reserved .\_\_infobim\_\_ dataset is re-validated, re-titled and re-indexed against the freshly-refreshed container metadata.</span>



</div>

<span class="fsm-reference-arrow">↓</span>



<div class="fsm-reference-state" markdown="1">

IfcProject Refreshed

<span class="fsm-reference-value">`__ifc_project_refreshed__`</span>

<span class="fsm-reference-description">The IfcProject declaration and its schema-specific ifcOWL type are re-derived from the IFC files that currently live in the refreshed container.</span>



</div>

<span class="fsm-reference-arrow">↓</span>



<div class="fsm-reference-state" markdown="1">

Project Ready To Render <span class="fsm-reference-final">final</span>

<span class="fsm-reference-value">`__project_ready_to_render__`</span>

<span class="fsm-reference-description">Every DXF/DWG project linkset currently declared under the project's payload/linkset directory is re-validated against the five is\_drawing\_linked\_to\_project integrity conditions (source-DWG backlink, ifcOWL IfcDocumentInformation type, globalId\_IfcRoot and name\_IfcRoot per document).</span>



</div>



</div>

</div>
