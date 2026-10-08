# Referência de FSM — annotation

Máquinas de estado finito declaradas por `annotation` em `infobim`.


=== "FSM"

    <div class="fsm-reference-index" markdown="1">

    | Nome | Descrição |
    | --- | --- |
    | [`StandardAnnotationCreationFromPoint`](#fsm-standardannotationcreationfrompoint) | Identifica o tipo de uma anotacao e cria anotacoes desse tipo em pontos escolhidos sobre um desenho. |
    | [`StandardAnnotationExportToExcel`](#fsm-standardannotationexporttoexcel) | Exporta as anotacoes de um tipo para uma planilha Excel que embute as fotos reduzidas a que elas se referem. |

    </div>

    
    <div class="fsm-reference-machine" markdown="1">

    ### `StandardAnnotationCreationFromPoint` { #fsm-standardannotationcreationfrompoint }

    <div class="fsm-reference-title" markdown="1">Criacao de Anotacao por Ponto</div>

    <div class="cli-reference-label">Descrição</div>

    Identifica o tipo de uma anotacao e cria anotacoes desse tipo em pontos escolhidos sobre um desenho.


    <div class="cli-reference-label">Estados</div>

    <div class="fsm-reference-states" markdown="1">


    <div class="fsm-reference-state" markdown="1">

    Indefinido

    <span class="fsm-reference-value">`__undefined__`</span>

    <span class="fsm-reference-description">Estado inicial antes da identificacao do tipo da anotacao.</span>



    </div>

    <span class="fsm-reference-arrow">↓</span>



    <div class="fsm-reference-state" markdown="1">

    Tipo da Anotacao Identificado

    <span class="fsm-reference-value">`__annotation_type_identified__`</span>

    <span class="fsm-reference-description">O tipo da anotacao a ser criada foi identificado.</span>


    <span class="fsm-reference-capability"><span class="fsm-reference-capability-label">Capability</span>: `src/ontobdc/annotation/plugin/capability/transformation/annotation_type_identified.py`</span>


    </div>

    <span class="fsm-reference-arrow">↓</span>



    <div class="fsm-reference-state" markdown="1">

    Metadados do Arquivo Extraidos

    <span class="fsm-reference-value">`__file_metadata_extracted__`</span>

    <span class="fsm-reference-description">O tipo MIME e os metadados de sistema de arquivos do desenho solicitado foram extraidos.</span>


    <span class="fsm-reference-capability"><span class="fsm-reference-capability-label">Capability</span>: `src/ontobdc/storage/plugin/capability/transformation/single_file_metadata_extracted.py`</span>


    </div>

    <span class="fsm-reference-arrow">↓</span>



    <div class="fsm-reference-state" markdown="1">

    Documentos Desenhaveis Carregados

    <span class="fsm-reference-value">`__drawable_documents_loaded__`</span>

    <span class="fsm-reference-description">O desenho solicitado, convertido de DWG quando necessario, foi carregado como documento DXF original.</span>


    <span class="fsm-reference-capability"><span class="fsm-reference-capability-label">Capability</span>: `src/ontobdc/annotation/plugin/capability/loader/drawable_documents_loaded.py`</span>


    </div>

    <span class="fsm-reference-arrow">↓</span>



    <div class="fsm-reference-state" markdown="1">

    Visualizador de Arquivo Desenhavel Aberto

    <span class="fsm-reference-value">`__drawable_file_viewer_opened__`</span>

    <span class="fsm-reference-description">O desenho carregado foi aberto em uma janela do visualizador 2D que permanece aberta para a captura de pontos.</span>


    <span class="fsm-reference-capability"><span class="fsm-reference-capability-label">Capability</span>: `src/ontobdc/annotation/plugin/capability/loader/drawable_file_viewer_opened.py`</span>


    </div>

    <span class="fsm-reference-arrow">↓</span>



    <div class="fsm-reference-state" markdown="1">

    Pontos Capturados

    <span class="fsm-reference-value">`__points_captured__`</span>

    <span class="fsm-reference-description">Os pontos nos quais as anotacoes sao posicionadas foram escolhidos na janela aberta do visualizador, na ordem dos cliques.</span>


    <span class="fsm-reference-capability"><span class="fsm-reference-capability-label">Capability</span>: `src/ontobdc/annotation/plugin/capability/loader/points_captured.py`</span>


    </div>

    <span class="fsm-reference-arrow">↓</span>



    <div class="fsm-reference-state" markdown="1">

    Detalhes da Anotacao Preenchidos

    <span class="fsm-reference-value">`__annotation_details_filled__`</span>

    <span class="fsm-reference-description">O titulo, o texto e o autor das anotacoes foram preenchidos por quem escolheu os pontos.</span>


    <span class="fsm-reference-capability"><span class="fsm-reference-capability-label">Capability</span>: `src/ontobdc/annotation/plugin/capability/loader/annotation_details_filled.py`</span>


    </div>

    <span class="fsm-reference-arrow">↓</span>



    <div class="fsm-reference-state" markdown="1">

    Anotacoes Criadas <span class="fsm-reference-final">final</span>

    <span class="fsm-reference-value">`__annotations_created__`</span>

    <span class="fsm-reference-description">Anotacoes do tipo identificado foram criadas nos pontos capturados.</span>


    <span class="fsm-reference-capability"><span class="fsm-reference-capability-label">Capability</span>: `src/ontobdc/annotation/plugin/capability/transformation/annotations_created.py`</span>


    </div>



    </div>

    </div>

    <div class="fsm-reference-machine" markdown="1">

    ### `StandardAnnotationExportToExcel` { #fsm-standardannotationexporttoexcel }

    <div class="fsm-reference-title" markdown="1">Exportacao de Anotacoes para Excel</div>

    <div class="cli-reference-label">Descrição</div>

    Exporta as anotacoes de um tipo para uma planilha Excel que embute as fotos reduzidas a que elas se referem.


    <div class="cli-reference-label">Estados</div>

    <div class="fsm-reference-states" markdown="1">


    <div class="fsm-reference-state" markdown="1">

    Indefinido

    <span class="fsm-reference-value">`__undefined__`</span>

    <span class="fsm-reference-description">Estado inicial antes da identificacao do escopo da exportacao.</span>



    </div>

    <span class="fsm-reference-arrow">↓</span>



    <div class="fsm-reference-state" markdown="1">

    Escopo da Exportacao Identificado

    <span class="fsm-reference-value">`__export_scope_identified__`</span>

    <span class="fsm-reference-description">O tipo de anotacao a exportar e o container que guarda suas anotacoes foram identificados.</span>


    <span class="fsm-reference-capability"><span class="fsm-reference-capability-label">Capability</span>: `src/ontobdc/annotation/plugin/capability/transformation/export_scope_identified.py`</span>


    </div>

    <span class="fsm-reference-arrow">↓</span>



    <div class="fsm-reference-state" markdown="1">

    Anotacoes Coletadas

    <span class="fsm-reference-value">`__annotations_collected__`</span>

    <span class="fsm-reference-description">As anotacoes do tipo identificado foram lidas do container e numeradas.</span>


    <span class="fsm-reference-capability"><span class="fsm-reference-capability-label">Capability</span>: `src/ontobdc/annotation/plugin/capability/transformation/annotations_collected.py`</span>


    </div>

    <span class="fsm-reference-arrow">↓</span>



    <div class="fsm-reference-state" markdown="1">

    Fotos Coletadas

    <span class="fsm-reference-value">`__photos_collected__`</span>

    <span class="fsm-reference-description">As imagens entre os arquivos a que cada anotacao se refere foram encontradas no container e numeradas.</span>


    <span class="fsm-reference-capability"><span class="fsm-reference-capability-label">Capability</span>: `src/ontobdc/annotation/plugin/capability/transformation/photos_collected.py`</span>


    </div>

    <span class="fsm-reference-arrow">↓</span>



    <div class="fsm-reference-state" markdown="1">

    Fotos Reduzidas

    <span class="fsm-reference-value">`__photos_downsampled__`</span>

    <span class="fsm-reference-description">Cada foto foi reduzida a uma imagem mais leve para ser embutida na planilha.</span>


    <span class="fsm-reference-capability"><span class="fsm-reference-capability-label">Capability</span>: `src/ontobdc/annotation/plugin/capability/transformation/photos_downsampled.py`</span>


    </div>

    <span class="fsm-reference-arrow">↓</span>



    <div class="fsm-reference-state" markdown="1">

    Planilha Construida

    <span class="fsm-reference-value">`__workbook_built__`</span>

    <span class="fsm-reference-description">A planilha com o indice de anotacoes, o acervo de fotos e o carrossel de cada item foi construida.</span>


    <span class="fsm-reference-capability"><span class="fsm-reference-capability-label">Capability</span>: `src/ontobdc/annotation/plugin/capability/transformation/workbook_built.py`</span>


    </div>

    <span class="fsm-reference-arrow">↓</span>



    <div class="fsm-reference-state" markdown="1">

    Planilha Salva <span class="fsm-reference-final">final</span>

    <span class="fsm-reference-value">`__workbook_saved__`</span>

    <span class="fsm-reference-description">A planilha foi salva e esta pronta para ser recebida.</span>


    <span class="fsm-reference-capability"><span class="fsm-reference-capability-label">Capability</span>: `src/ontobdc/annotation/plugin/capability/transformation/workbook_saved.py`</span>


    </div>



    </div>

    </div>


=== "Cadeias"

    <div class="fsm-reference-index" markdown="1">

    | Nome | Descrição |
    | --- | --- |
    | [`AnnotationDetailsChain`](#fsm-annotationdetailschain) | Fallback chain run by ANNOTATION\_DETAILS\_FILLED when the context maps no capability to the file's MIME type. The complete topology is declared here: the root is parallel and each region is one responsibility, named by the ID of the AnnotationDetailsChainSupport capability it runs. The worker only interprets this file; it never adds, removes or renames states or regions. ontobdc currently ships no capability implementing AnnotationDetailsChainSupport, so the chain declares no responsibility region. A responsibility is declared as one region of this shape: - name: &lt;responsibility&gt; initial: &lt;responsibility&gt;\_pending states: - name: &lt;responsibility&gt;\_pending transitions: - target: &lt;responsibility&gt;\_completed guard: worker.can\_handle('&lt;capability id&gt;') action: worker.execute\_responsibility('&lt;capability id&gt;') - target: &lt;responsibility&gt;\_completed guard: not worker.can\_handle('&lt;capability id&gt;') - name: &lt;responsibility&gt;\_completed type: final |
    | [`DrawableDocumentsChain`](#fsm-drawabledocumentschain) | Fallback chain run by DRAWABLE\_DOCUMENTS\_LOADED when the context maps no capability to the file's MIME type. The complete topology is declared here: the root is parallel and each region is one responsibility, named by the ID of the DrawableDocumentChainSupport capability it runs. The worker only interprets this file; it never adds, removes or renames states or regions. ontobdc currently ships no capability implementing DrawableDocumentChainSupport, so the chain declares no responsibility region. A responsibility is declared as one region of this shape: - name: &lt;responsibility&gt; initial: &lt;responsibility&gt;\_pending states: - name: &lt;responsibility&gt;\_pending transitions: - target: &lt;responsibility&gt;\_completed guard: worker.can\_handle('&lt;capability id&gt;') action: worker.execute\_responsibility('&lt;capability id&gt;') - target: &lt;responsibility&gt;\_completed guard: not worker.can\_handle('&lt;capability id&gt;') - name: &lt;responsibility&gt;\_completed type: final |
    | [`DrawableFileViewerChain`](#fsm-drawablefileviewerchain) | Fallback chain run by DRAWABLE\_FILE\_VIEWER\_OPENED when the context maps no capability to the file's MIME type. The complete topology is declared here: the root is parallel and each region is one responsibility, named by the ID of the DrawableFileViewerChainSupport capability it runs. The worker only interprets this file; it never adds, removes or renames states or regions. ontobdc currently ships no capability implementing DrawableFileViewerChainSupport, so the chain declares no responsibility region. A responsibility is declared as one region of this shape: - name: &lt;responsibility&gt; initial: &lt;responsibility&gt;\_pending states: - name: &lt;responsibility&gt;\_pending transitions: - target: &lt;responsibility&gt;\_completed guard: worker.can\_handle('&lt;capability id&gt;') action: worker.execute\_responsibility('&lt;capability id&gt;') - target: &lt;responsibility&gt;\_completed guard: not worker.can\_handle('&lt;capability id&gt;') - name: &lt;responsibility&gt;\_completed type: final |
    | [`PointsCapturedChain`](#fsm-pointscapturedchain) | Fallback chain run by POINTS\_CAPTURED when the context maps no capability to the file's MIME type. The complete topology is declared here: the root is parallel and each region is one responsibility, named by the ID of the PointsCapturedChainSupport capability it runs. The worker only interprets this file; it never adds, removes or renames states or regions. ontobdc currently ships no capability implementing PointsCapturedChainSupport, so the chain declares no responsibility region. A responsibility is declared as one region of this shape: - name: &lt;responsibility&gt; initial: &lt;responsibility&gt;\_pending states: - name: &lt;responsibility&gt;\_pending transitions: - target: &lt;responsibility&gt;\_completed guard: worker.can\_handle('&lt;capability id&gt;') action: worker.execute\_responsibility('&lt;capability id&gt;') - target: &lt;responsibility&gt;\_completed guard: not worker.can\_handle('&lt;capability id&gt;') - name: &lt;responsibility&gt;\_completed type: final |

    </div>

    
    <div class="fsm-reference-machine" markdown="1">

    ### `AnnotationDetailsChain` { #fsm-annotationdetailschain }



    <div class="cli-reference-label">Descrição</div>

    Fallback chain run by ANNOTATION\_DETAILS\_FILLED when the context maps no capability to the file's MIME type. The complete topology is declared here: the root is parallel and each region is one responsibility, named by the ID of the AnnotationDetailsChainSupport capability it runs. The worker only interprets this file; it never adds, removes or renames states or regions. ontobdc currently ships no capability implementing AnnotationDetailsChainSupport, so the chain declares no responsibility region. A responsibility is declared as one region of this shape: - name: &lt;responsibility&gt; initial: &lt;responsibility&gt;\_pending states: - name: &lt;responsibility&gt;\_pending transitions: - target: &lt;responsibility&gt;\_completed guard: worker.can\_handle('&lt;capability id&gt;') action: worker.execute\_responsibility('&lt;capability id&gt;') - target: &lt;responsibility&gt;\_completed guard: not worker.can\_handle('&lt;capability id&gt;') - name: &lt;responsibility&gt;\_completed type: final


    </div>

    <div class="fsm-reference-machine" markdown="1">

    ### `DrawableDocumentsChain` { #fsm-drawabledocumentschain }



    <div class="cli-reference-label">Descrição</div>

    Fallback chain run by DRAWABLE\_DOCUMENTS\_LOADED when the context maps no capability to the file's MIME type. The complete topology is declared here: the root is parallel and each region is one responsibility, named by the ID of the DrawableDocumentChainSupport capability it runs. The worker only interprets this file; it never adds, removes or renames states or regions. ontobdc currently ships no capability implementing DrawableDocumentChainSupport, so the chain declares no responsibility region. A responsibility is declared as one region of this shape: - name: &lt;responsibility&gt; initial: &lt;responsibility&gt;\_pending states: - name: &lt;responsibility&gt;\_pending transitions: - target: &lt;responsibility&gt;\_completed guard: worker.can\_handle('&lt;capability id&gt;') action: worker.execute\_responsibility('&lt;capability id&gt;') - target: &lt;responsibility&gt;\_completed guard: not worker.can\_handle('&lt;capability id&gt;') - name: &lt;responsibility&gt;\_completed type: final


    </div>

    <div class="fsm-reference-machine" markdown="1">

    ### `DrawableFileViewerChain` { #fsm-drawablefileviewerchain }



    <div class="cli-reference-label">Descrição</div>

    Fallback chain run by DRAWABLE\_FILE\_VIEWER\_OPENED when the context maps no capability to the file's MIME type. The complete topology is declared here: the root is parallel and each region is one responsibility, named by the ID of the DrawableFileViewerChainSupport capability it runs. The worker only interprets this file; it never adds, removes or renames states or regions. ontobdc currently ships no capability implementing DrawableFileViewerChainSupport, so the chain declares no responsibility region. A responsibility is declared as one region of this shape: - name: &lt;responsibility&gt; initial: &lt;responsibility&gt;\_pending states: - name: &lt;responsibility&gt;\_pending transitions: - target: &lt;responsibility&gt;\_completed guard: worker.can\_handle('&lt;capability id&gt;') action: worker.execute\_responsibility('&lt;capability id&gt;') - target: &lt;responsibility&gt;\_completed guard: not worker.can\_handle('&lt;capability id&gt;') - name: &lt;responsibility&gt;\_completed type: final


    </div>

    <div class="fsm-reference-machine" markdown="1">

    ### `PointsCapturedChain` { #fsm-pointscapturedchain }



    <div class="cli-reference-label">Descrição</div>

    Fallback chain run by POINTS\_CAPTURED when the context maps no capability to the file's MIME type. The complete topology is declared here: the root is parallel and each region is one responsibility, named by the ID of the PointsCapturedChainSupport capability it runs. The worker only interprets this file; it never adds, removes or renames states or regions. ontobdc currently ships no capability implementing PointsCapturedChainSupport, so the chain declares no responsibility region. A responsibility is declared as one region of this shape: - name: &lt;responsibility&gt; initial: &lt;responsibility&gt;\_pending states: - name: &lt;responsibility&gt;\_pending transitions: - target: &lt;responsibility&gt;\_completed guard: worker.can\_handle('&lt;capability id&gt;') action: worker.execute\_responsibility('&lt;capability id&gt;') - target: &lt;responsibility&gt;\_completed guard: not worker.can\_handle('&lt;capability id&gt;') - name: &lt;responsibility&gt;\_completed type: final


    </div>
