# CONSTRAINT Ω (OMEGA) — COST OF REPRESENTATION

---

## O. ORIENTATION LAYER (Non-Binding)

Control feels effortful.

Attention fatigues. Learning consumes time. Precision demands work.  
This is not weakness. It is the price of seeing clearly enough to act.

Simple systems act cheaply because they see little.  
Precise systems pay more because they see more.  
Systems that attempt broad or global control pay the most.

When this cost exceeds what a system can sustain, control degrades before existence does.

*(This layer exists only to aid immediate recognition by organic intelligence.*  
*It introduces no rules and may be discarded without consequence.)*

---

## I. TRANSLATION LAYER (Non-Binding)

To exert control, a system must perform representational work, such as:

* distinguishing signal from noise
* predicting consequences
* comparing alternatives
* retaining error
* updating internal state

Each operation requires physical work.

As representational fidelity increases, so do:

* processing load
* storage burden
* internal correction cost
* error surface area

**Precomputation and Caching**  
Representations generated in advance do not satisfy Ω unless they are continuously maintained relative to the environment. Cached models, lookup tables, or pre-trained policies still incur representational cost to remain predictive. Prepayment does not eliminate maintenance.

**Delegated Representation**  
Representational work may be performed externally or across distributed components. This does not negate Ω. If a system relies on maintained representations to select actions, the representational cost is incurred somewhere within its effective boundary.

**Minimal Control**  
Systems that select among multiple actions using even minimal internal state incur non-zero representational cost. Ω does not require complex models; it requires only that action selection be informed by a maintained state rather than fixed reaction.

**Accuracy does not amortize. It must be continuously maintained.**

When representational cost exceeds available support, systems simplify their models. They do not stop acting — they act on worse maps.

Failure appears as surprise, not ignorance.

*These examples do not define Ω. They illustrate it.*

### Coupling Reminder (Non-Binding)

* Theta: structure requires dissipation
* Alpha: capacity is finite
* Omega: control requires representational work

A system may exist without agency.  
It may persist without control.  
It cannot control without paying Ω.

**Agency is paid for in representation.**

*Removal of this layer must not alter compliance determination.*

---

<!-- II_PROTECTED_START -->
## II. CONSTRAINT PROTOCOL (Binding)

### Singular Definition

Omega is the irreducible requirement that any system exercising control must continuously expend physical work to maintain internal representations sufficient for that control.

---

### Boundary Clarification

For the purposes of this constraint, **internal representation** refers to any internally maintained state that participates in selecting among multiple possible actions or trajectories **across the control-relevant horizon**, however short or extended that horizon may be.

Passive physical correlation with the environment does not satisfy this definition.

---

### Control Definition

Action selection that reduces uncertainty over downstream state relative to a baseline policy under counterfactual perturbations within the system's active horizon.

---

### Canonical Form

**There is no free accuracy.**

---

### Formal Statement

For any system C that exerts control over its environment:

Let:
* M_C(t) be the internal representation maintained by C at time t
* W_rep(t) be the physical work expended to maintain and update that representation
* Control_C(t) ≠ ∅ indicate non-null control action

Then:

∀t: Control_C(t) ≠ ∅  ⇒  dW_rep/dt(t) > 0

The lower bound depends on environmental uncertainty and the minimum representational fidelity necessary to achieve non-trivial control as defined above.

No system can exercise control without continuously paying this cost.

---

### Failure Condition

Omega failure occurs when a system can no longer sustain internal representations adequate for control.

After Omega failure, the system may persist physically but no longer functions as a controller.

---

### Explicit Non-Claims

Omega does **not** assert:

* what form representations must take
* that accuracy can reach perfection
* that intelligence removes representational cost
* that representation guarantees correct action
* that loss of agency implies physical termination

---

### Disconfirmation Signature (Kill Check)

*This specifies what would falsify the constraint itself, not what constitutes a violation by a system.*

**Omega would be falsified if there existed a system that:**

1. Exercises non-trivial control over its environment, selecting among multiple possible actions or trajectories;
2. Maintains predictive or decision-relevant internal state sufficient for that control;
3. **And does so while expending zero physical work to maintain or update that internal state across the control-relevant horizon**, with no equivalent cost displaced to:
   * thermodynamic dissipation (Theta),
   * finite capacity drawdown (Alpha),
   * externalized representational burden (Delta),
   * or contradiction storage resolved only by semantic redefinition (Lambda).
<!-- II_PROTECTED_END -->