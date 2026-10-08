# Referencia de FSM — context

Máquinas de estados finitos declaradas por `context` en `infobim`.


<div class="fsm-reference-index" markdown="1">

| Nombre | Descripción |
| --- | --- |
| [`DictionaryInspection`](#fsm-dictionaryinspection) | Statechart for generic semantic dictionary inspection of arbitrary text. |
| [`FileMeaningSuggestion`](#fsm-filemeaningsuggestion) | Statechart for semantic file meaning suggestions derived from paths. |
| [`PdfToGraph`](#fsm-pdftograph) | Statechart for transforming PDF documents into knowledge graph inputs. |

</div>


<div class="fsm-reference-machine" markdown="1">

### `DictionaryInspection` { #fsm-dictionaryinspection }



<div class="cli-reference-label">Descripción</div>

Statechart for generic semantic dictionary inspection of arbitrary text.


<div class="cli-reference-label">Estados</div>

<div class="fsm-reference-states" markdown="1">


<div class="fsm-reference-state" markdown="1">

Undefined

<span class="fsm-reference-value">`__undefined__`</span>

<span class="fsm-reference-description">Initial state before the input text has been normalized.</span>



</div>

<span class="fsm-reference-arrow">↓</span>



<div class="fsm-reference-state" markdown="1">

Text Normalized

<span class="fsm-reference-value">`__text_normalized__`</span>

<span class="fsm-reference-description">The input text has a deterministic normalized representation.</span>


<span class="fsm-reference-capability"><span class="fsm-reference-capability-label">Capability</span>: `src/ontobdc/context/plugin/capability/transformation/text_normalized.py`</span>


</div>

<span class="fsm-reference-arrow">↓</span>



<div class="fsm-reference-state" markdown="1">

Text Language Identified

<span class="fsm-reference-value">`__text_language_identified__`</span>

<span class="fsm-reference-description">The language of the normalized text has been identified.</span>


<span class="fsm-reference-capability"><span class="fsm-reference-capability-label">Capability</span>: `src/ontobdc/context/plugin/capability/transformation/text_language_identified.py`</span>


</div>

<span class="fsm-reference-arrow">↓</span>



<div class="fsm-reference-state" markdown="1">

Text Lemmatized

<span class="fsm-reference-value">`__text_lemmatized__`</span>

<span class="fsm-reference-description">The normalized text has been reduced to language-aware lemmas.</span>


<span class="fsm-reference-capability"><span class="fsm-reference-capability-label">Capability</span>: `src/ontobdc/context/plugin/capability/transformation/text_lemmatized.py`</span>


</div>

<span class="fsm-reference-arrow">↓</span>



<div class="fsm-reference-state" markdown="1">

Ontology Term Resolved

<span class="fsm-reference-value">`__ontology_term_resolved__`</span>

<span class="fsm-reference-description">The lemmatized text has been resolved against the ontology dictionary using exact or fuzzy matching.</span>


<span class="fsm-reference-capability"><span class="fsm-reference-capability-label">Capability</span>: `src/ontobdc/context/plugin/capability/transformation/ontology_term_resolved.py`</span>


</div>

<span class="fsm-reference-arrow">↓</span>



<div class="fsm-reference-state" markdown="1">

Kind Representation Resolved

<span class="fsm-reference-value">`__kind_representation_resolved__`</span>

<span class="fsm-reference-description">The representations declared for every resolved ontology term have been fetched.</span>


<span class="fsm-reference-capability"><span class="fsm-reference-capability-label">Capability</span>: `src/ontobdc/context/plugin/capability/transformation/kind_representation_resolved.py`</span>


</div>

<span class="fsm-reference-arrow">↓</span>



<div class="fsm-reference-state" markdown="1">

Markdown Rendered <span class="fsm-reference-final">final</span>

<span class="fsm-reference-value">`__markdown_rendered__`</span>

<span class="fsm-reference-description">The dictionary inspection result has been rendered and persisted as a Markdown ETL state file.</span>


<span class="fsm-reference-capability"><span class="fsm-reference-capability-label">Capability</span>: `src/ontobdc/context/plugin/capability/persister/dictionary_inspection_markdown_rendered.py`</span>


</div>



</div>

</div>

<div class="fsm-reference-machine" markdown="1">

### `FileMeaningSuggestion` { #fsm-filemeaningsuggestion }



<div class="cli-reference-label">Descripción</div>

Statechart for semantic file meaning suggestions derived from paths.


<div class="cli-reference-label">Estados</div>

<div class="fsm-reference-states" markdown="1">


<div class="fsm-reference-state" markdown="1">

Undefined

<span class="fsm-reference-value">`__undefined__`</span>

<span class="fsm-reference-description">Initial state before the source file path has been normalized.</span>



</div>

<span class="fsm-reference-arrow">↓</span>



<div class="fsm-reference-state" markdown="1">

Path Normalized

<span class="fsm-reference-value">`__path_normalized__`</span>

<span class="fsm-reference-description">The source path has a normalized representation ready for language identification.</span>



</div>

<span class="fsm-reference-arrow">↓</span>



<div class="fsm-reference-state" markdown="1">

Path Language Identified

<span class="fsm-reference-value">`__path_language_identified__`</span>

<span class="fsm-reference-description">The language of the normalized path has been identified for lemmatization.</span>



</div>

<span class="fsm-reference-arrow">↓</span>



<div class="fsm-reference-state" markdown="1">

File Metadata Extracted

<span class="fsm-reference-value">`__file_metadata_extracted__`</span>

<span class="fsm-reference-description">Metadata relevant to semantic matching has been extracted from the normalized file path.</span>



</div>

<span class="fsm-reference-arrow">↓</span>



<div class="fsm-reference-state" markdown="1">

Path Lemmatized

<span class="fsm-reference-value">`__path_lemmatized__`</span>

<span class="fsm-reference-description">The normalized path has been reduced to its lemma, ready for token-level corpus statistics.</span>



</div>

<span class="fsm-reference-arrow">↓</span>



<div class="fsm-reference-state" markdown="1">

Token Statistics Computed

<span class="fsm-reference-value">`__token_statistics_computed__`</span>

<span class="fsm-reference-description">Deterministic token-level corpus statistics have been computed from every lemmatized path.</span>



</div>

<span class="fsm-reference-arrow">↓</span>



<div class="fsm-reference-state" markdown="1">

Chunk Candidates Generated

<span class="fsm-reference-value">`__chunk_candidates_generated__`</span>

<span class="fsm-reference-description">Contiguous multi-token expressions have been generated as chunk candidates with traceable corpus evidence.</span>



</div>

<span class="fsm-reference-arrow">↓</span>



<div class="fsm-reference-state" markdown="1">

Chunks Extracted

<span class="fsm-reference-value">`__chunks_extracted__`</span>

<span class="fsm-reference-description">Statistically supported chunk candidates have been promoted to deterministic accepted chunks.</span>



</div>

<span class="fsm-reference-arrow">↓</span>



<div class="fsm-reference-state" markdown="1">

Ontology Terms Matched

<span class="fsm-reference-value">`__ontology_terms_matched__`</span>

<span class="fsm-reference-description">Accepted chunks have been matched against explicitly declared ontology terms.</span>



</div>

<span class="fsm-reference-arrow">↓</span>



<div class="fsm-reference-state" markdown="1">

Category Candidates Found <span class="fsm-reference-final">final</span>

<span class="fsm-reference-value">`__category_candidates_found__`</span>

<span class="fsm-reference-description">Hierarchical category candidates grouped per ro-crate file, then per ontology category, then per chunk. Exact=1.0, fuzzy=min(len)/max(len) substring ratio, unmatched=0 with synthetic bucket.</span>



</div>



</div>

</div>

<div class="fsm-reference-machine" markdown="1">

### `PdfToGraph` { #fsm-pdftograph }



<div class="cli-reference-label">Descripción</div>

Statechart for transforming PDF documents into knowledge graph inputs.


<div class="cli-reference-label">Estados</div>

<div class="fsm-reference-states" markdown="1">


<div class="fsm-reference-state" markdown="1">

Undefined

<span class="fsm-reference-value">`__undefined__`</span>

<span class="fsm-reference-description">Initial state before the PDF-to-graph pipeline has started.</span>



</div>

<span class="fsm-reference-arrow">↓</span>



<div class="fsm-reference-state" markdown="1">

PDF Text Readiness Verified

<span class="fsm-reference-value">`__text_readiness_checked__`</span>

<span class="fsm-reference-description">The PDF was verified to contain enough extractable plain text for knowledge graph authoring.</span>


<span class="fsm-reference-capability"><span class="fsm-reference-capability-label">Capability</span>: `src/ontobdc/context/plugin/capability/transformation/text_readiness.py`</span>


</div>

<span class="fsm-reference-arrow">↓</span>



<div class="fsm-reference-state" markdown="1">

PDF Text Blocks Extracted <span class="fsm-reference-final">final</span>

<span class="fsm-reference-value">`__pdf_blocks_extracted__`</span>

<span class="fsm-reference-description">Positioned text blocks were extracted from every page of the PDF using PyMuPDF.</span>


<span class="fsm-reference-capability"><span class="fsm-reference-capability-label">Capability</span>: `src/ontobdc/context/plugin/capability/transformation/pdf_block.py`</span>


</div>



</div>

</div>
