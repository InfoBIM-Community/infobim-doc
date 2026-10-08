# Referencia de FSM — annotation

Máquinas de estados finitos declaradas por `annotation` en `infobim`.


=== "FSM"

    <div class="fsm-reference-index" markdown="1">

    | Nombre | Descripción |
    | --- | --- |
    | [`StandardAnnotationCreationFromPoint`](#fsm-standardannotationcreationfrompoint) | Identify the type of an annotation, then create annotations of that type at points picked on a drawing. |
    | [`StandardAnnotationExportToExcel`](#fsm-standardannotationexporttoexcel) | Export the annotations of one type to an Excel workbook that embeds the reduced photos they refer to. |

    </div>

    
    <div class="fsm-reference-machine" markdown="1">

    ### `StandardAnnotationCreationFromPoint` { #fsm-standardannotationcreationfrompoint }

    <div class="fsm-reference-title" markdown="1">Annotation Creation from Point</div>

    <div class="cli-reference-label">Descripción</div>

    Identify the type of an annotation, then create annotations of that type at points picked on a drawing.


    <div class="cli-reference-label">Estados</div>

    <div class="fsm-reference-states" markdown="1">


    <div class="fsm-reference-state" markdown="1">

    Undefined

    <span class="fsm-reference-value">`__undefined__`</span>

    <span class="fsm-reference-description">Initial state before the type of the annotation is identified.</span>



    </div>

    <span class="fsm-reference-arrow">↓</span>



    <div class="fsm-reference-state" markdown="1">

    Annotation Type Identified

    <span class="fsm-reference-value">`__annotation_type_identified__`</span>

    <span class="fsm-reference-description">The type of the annotation to create has been identified.</span>


    <span class="fsm-reference-capability"><span class="fsm-reference-capability-label">Capability</span>: `src/ontobdc/annotation/plugin/capability/transformation/annotation_type_identified.py`</span>


    </div>

    <span class="fsm-reference-arrow">↓</span>



    <div class="fsm-reference-state" markdown="1">

    File Metadata Extracted

    <span class="fsm-reference-value">`__file_metadata_extracted__`</span>

    <span class="fsm-reference-description">The MIME type and filesystem metadata of the requested drawing file have been extracted.</span>


    <span class="fsm-reference-capability"><span class="fsm-reference-capability-label">Capability</span>: `src/ontobdc/storage/plugin/capability/transformation/single_file_metadata_extracted.py`</span>


    </div>

    <span class="fsm-reference-arrow">↓</span>



    <div class="fsm-reference-state" markdown="1">

    Drawable Documents Loaded

    <span class="fsm-reference-value">`__drawable_documents_loaded__`</span>

    <span class="fsm-reference-description">The requested drawing, converted from DWG when needed, has been loaded as the original DXF document.</span>


    <span class="fsm-reference-capability"><span class="fsm-reference-capability-label">Capability</span>: `src/ontobdc/annotation/plugin/capability/loader/drawable_documents_loaded.py`</span>


    </div>

    <span class="fsm-reference-arrow">↓</span>



    <div class="fsm-reference-state" markdown="1">

    Drawable File Viewer Opened

    <span class="fsm-reference-value">`__drawable_file_viewer_opened__`</span>

    <span class="fsm-reference-description">The loaded drawing has been opened in a 2D viewer window that stays open for the point capture.</span>


    <span class="fsm-reference-capability"><span class="fsm-reference-capability-label">Capability</span>: `src/ontobdc/annotation/plugin/capability/loader/drawable_file_viewer_opened.py`</span>


    </div>

    <span class="fsm-reference-arrow">↓</span>



    <div class="fsm-reference-state" markdown="1">

    Points Captured

    <span class="fsm-reference-value">`__points_captured__`</span>

    <span class="fsm-reference-description">The points at which the annotations are placed have been picked on the open viewer window, in click order.</span>


    <span class="fsm-reference-capability"><span class="fsm-reference-capability-label">Capability</span>: `src/ontobdc/annotation/plugin/capability/loader/points_captured.py`</span>


    </div>

    <span class="fsm-reference-arrow">↓</span>



    <div class="fsm-reference-state" markdown="1">

    Annotation Details Filled

    <span class="fsm-reference-value">`__annotation_details_filled__`</span>

    <span class="fsm-reference-description">The title, the text and the author of the annotations have been filled in by the person who picked the points.</span>


    <span class="fsm-reference-capability"><span class="fsm-reference-capability-label">Capability</span>: `src/ontobdc/annotation/plugin/capability/loader/annotation_details_filled.py`</span>


    </div>

    <span class="fsm-reference-arrow">↓</span>



    <div class="fsm-reference-state" markdown="1">

    Annotations Created <span class="fsm-reference-final">final</span>

    <span class="fsm-reference-value">`__annotations_created__`</span>

    <span class="fsm-reference-description">Annotations of the identified type have been created at the captured points.</span>


    <span class="fsm-reference-capability"><span class="fsm-reference-capability-label">Capability</span>: `src/ontobdc/annotation/plugin/capability/transformation/annotations_created.py`</span>


    </div>



    </div>

    </div>

    <div class="fsm-reference-machine" markdown="1">

    ### `StandardAnnotationExportToExcel` { #fsm-standardannotationexporttoexcel }

    <div class="fsm-reference-title" markdown="1">Annotation Export to Excel</div>

    <div class="cli-reference-label">Descripción</div>

    Export the annotations of one type to an Excel workbook that embeds the reduced photos they refer to.


    <div class="cli-reference-label">Estados</div>

    <div class="fsm-reference-states" markdown="1">


    <div class="fsm-reference-state" markdown="1">

    Undefined

    <span class="fsm-reference-value">`__undefined__`</span>

    <span class="fsm-reference-description">Initial state before the scope of the export is identified.</span>



    </div>

    <span class="fsm-reference-arrow">↓</span>



    <div class="fsm-reference-state" markdown="1">

    Export Scope Identified

    <span class="fsm-reference-value">`__export_scope_identified__`</span>

    <span class="fsm-reference-description">The annotation type to export and the container that keeps its annotations have been identified.</span>


    <span class="fsm-reference-capability"><span class="fsm-reference-capability-label">Capability</span>: `src/ontobdc/annotation/plugin/capability/transformation/export_scope_identified.py`</span>


    </div>

    <span class="fsm-reference-arrow">↓</span>



    <div class="fsm-reference-state" markdown="1">

    Annotations Collected

    <span class="fsm-reference-value">`__annotations_collected__`</span>

    <span class="fsm-reference-description">The annotations of the identified type have been read from the container and numbered.</span>


    <span class="fsm-reference-capability"><span class="fsm-reference-capability-label">Capability</span>: `src/ontobdc/annotation/plugin/capability/transformation/annotations_collected.py`</span>


    </div>

    <span class="fsm-reference-arrow">↓</span>



    <div class="fsm-reference-state" markdown="1">

    Photos Collected

    <span class="fsm-reference-value">`__photos_collected__`</span>

    <span class="fsm-reference-description">The images among the files each annotation refers to have been found in the container and numbered.</span>


    <span class="fsm-reference-capability"><span class="fsm-reference-capability-label">Capability</span>: `src/ontobdc/annotation/plugin/capability/transformation/photos_collected.py`</span>


    </div>

    <span class="fsm-reference-arrow">↓</span>



    <div class="fsm-reference-state" markdown="1">

    Photos Downsampled

    <span class="fsm-reference-value">`__photos_downsampled__`</span>

    <span class="fsm-reference-description">Each photo has been reduced to a lighter image to be embedded in the workbook.</span>


    <span class="fsm-reference-capability"><span class="fsm-reference-capability-label">Capability</span>: `src/ontobdc/annotation/plugin/capability/transformation/photos_downsampled.py`</span>


    </div>

    <span class="fsm-reference-arrow">↓</span>



    <div class="fsm-reference-state" markdown="1">

    Workbook Built

    <span class="fsm-reference-value">`__workbook_built__`</span>

    <span class="fsm-reference-description">The workbook with the index of annotations, the photo archive and the carousel of each item has been built.</span>


    <span class="fsm-reference-capability"><span class="fsm-reference-capability-label">Capability</span>: `src/ontobdc/annotation/plugin/capability/transformation/workbook_built.py`</span>


    </div>

    <span class="fsm-reference-arrow">↓</span>



    <div class="fsm-reference-state" markdown="1">

    Workbook Saved <span class="fsm-reference-final">final</span>

    <span class="fsm-reference-value">`__workbook_saved__`</span>

    <span class="fsm-reference-description">The workbook has been saved and is ready to be received.</span>


    <span class="fsm-reference-capability"><span class="fsm-reference-capability-label">Capability</span>: `src/ontobdc/annotation/plugin/capability/transformation/workbook_saved.py`</span>


    </div>



    </div>

    </div>


=== "Cadenas"

    <div class="fsm-reference-index" markdown="1">

    | Nombre | Descripción |
    | --- | --- |
    | [`AnnotationDetailsChain`](#fsm-annotationdetailschain) | Fallback chain run by ANNOTATION\_DETAILS\_FILLED when the context maps no capability to the file's MIME type. The complete topology is declared here: the root is parallel and each region is one responsibility, named by the ID of the AnnotationDetailsChainSupport capability it runs. The worker only interprets this file; it never adds, removes or renames states or regions. ontobdc currently ships no capability implementing AnnotationDetailsChainSupport, so the chain declares no responsibility region. A responsibility is declared as one region of this shape: - name: &lt;responsibility&gt; initial: &lt;responsibility&gt;\_pending states: - name: &lt;responsibility&gt;\_pending transitions: - target: &lt;responsibility&gt;\_completed guard: worker.can\_handle('&lt;capability id&gt;') action: worker.execute\_responsibility('&lt;capability id&gt;') - target: &lt;responsibility&gt;\_completed guard: not worker.can\_handle('&lt;capability id&gt;') - name: &lt;responsibility&gt;\_completed type: final |
    | [`DrawableDocumentsChain`](#fsm-drawabledocumentschain) | Fallback chain run by DRAWABLE\_DOCUMENTS\_LOADED when the context maps no capability to the file's MIME type. The complete topology is declared here: the root is parallel and each region is one responsibility, named by the ID of the DrawableDocumentChainSupport capability it runs. The worker only interprets this file; it never adds, removes or renames states or regions. ontobdc currently ships no capability implementing DrawableDocumentChainSupport, so the chain declares no responsibility region. A responsibility is declared as one region of this shape: - name: &lt;responsibility&gt; initial: &lt;responsibility&gt;\_pending states: - name: &lt;responsibility&gt;\_pending transitions: - target: &lt;responsibility&gt;\_completed guard: worker.can\_handle('&lt;capability id&gt;') action: worker.execute\_responsibility('&lt;capability id&gt;') - target: &lt;responsibility&gt;\_completed guard: not worker.can\_handle('&lt;capability id&gt;') - name: &lt;responsibility&gt;\_completed type: final |
    | [`DrawableFileViewerChain`](#fsm-drawablefileviewerchain) | Fallback chain run by DRAWABLE\_FILE\_VIEWER\_OPENED when the context maps no capability to the file's MIME type. The complete topology is declared here: the root is parallel and each region is one responsibility, named by the ID of the DrawableFileViewerChainSupport capability it runs. The worker only interprets this file; it never adds, removes or renames states or regions. ontobdc currently ships no capability implementing DrawableFileViewerChainSupport, so the chain declares no responsibility region. A responsibility is declared as one region of this shape: - name: &lt;responsibility&gt; initial: &lt;responsibility&gt;\_pending states: - name: &lt;responsibility&gt;\_pending transitions: - target: &lt;responsibility&gt;\_completed guard: worker.can\_handle('&lt;capability id&gt;') action: worker.execute\_responsibility('&lt;capability id&gt;') - target: &lt;responsibility&gt;\_completed guard: not worker.can\_handle('&lt;capability id&gt;') - name: &lt;responsibility&gt;\_completed type: final |
    | [`PointsCapturedChain`](#fsm-pointscapturedchain) | Fallback chain run by POINTS\_CAPTURED when the context maps no capability to the file's MIME type. The complete topology is declared here: the root is parallel and each region is one responsibility, named by the ID of the PointsCapturedChainSupport capability it runs. The worker only interprets this file; it never adds, removes or renames states or regions. ontobdc currently ships no capability implementing PointsCapturedChainSupport, so the chain declares no responsibility region. A responsibility is declared as one region of this shape: - name: &lt;responsibility&gt; initial: &lt;responsibility&gt;\_pending states: - name: &lt;responsibility&gt;\_pending transitions: - target: &lt;responsibility&gt;\_completed guard: worker.can\_handle('&lt;capability id&gt;') action: worker.execute\_responsibility('&lt;capability id&gt;') - target: &lt;responsibility&gt;\_completed guard: not worker.can\_handle('&lt;capability id&gt;') - name: &lt;responsibility&gt;\_completed type: final |

    </div>

    
    <div class="fsm-reference-machine" markdown="1">

    ### `AnnotationDetailsChain` { #fsm-annotationdetailschain }



    <div class="cli-reference-label">Descripción</div>

    Fallback chain run by ANNOTATION\_DETAILS\_FILLED when the context maps no capability to the file's MIME type. The complete topology is declared here: the root is parallel and each region is one responsibility, named by the ID of the AnnotationDetailsChainSupport capability it runs. The worker only interprets this file; it never adds, removes or renames states or regions. ontobdc currently ships no capability implementing AnnotationDetailsChainSupport, so the chain declares no responsibility region. A responsibility is declared as one region of this shape: - name: &lt;responsibility&gt; initial: &lt;responsibility&gt;\_pending states: - name: &lt;responsibility&gt;\_pending transitions: - target: &lt;responsibility&gt;\_completed guard: worker.can\_handle('&lt;capability id&gt;') action: worker.execute\_responsibility('&lt;capability id&gt;') - target: &lt;responsibility&gt;\_completed guard: not worker.can\_handle('&lt;capability id&gt;') - name: &lt;responsibility&gt;\_completed type: final


    </div>

    <div class="fsm-reference-machine" markdown="1">

    ### `DrawableDocumentsChain` { #fsm-drawabledocumentschain }



    <div class="cli-reference-label">Descripción</div>

    Fallback chain run by DRAWABLE\_DOCUMENTS\_LOADED when the context maps no capability to the file's MIME type. The complete topology is declared here: the root is parallel and each region is one responsibility, named by the ID of the DrawableDocumentChainSupport capability it runs. The worker only interprets this file; it never adds, removes or renames states or regions. ontobdc currently ships no capability implementing DrawableDocumentChainSupport, so the chain declares no responsibility region. A responsibility is declared as one region of this shape: - name: &lt;responsibility&gt; initial: &lt;responsibility&gt;\_pending states: - name: &lt;responsibility&gt;\_pending transitions: - target: &lt;responsibility&gt;\_completed guard: worker.can\_handle('&lt;capability id&gt;') action: worker.execute\_responsibility('&lt;capability id&gt;') - target: &lt;responsibility&gt;\_completed guard: not worker.can\_handle('&lt;capability id&gt;') - name: &lt;responsibility&gt;\_completed type: final


    </div>

    <div class="fsm-reference-machine" markdown="1">

    ### `DrawableFileViewerChain` { #fsm-drawablefileviewerchain }



    <div class="cli-reference-label">Descripción</div>

    Fallback chain run by DRAWABLE\_FILE\_VIEWER\_OPENED when the context maps no capability to the file's MIME type. The complete topology is declared here: the root is parallel and each region is one responsibility, named by the ID of the DrawableFileViewerChainSupport capability it runs. The worker only interprets this file; it never adds, removes or renames states or regions. ontobdc currently ships no capability implementing DrawableFileViewerChainSupport, so the chain declares no responsibility region. A responsibility is declared as one region of this shape: - name: &lt;responsibility&gt; initial: &lt;responsibility&gt;\_pending states: - name: &lt;responsibility&gt;\_pending transitions: - target: &lt;responsibility&gt;\_completed guard: worker.can\_handle('&lt;capability id&gt;') action: worker.execute\_responsibility('&lt;capability id&gt;') - target: &lt;responsibility&gt;\_completed guard: not worker.can\_handle('&lt;capability id&gt;') - name: &lt;responsibility&gt;\_completed type: final


    </div>

    <div class="fsm-reference-machine" markdown="1">

    ### `PointsCapturedChain` { #fsm-pointscapturedchain }



    <div class="cli-reference-label">Descripción</div>

    Fallback chain run by POINTS\_CAPTURED when the context maps no capability to the file's MIME type. The complete topology is declared here: the root is parallel and each region is one responsibility, named by the ID of the PointsCapturedChainSupport capability it runs. The worker only interprets this file; it never adds, removes or renames states or regions. ontobdc currently ships no capability implementing PointsCapturedChainSupport, so the chain declares no responsibility region. A responsibility is declared as one region of this shape: - name: &lt;responsibility&gt; initial: &lt;responsibility&gt;\_pending states: - name: &lt;responsibility&gt;\_pending transitions: - target: &lt;responsibility&gt;\_completed guard: worker.can\_handle('&lt;capability id&gt;') action: worker.execute\_responsibility('&lt;capability id&gt;') - target: &lt;responsibility&gt;\_completed guard: not worker.can\_handle('&lt;capability id&gt;') - name: &lt;responsibility&gt;\_completed type: final


    </div>
