# Referência de FSM — cli

Máquinas de estado finito declaradas por `cli` em `infobim`.


<div class="fsm-reference-index" markdown="1">

| Nome | Descrição |
| --- | --- |
| [`StandardInfoBIMInit`](#fsm-standardinfobiminit) | Leva um projeto OntoBDC inicializado a um projeto de onde o InfoBIM pode ser iniciado. |

</div>


<div class="fsm-reference-machine" markdown="1">

### `StandardInfoBIMInit` { #fsm-standardinfobiminit }

<div class="fsm-reference-title" markdown="1">Init do InfoBIM</div>

<div class="cli-reference-label">Descrição</div>

Leva um projeto OntoBDC inicializado a um projeto de onde o InfoBIM pode ser iniciado.


<div class="cli-reference-label">Estados</div>

<div class="fsm-reference-states" markdown="1">


<div class="fsm-reference-state" markdown="1">

Indefinido

<span class="fsm-reference-value">`__undefined__`</span>

<span class="fsm-reference-description">Estado inicial antes de o atalho de serve do InfoBIM existir.</span>



</div>

<span class="fsm-reference-arrow">↓</span>



<div class="fsm-reference-state" markdown="1">

Atalho de Serve Pronto <span class="fsm-reference-final">final</span>

<span class="fsm-reference-value">`__serve_shortcut_ready__`</span>

<span class="fsm-reference-description">A raiz do projeto contem o atalho InfoBIM-Serve.lnk, que executa infobim serve a partir da pasta do projeto. Onde a plataforma nao tem atalhos, nao ha o que manter.</span>



</div>



</div>

</div>
