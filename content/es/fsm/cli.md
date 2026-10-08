# Referencia de FSM — cli

Máquinas de estados finitos declaradas por `cli` en `infobim`.


<div class="fsm-reference-index" markdown="1">

| Nombre | Descripción |
| --- | --- |
| [`StandardInfoBIMInit`](#fsm-standardinfobiminit) | Bring an initialized OntoBDC project to one InfoBIM can be started from. |

</div>


<div class="fsm-reference-machine" markdown="1">

### `StandardInfoBIMInit` { #fsm-standardinfobiminit }

<div class="fsm-reference-title" markdown="1">InfoBIM Init</div>

<div class="cli-reference-label">Descripción</div>

Bring an initialized OntoBDC project to one InfoBIM can be started from.


<div class="cli-reference-label">Estados</div>

<div class="fsm-reference-states" markdown="1">


<div class="fsm-reference-state" markdown="1">

Undefined

<span class="fsm-reference-value">`__undefined__`</span>

<span class="fsm-reference-description">Initial state before the InfoBIM serve shortcut is in place.</span>



</div>

<span class="fsm-reference-arrow">↓</span>



<div class="fsm-reference-state" markdown="1">

Serve Shortcut Ready <span class="fsm-reference-final">final</span>

<span class="fsm-reference-value">`__serve_shortcut_ready__`</span>

<span class="fsm-reference-description">The project root holds the InfoBIM-Serve.lnk shortcut, which runs infobim serve from the project folder. Where the platform has no shortcuts there is none to hold.</span>



</div>



</div>

</div>
