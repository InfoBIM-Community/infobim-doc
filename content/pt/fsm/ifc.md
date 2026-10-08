# Referência de FSM — ifc

Máquinas de estado finito declaradas por `ifc` em `infobim`.


=== "FSM"

    <div class="fsm-reference-index" markdown="1">

    | Nome | Descrição |
    | --- | --- |
    | [`StandardGeometricProductCreate`](#fsm-standardgeometricproductcreate) | Statechart for creating a geometric product in an InfoBIM project's IFC model. |
    | [`StandardGeometricProductDelete`](#fsm-standardgeometricproductdelete) | Statechart for deleting a geometric product (by GlobalId) from an InfoBIM project's IFC model. |
    | [`StandardIfcModelCreate`](#fsm-standardifcmodelcreate) | Statechart for creating the IFC model file an InfoBIM project writes its own elements into. |

    </div>

    
    <div class="fsm-reference-machine" markdown="1">

    ### `StandardGeometricProductCreate` { #fsm-standardgeometricproductcreate }



    <div class="cli-reference-label">Descrição</div>

    Statechart for creating a geometric product in an InfoBIM project's IFC model.


    <div class="cli-reference-label">Estados</div>

    <div class="fsm-reference-states" markdown="1">


    <div class="fsm-reference-state" markdown="1">

    Indefinido

    <span class="fsm-reference-value">`__undefined__`</span>

    <span class="fsm-reference-description">Estado inicial, antes da verificacao do modelo IFC alvo.</span>



    </div>

    <span class="fsm-reference-arrow">↓</span>



    <div class="fsm-reference-state" markdown="1">

    Modelo IFC Saudavel

    <span class="fsm-reference-value">`__ifc_model_healthy__`</span>

    <span class="fsm-reference-description">O modelo IFC alvo foi resolvido ou criado e pode ser modificado.</span>



    </div>

    <span class="fsm-reference-arrow">↓</span>



    <div class="fsm-reference-state" markdown="1">

    Unidade Definida

    <span class="fsm-reference-value">`__unit_defined__`</span>

    <span class="fsm-reference-description">O modelo IFC alvo declara o contexto de unidades da geometria.</span>



    </div>

    <span class="fsm-reference-arrow">↓</span>



    <div class="fsm-reference-state" markdown="1">

    Posicao Definida

    <span class="fsm-reference-value">`__position_defined__`</span>

    <span class="fsm-reference-description">A posicao exigida pela operacao geometrica esta definida nesta execucao.</span>



    </div>

    <span class="fsm-reference-arrow">↓</span>



    <div class="fsm-reference-state" markdown="1">

    Geometria Definida

    <span class="fsm-reference-value">`__geometry_defined__`</span>

    <span class="fsm-reference-description">A geometria primitiva esta completamente definida pelo seu comando.</span>



    </div>

    <span class="fsm-reference-arrow">↓</span>



    <div class="fsm-reference-state" markdown="1">

    Geometria Criada

    <span class="fsm-reference-value">`__geometry_created__`</span>

    <span class="fsm-reference-description">A geometria IFC correspondente existe no modelo IFC alvo.</span>



    </div>

    <span class="fsm-reference-arrow">↓</span>



    <div class="fsm-reference-state" markdown="1">

    Representacao de Forma Criada

    <span class="fsm-reference-value">`__shape_representation_created__`</span>

    <span class="fsm-reference-description">A representacao de forma IFC da geometria criada existe.</span>



    </div>

    <span class="fsm-reference-arrow">↓</span>



    <div class="fsm-reference-state" markdown="1">

    Produto Geometrico Criado

    <span class="fsm-reference-value">`__geometric_product_created__`</span>

    <span class="fsm-reference-description">O elemento IFC nomeado pelo titulo existe e carrega a representacao criada.</span>



    </div>

    <span class="fsm-reference-arrow">↓</span>



    <div class="fsm-reference-state" markdown="1">

    Produto Geometrico Federado <span class="fsm-reference-final">final</span>

    <span class="fsm-reference-value">`__geometric_product_federated__`</span>

    <span class="fsm-reference-description">O modelo IFC do projeto carrega o produto, colocado em sua estrutura espacial. Estados alem deste sao especificados antes de serem adicionados.</span>



    </div>



    </div>

    </div>

    <div class="fsm-reference-machine" markdown="1">

    ### `StandardGeometricProductDelete` { #fsm-standardgeometricproductdelete }



    <div class="cli-reference-label">Descrição</div>

    Statechart for deleting a geometric product (by GlobalId) from an InfoBIM project's IFC model.


    <div class="cli-reference-label">Estados</div>

    <div class="fsm-reference-states" markdown="1">


    <div class="fsm-reference-state" markdown="1">

    Indefinido

    <span class="fsm-reference-value">`__undefined__`</span>

    <span class="fsm-reference-description">Estado inicial, antes da verificacao do modelo IFC alvo.</span>



    </div>

    <span class="fsm-reference-arrow">↓</span>



    <div class="fsm-reference-state" markdown="1">

    Modelo IFC Saudavel

    <span class="fsm-reference-value">`__ifc_model_healthy__`</span>

    <span class="fsm-reference-description">O modelo IFC alvo foi resolvido e pode ser modificado.</span>



    </div>

    <span class="fsm-reference-arrow">↓</span>



    <div class="fsm-reference-state" markdown="1">

    GlobalId Conhecido

    <span class="fsm-reference-value">`__global_id_known__`</span>

    <span class="fsm-reference-description">O GlobalId do elemento a excluir esta bem formado nesta execucao.</span>



    </div>

    <span class="fsm-reference-arrow">↓</span>



    <div class="fsm-reference-state" markdown="1">

    GlobalId Presente

    <span class="fsm-reference-value">`__global_id_present__`</span>

    <span class="fsm-reference-description">Um produto IFC com o GlobalId solicitado existe no modelo federado.</span>



    </div>

    <span class="fsm-reference-arrow">↓</span>



    <div class="fsm-reference-state" markdown="1">

    Produto Geometrico Defederado

    <span class="fsm-reference-value">`__geometric_product_defederated__`</span>

    <span class="fsm-reference-description">O elemento e tudo o que ele era o unico dono foram removidos do modelo federado.</span>



    </div>

    <span class="fsm-reference-arrow">↓</span>



    <div class="fsm-reference-state" markdown="1">

    Estado Limpo <span class="fsm-reference-final">final</span>

    <span class="fsm-reference-value">`__state_cleaned_up__`</span>

    <span class="fsm-reference-description">O estado montado que gerou este produto (arquivos STEP sob a identidade do produto) foi removido do workspace ETL do projeto.</span>



    </div>



    </div>

    </div>

    <div class="fsm-reference-machine" markdown="1">

    ### `StandardIfcModelCreate` { #fsm-standardifcmodelcreate }



    <div class="cli-reference-label">Descrição</div>

    Statechart for creating the IFC model file an InfoBIM project writes its own elements into.


    <div class="cli-reference-label">Estados</div>

    <div class="fsm-reference-states" markdown="1">


    <div class="fsm-reference-state" markdown="1">

    Indefinido

    <span class="fsm-reference-value">`__undefined__`</span>

    <span class="fsm-reference-description">Estado inicial, antes da existencia do arquivo do modelo IFC.</span>



    </div>

    <span class="fsm-reference-arrow">↓</span>



    <div class="fsm-reference-state" markdown="1">

    Arquivo do Modelo IFC Criado

    <span class="fsm-reference-value">`__ifc_model_file_created__`</span>

    <span class="fsm-reference-description">O arquivo do modelo IFC existe no caminho indicado pela execucao e carrega o IfcProject do projeto.</span>


    <span class="fsm-reference-capability"><span class="fsm-reference-capability-label">Capability</span>: `src/infobim/ifc/plugin/capability/transformation/ifc_model_file_created.py`</span>


    </div>

    <span class="fsm-reference-arrow">↓</span>



    <div class="fsm-reference-state" markdown="1">

    Modelo IFC Declarado <span class="fsm-reference-final">final</span>

    <span class="fsm-reference-value">`__ifc_model_declared__`</span>

    <span class="fsm-reference-description">O RO-Crate do projeto declara o arquivo do modelo IFC.</span>


    <span class="fsm-reference-capability"><span class="fsm-reference-capability-label">Capability</span>: `src/infobim/ifc/plugin/capability/transformation/ifc_model_declared.py`</span>


    </div>



    </div>

    </div>


=== "Cadeias"

    <div class="fsm-reference-index" markdown="1">

    | Nome | Descrição |
    | --- | --- |
    | [`StandardGeometricResolverChain`](#fsm-standardgeometricresolverchain) | Parallel chain that resolves the geometry creation responsibilities able to handle a geometry definition. Each region is one responsibility, named by the id of the GeometryCreateResponsibilityPort capability it runs. |
    | [`StandardIfcProductChain`](#fsm-standardifcproductchain) | Parallel chain that resolves which capability creates the IFC class a run named. Each region is one responsibility, named by the id of the IfcProductCreateResponsibilityPort capability it runs. |

    </div>

    
    <div class="fsm-reference-machine" markdown="1">

    ### `StandardGeometricResolverChain` { #fsm-standardgeometricresolverchain }



    <div class="cli-reference-label">Descrição</div>

    Parallel chain that resolves the geometry creation responsibilities able to handle a geometry definition. Each region is one responsibility, named by the id of the GeometryCreateResponsibilityPort capability it runs.


    </div>

    <div class="fsm-reference-machine" markdown="1">

    ### `StandardIfcProductChain` { #fsm-standardifcproductchain }



    <div class="cli-reference-label">Descrição</div>

    Parallel chain that resolves which capability creates the IFC class a run named. Each region is one responsibility, named by the id of the IfcProductCreateResponsibilityPort capability it runs.


    </div>
