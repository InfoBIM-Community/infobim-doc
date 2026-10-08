# Referência de FSM — project

Máquinas de estado finito declaradas por `project` em `infobim`.


<div class="fsm-reference-index" markdown="1">

| Nome | Descrição |
| --- | --- |
| [`StandardInfoBIMProjectCreate`](#fsm-standardinfobimprojectcreate) | Statechart for InfoBIM project creation over an OntoBDC container. |
| [`StandardInfoBIMProjectRefresh`](#fsm-standardinfobimprojectrefresh) | Statechart para a etapa de atualização específica InfoBIM do projeto. Roda SOMENTE APÓS a state machine padrão de atualização de container do OntoBDC já ter terminado com sucesso. |

</div>


<div class="fsm-reference-machine" markdown="1">

### `StandardInfoBIMProjectCreate` { #fsm-standardinfobimprojectcreate }



<div class="cli-reference-label">Descrição</div>

Statechart for InfoBIM project creation over an OntoBDC container.


<div class="cli-reference-label">Estados</div>

<div class="fsm-reference-states" markdown="1">


<div class="fsm-reference-state" markdown="1">

Indefinido

<span class="fsm-reference-value">`__undefined__`</span>

<span class="fsm-reference-description">Estado inicial antes da existencia do diretorio alvo do projeto.</span>



</div>

<span class="fsm-reference-arrow">↓</span>



<div class="fsm-reference-state" markdown="1">

Caminho Invalido <span class="fsm-reference-final">final</span>

<span class="fsm-reference-value">`__invalid_path__`</span>

<span class="fsm-reference-description">O caminho alvo aponta para um arquivo existente e nao pode ser usado como diretorio de projeto.</span>



</div>

<span class="fsm-reference-arrow">↓</span>



<div class="fsm-reference-state" markdown="1">

Diretorio Pronto

<span class="fsm-reference-value">`__directory_ready__`</span>

<span class="fsm-reference-description">O diretorio alvo do projeto existe e esta pronto para as proximas etapas da criacao.</span>



</div>

<span class="fsm-reference-arrow">↓</span>



<div class="fsm-reference-state" markdown="1">

Metadados do Container Prontos

<span class="fsm-reference-value">`__container_metadata_ready__`</span>

<span class="fsm-reference-description">O arquivo de metadados do container existe e descreve o container do projeto.</span>



</div>

<span class="fsm-reference-arrow">↓</span>



<div class="fsm-reference-state" markdown="1">

Indice de Storage do Container Pronto

<span class="fsm-reference-value">`__container_storage_index_ready__`</span>

<span class="fsm-reference-description">A entrada do container do projeto no indice de storage esta sincronizada.</span>



</div>

<span class="fsm-reference-arrow">↓</span>



<div class="fsm-reference-state" markdown="1">

Manifesto do Container Sincronizado

<span class="fsm-reference-value">`__container_manifest_synced__`</span>

<span class="fsm-reference-description">O manifesto do container lista os arquivos do container do projeto.</span>



</div>

<span class="fsm-reference-arrow">↓</span>



<div class="fsm-reference-state" markdown="1">

Dataset de Projeto Pronto

<span class="fsm-reference-value">`__project_dataset_ready__`</span>

<span class="fsm-reference-description">O container contem o dataset reservado .\_\_infobim\_\_ e o indexa.</span>



</div>

<span class="fsm-reference-arrow">↓</span>



<div class="fsm-reference-state" markdown="1">

IfcProject Pronto <span class="fsm-reference-final">final</span>

<span class="fsm-reference-value">`__ifc_project_ready__`</span>

<span class="fsm-reference-description">O dataset reservado declara o IfcProject do qual o modelo depende.</span>



</div>



</div>

</div>

<div class="fsm-reference-machine" markdown="1">

### `StandardInfoBIMProjectRefresh` { #fsm-standardinfobimprojectrefresh }

<div class="fsm-reference-title" markdown="1">Atualização de Projeto InfoBIM</div>

<div class="cli-reference-label">Descrição</div>

Statechart para a etapa de atualização específica InfoBIM do projeto. Roda SOMENTE APÓS a state machine padrão de atualização de container do OntoBDC já ter terminado com sucesso.


<div class="cli-reference-label">Estados</div>

<div class="fsm-reference-states" markdown="1">


<div class="fsm-reference-state" markdown="1">

Indefinido

<span class="fsm-reference-value">`__undefined__`</span>

<span class="fsm-reference-description">Estado inicial antes das etapas de atualização da camada InfoBIM do projeto serem avaliadas.</span>



</div>

<span class="fsm-reference-arrow">↓</span>



<div class="fsm-reference-state" markdown="1">

Dataset de Projeto Atualizado

<span class="fsm-reference-value">`__project_dataset_refreshed__`</span>

<span class="fsm-reference-description">O dataset reservado .\_\_infobim\_\_ é re-validado, re-titulado e re-indexado contra os metadados do container recém-refrescado.</span>



</div>

<span class="fsm-reference-arrow">↓</span>



<div class="fsm-reference-state" markdown="1">

IfcProject Atualizado

<span class="fsm-reference-value">`__ifc_project_refreshed__`</span>

<span class="fsm-reference-description">A declaração de IfcProject e seu tipo ifcOWL específico de schema são re-derivados a partir dos arquivos IFC que atualmente vivem no container refrescado.</span>



</div>

<span class="fsm-reference-arrow">↓</span>



<div class="fsm-reference-state" markdown="1">

Projeto Pronto para Renderização <span class="fsm-reference-final">final</span>

<span class="fsm-reference-value">`__project_ready_to_render__`</span>

<span class="fsm-reference-description">Cada linkset de projeto DXF/DWG atualmente declarado sob o diretório payload/linkset do projeto é re-validado contra as cinco condições de integridade is\_drawing\_linked\_to\_project (backlink para o DWG de origem, tipo ifcOWL IfcDocumentInformation, globalId\_IfcRoot e name\_IfcRoot por documento).</span>



</div>



</div>

</div>
