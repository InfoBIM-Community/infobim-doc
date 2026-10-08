# Referência de FSM — context

Máquinas de estado finito declaradas por `context` em `infobim`.


<div class="fsm-reference-index" markdown="1">

| Nome | Descrição |
| --- | --- |
| [`DictionaryInspection`](#fsm-dictionaryinspection) | Statechart for generic semantic dictionary inspection of arbitrary text. |
| [`FileMeaningSuggestion`](#fsm-filemeaningsuggestion) | Statechart for semantic file meaning suggestions derived from paths. |
| [`PdfToGraph`](#fsm-pdftograph) | Statechart for transforming PDF documents into knowledge graph inputs. |

</div>


<div class="fsm-reference-machine" markdown="1">

### `DictionaryInspection` { #fsm-dictionaryinspection }



<div class="cli-reference-label">Descrição</div>

Statechart for generic semantic dictionary inspection of arbitrary text.


<div class="cli-reference-label">Estados</div>

<div class="fsm-reference-states" markdown="1">


<div class="fsm-reference-state" markdown="1">

Indefinido

<span class="fsm-reference-value">`__undefined__`</span>

<span class="fsm-reference-description">Estado inicial antes da normalizacao do texto de entrada.</span>



</div>

<span class="fsm-reference-arrow">↓</span>



<div class="fsm-reference-state" markdown="1">

Texto Normalizado

<span class="fsm-reference-value">`__text_normalized__`</span>

<span class="fsm-reference-description">O texto de entrada possui uma representacao normalizada deterministica.</span>


<span class="fsm-reference-capability"><span class="fsm-reference-capability-label">Capability</span>: `src/ontobdc/context/plugin/capability/transformation/text_normalized.py`</span>


</div>

<span class="fsm-reference-arrow">↓</span>



<div class="fsm-reference-state" markdown="1">

Idioma do Texto Identificado

<span class="fsm-reference-value">`__text_language_identified__`</span>

<span class="fsm-reference-description">O idioma do texto normalizado foi identificado.</span>


<span class="fsm-reference-capability"><span class="fsm-reference-capability-label">Capability</span>: `src/ontobdc/context/plugin/capability/transformation/text_language_identified.py`</span>


</div>

<span class="fsm-reference-arrow">↓</span>



<div class="fsm-reference-state" markdown="1">

Texto Lematizado

<span class="fsm-reference-value">`__text_lemmatized__`</span>

<span class="fsm-reference-description">O texto normalizado foi reduzido a lemas dependentes do idioma.</span>


<span class="fsm-reference-capability"><span class="fsm-reference-capability-label">Capability</span>: `src/ontobdc/context/plugin/capability/transformation/text_lemmatized.py`</span>


</div>

<span class="fsm-reference-arrow">↓</span>



<div class="fsm-reference-state" markdown="1">

Termo da Ontologia Resolvido

<span class="fsm-reference-value">`__ontology_term_resolved__`</span>

<span class="fsm-reference-description">O texto lematizado foi resolvido contra o dicionario de ontologias por correspondencia exata ou fuzzy.</span>


<span class="fsm-reference-capability"><span class="fsm-reference-capability-label">Capability</span>: `src/ontobdc/context/plugin/capability/transformation/ontology_term_resolved.py`</span>


</div>

<span class="fsm-reference-arrow">↓</span>



<div class="fsm-reference-state" markdown="1">

Representacao do Tipo Resolvida

<span class="fsm-reference-value">`__kind_representation_resolved__`</span>

<span class="fsm-reference-description">As representacoes declaradas para cada termo resolvido foram obtidas.</span>


<span class="fsm-reference-capability"><span class="fsm-reference-capability-label">Capability</span>: `src/ontobdc/context/plugin/capability/transformation/kind_representation_resolved.py`</span>


</div>

<span class="fsm-reference-arrow">↓</span>



<div class="fsm-reference-state" markdown="1">

Markdown Renderizado <span class="fsm-reference-final">final</span>

<span class="fsm-reference-value">`__markdown_rendered__`</span>

<span class="fsm-reference-description">O resultado da inspecao do dicionario foi renderizado e persistido como arquivo de estado ETL Markdown.</span>


<span class="fsm-reference-capability"><span class="fsm-reference-capability-label">Capability</span>: `src/ontobdc/context/plugin/capability/persister/dictionary_inspection_markdown_rendered.py`</span>


</div>



</div>

</div>

<div class="fsm-reference-machine" markdown="1">

### `FileMeaningSuggestion` { #fsm-filemeaningsuggestion }



<div class="cli-reference-label">Descrição</div>

Statechart for semantic file meaning suggestions derived from paths.


<div class="cli-reference-label">Estados</div>

<div class="fsm-reference-states" markdown="1">


<div class="fsm-reference-state" markdown="1">

Indefinido

<span class="fsm-reference-value">`__undefined__`</span>

<span class="fsm-reference-description">Estado inicial antes da normalizacao do caminho do arquivo de origem.</span>



</div>

<span class="fsm-reference-arrow">↓</span>



<div class="fsm-reference-state" markdown="1">

Caminho Normalizado

<span class="fsm-reference-value">`__path_normalized__`</span>

<span class="fsm-reference-description">O caminho de origem possui uma representacao normalizada pronta para identificacao de idioma.</span>



</div>

<span class="fsm-reference-arrow">↓</span>



<div class="fsm-reference-state" markdown="1">

Idioma do Caminho Identificado

<span class="fsm-reference-value">`__path_language_identified__`</span>

<span class="fsm-reference-description">O idioma do caminho normalizado foi identificado para lematizacao.</span>



</div>

<span class="fsm-reference-arrow">↓</span>



<div class="fsm-reference-state" markdown="1">

Metadados do Arquivo Extraidos

<span class="fsm-reference-value">`__file_metadata_extracted__`</span>

<span class="fsm-reference-description">Os metadados relevantes para correspondencia semantica foram extraidos do caminho normalizado do arquivo.</span>



</div>

<span class="fsm-reference-arrow">↓</span>



<div class="fsm-reference-state" markdown="1">

Caminho Lematizado

<span class="fsm-reference-value">`__path_lemmatized__`</span>

<span class="fsm-reference-description">O caminho normalizado foi reduzido ao seu lema, pronto para estatisticas de corpus em nivel de token.</span>



</div>

<span class="fsm-reference-arrow">↓</span>



<div class="fsm-reference-state" markdown="1">

Estatisticas de Token Computadas

<span class="fsm-reference-value">`__token_statistics_computed__`</span>

<span class="fsm-reference-description">Estatisticas deterministicas de corpus em nivel de token foram computadas a partir de cada caminho lematizado.</span>



</div>

<span class="fsm-reference-arrow">↓</span>



<div class="fsm-reference-state" markdown="1">

Candidatos a Chunk Gerados

<span class="fsm-reference-value">`__chunk_candidates_generated__`</span>

<span class="fsm-reference-description">Expressoes contiguas de multiplos tokens foram geradas como candidatos a chunk com evidencias rastreaveis do corpus.</span>



</div>

<span class="fsm-reference-arrow">↓</span>



<div class="fsm-reference-state" markdown="1">

Chunks Extraidos

<span class="fsm-reference-value">`__chunks_extracted__`</span>

<span class="fsm-reference-description">Os candidatos a chunk com suporte estatistico foram promovidos a chunks aceitos de forma deterministica.</span>



</div>

<span class="fsm-reference-arrow">↓</span>



<div class="fsm-reference-state" markdown="1">

Termos da Ontologia Correspondidos

<span class="fsm-reference-value">`__ontology_terms_matched__`</span>

<span class="fsm-reference-description">Os chunks aceitos foram comparados com termos explicitamente declarados na ontologia.</span>



</div>

<span class="fsm-reference-arrow">↓</span>



<div class="fsm-reference-state" markdown="1">

Candidatos de Categoria Encontrados <span class="fsm-reference-final">final</span>

<span class="fsm-reference-value">`__category_candidates_found__`</span>

<span class="fsm-reference-description">Candidatos de categoria hierarquicos agrupados por arquivo do ro-crate, depois por categoria da ontologia, depois por chunk. Exato=1.0, fuzzy=min/comprimento/max(comprimento) por substring, nao-match=0 em bucket sintetico.</span>



</div>



</div>

</div>

<div class="fsm-reference-machine" markdown="1">

### `PdfToGraph` { #fsm-pdftograph }



<div class="cli-reference-label">Descrição</div>

Statechart for transforming PDF documents into knowledge graph inputs.


<div class="cli-reference-label">Estados</div>

<div class="fsm-reference-states" markdown="1">


<div class="fsm-reference-state" markdown="1">

Indefinido

<span class="fsm-reference-value">`__undefined__`</span>

<span class="fsm-reference-description">Estado inicial antes do pipeline PDF-para-grafo começar.</span>



</div>

<span class="fsm-reference-arrow">↓</span>



<div class="fsm-reference-state" markdown="1">

Legibilidade de Texto do PDF Verificada

<span class="fsm-reference-value">`__text_readiness_checked__`</span>

<span class="fsm-reference-description">O PDF foi verificado e contém texto plano extraível suficiente para autoria de grafo de conhecimento.</span>


<span class="fsm-reference-capability"><span class="fsm-reference-capability-label">Capability</span>: `src/ontobdc/context/plugin/capability/transformation/text_readiness.py`</span>


</div>

<span class="fsm-reference-arrow">↓</span>



<div class="fsm-reference-state" markdown="1">

Blocos de Texto do PDF Extraídos <span class="fsm-reference-final">final</span>

<span class="fsm-reference-value">`__pdf_blocks_extracted__`</span>

<span class="fsm-reference-description">Blocos de texto posicionados foram extraídos de cada página do PDF com PyMuPDF.</span>


<span class="fsm-reference-capability"><span class="fsm-reference-capability-label">Capability</span>: `src/ontobdc/context/plugin/capability/transformation/pdf_block.py`</span>


</div>



</div>

</div>
