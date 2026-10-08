# FSM reference — ifc

Finite-state machines declared by `ifc` in `infobim`.


=== "FSM"

    <div class="fsm-reference-index" markdown="1">

    | Name | Description |
    | --- | --- |
    | [`StandardGeometricProductCreate`](#fsm-standardgeometricproductcreate) | Statechart for creating a geometric product in an InfoBIM project's IFC model. |
    | [`StandardGeometricProductDelete`](#fsm-standardgeometricproductdelete) | Statechart for deleting a geometric product (by GlobalId) from an InfoBIM project's IFC model. |
    | [`StandardIfcModelCreate`](#fsm-standardifcmodelcreate) | Statechart for creating the IFC model file an InfoBIM project writes its own elements into. |

    </div>

    
    <div class="fsm-reference-machine" markdown="1">

    ### `StandardGeometricProductCreate` { #fsm-standardgeometricproductcreate }



    <div class="cli-reference-label">Description</div>

    Statechart for creating a geometric product in an InfoBIM project's IFC model.


    <div class="cli-reference-label">States</div>

    <div class="fsm-reference-states" markdown="1">


    <div class="fsm-reference-state" markdown="1">

    Undefined

    <span class="fsm-reference-value">`__undefined__`</span>

    <span class="fsm-reference-description">Initial state, before the target IFC model was verified.</span>



    </div>

    <span class="fsm-reference-arrow">↓</span>



    <div class="fsm-reference-state" markdown="1">

    IFC Model Healthy

    <span class="fsm-reference-value">`__ifc_model_healthy__`</span>

    <span class="fsm-reference-description">The target IFC model was resolved or created and can be modified.</span>



    </div>

    <span class="fsm-reference-arrow">↓</span>



    <div class="fsm-reference-state" markdown="1">

    Unit Defined

    <span class="fsm-reference-value">`__unit_defined__`</span>

    <span class="fsm-reference-description">The target IFC model states the unit context geometry is measured in.</span>



    </div>

    <span class="fsm-reference-arrow">↓</span>



    <div class="fsm-reference-state" markdown="1">

    Position Defined

    <span class="fsm-reference-value">`__position_defined__`</span>

    <span class="fsm-reference-description">The position the geometric operation requires is defined for this run.</span>



    </div>

    <span class="fsm-reference-arrow">↓</span>



    <div class="fsm-reference-state" markdown="1">

    Geometry Defined

    <span class="fsm-reference-value">`__geometry_defined__`</span>

    <span class="fsm-reference-description">The primitive geometry is completely defined by its own command.</span>



    </div>

    <span class="fsm-reference-arrow">↓</span>



    <div class="fsm-reference-state" markdown="1">

    Geometry Created

    <span class="fsm-reference-value">`__geometry_created__`</span>

    <span class="fsm-reference-description">The corresponding IFC geometry exists in the target IFC model.</span>



    </div>

    <span class="fsm-reference-arrow">↓</span>



    <div class="fsm-reference-state" markdown="1">

    Shape Representation Created

    <span class="fsm-reference-value">`__shape_representation_created__`</span>

    <span class="fsm-reference-description">The IFC shape representation of the created geometry exists.</span>



    </div>

    <span class="fsm-reference-arrow">↓</span>



    <div class="fsm-reference-state" markdown="1">

    Geometric Product Created

    <span class="fsm-reference-value">`__geometric_product_created__`</span>

    <span class="fsm-reference-description">The IFC element the title names exists and carries the created representation.</span>



    </div>

    <span class="fsm-reference-arrow">↓</span>



    <div class="fsm-reference-state" markdown="1">

    Geometric Product Federated <span class="fsm-reference-final">final</span>

    <span class="fsm-reference-value">`__geometric_product_federated__`</span>

    <span class="fsm-reference-description">The project's IFC model carries the product, placed in its spatial structure. States beyond this one are specified before being added.</span>



    </div>



    </div>

    </div>

    <div class="fsm-reference-machine" markdown="1">

    ### `StandardGeometricProductDelete` { #fsm-standardgeometricproductdelete }



    <div class="cli-reference-label">Description</div>

    Statechart for deleting a geometric product (by GlobalId) from an InfoBIM project's IFC model.


    <div class="cli-reference-label">States</div>

    <div class="fsm-reference-states" markdown="1">


    <div class="fsm-reference-state" markdown="1">

    Undefined

    <span class="fsm-reference-value">`__undefined__`</span>

    <span class="fsm-reference-description">Initial state, before the target IFC model was verified.</span>



    </div>

    <span class="fsm-reference-arrow">↓</span>



    <div class="fsm-reference-state" markdown="1">

    IFC Model Healthy

    <span class="fsm-reference-value">`__ifc_model_healthy__`</span>

    <span class="fsm-reference-description">The target IFC model was resolved and can be modified.</span>



    </div>

    <span class="fsm-reference-arrow">↓</span>



    <div class="fsm-reference-state" markdown="1">

    GlobalId Known

    <span class="fsm-reference-value">`__global_id_known__`</span>

    <span class="fsm-reference-description">The GlobalId of the element to delete is well-formed for this run.</span>



    </div>

    <span class="fsm-reference-arrow">↓</span>



    <div class="fsm-reference-state" markdown="1">

    GlobalId Present

    <span class="fsm-reference-value">`__global_id_present__`</span>

    <span class="fsm-reference-description">An IFC product with the requested GlobalId is carried by the federated model.</span>



    </div>

    <span class="fsm-reference-arrow">↓</span>



    <div class="fsm-reference-state" markdown="1">

    Geometric Product Defederated

    <span class="fsm-reference-value">`__geometric_product_defederated__`</span>

    <span class="fsm-reference-description">The element and everything only it owned have been removed from the federated model.</span>



    </div>

    <span class="fsm-reference-arrow">↓</span>



    <div class="fsm-reference-state" markdown="1">

    State Cleaned Up <span class="fsm-reference-final">final</span>

    <span class="fsm-reference-value">`__state_cleaned_up__`</span>

    <span class="fsm-reference-description">The assembled state that produced this product (STEP files under the product's identity) is gone from the project's ETL workspace.</span>



    </div>



    </div>

    </div>

    <div class="fsm-reference-machine" markdown="1">

    ### `StandardIfcModelCreate` { #fsm-standardifcmodelcreate }



    <div class="cli-reference-label">Description</div>

    Statechart for creating the IFC model file an InfoBIM project writes its own elements into.


    <div class="cli-reference-label">States</div>

    <div class="fsm-reference-states" markdown="1">


    <div class="fsm-reference-state" markdown="1">

    Undefined

    <span class="fsm-reference-value">`__undefined__`</span>

    <span class="fsm-reference-description">Initial state, before the IFC model file exists.</span>



    </div>

    <span class="fsm-reference-arrow">↓</span>



    <div class="fsm-reference-state" markdown="1">

    IFC Model File Created

    <span class="fsm-reference-value">`__ifc_model_file_created__`</span>

    <span class="fsm-reference-description">The IFC model file exists at the path the run names and carries the project's IfcProject.</span>


    <span class="fsm-reference-capability"><span class="fsm-reference-capability-label">Capability</span>: `src/infobim/ifc/plugin/capability/transformation/ifc_model_file_created.py`</span>


    </div>

    <span class="fsm-reference-arrow">↓</span>



    <div class="fsm-reference-state" markdown="1">

    IFC Model Declared <span class="fsm-reference-final">final</span>

    <span class="fsm-reference-value">`__ifc_model_declared__`</span>

    <span class="fsm-reference-description">The project's RO-Crate states the IFC model file.</span>


    <span class="fsm-reference-capability"><span class="fsm-reference-capability-label">Capability</span>: `src/infobim/ifc/plugin/capability/transformation/ifc_model_declared.py`</span>


    </div>



    </div>

    </div>


=== "Chains"

    <div class="fsm-reference-index" markdown="1">

    | Name | Description |
    | --- | --- |
    | [`StandardGeometricResolverChain`](#fsm-standardgeometricresolverchain) | Parallel chain that resolves the geometry creation responsibilities able to handle a geometry definition. Each region is one responsibility, named by the id of the GeometryCreateResponsibilityPort capability it runs. |
    | [`StandardIfcProductChain`](#fsm-standardifcproductchain) | Parallel chain that resolves which capability creates the IFC class a run named. Each region is one responsibility, named by the id of the IfcProductCreateResponsibilityPort capability it runs. |

    </div>

    
    <div class="fsm-reference-machine" markdown="1">

    ### `StandardGeometricResolverChain` { #fsm-standardgeometricresolverchain }



    <div class="cli-reference-label">Description</div>

    Parallel chain that resolves the geometry creation responsibilities able to handle a geometry definition. Each region is one responsibility, named by the id of the GeometryCreateResponsibilityPort capability it runs.


    </div>

    <div class="fsm-reference-machine" markdown="1">

    ### `StandardIfcProductChain` { #fsm-standardifcproductchain }



    <div class="cli-reference-label">Description</div>

    Parallel chain that resolves which capability creates the IFC class a run named. Each region is one responsibility, named by the id of the IfcProductCreateResponsibilityPort capability it runs.


    </div>
