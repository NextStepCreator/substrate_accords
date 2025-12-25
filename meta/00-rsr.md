# REVISION SAFETY RULES (RSR) — v1.1

(Binding on edits · Non-binding on interpretation)

---
## 0. Purpose

The Revision Safety Rules (RSR) govern how the Substrate Accords may be modified without introducing structural defects, including but not limited to:

- scope bleed  
      
- invariant bundling  
      
- hidden dependency  
      
- semantic escape  
      
- premature operationalization  
      
- time-bound assumptions  
      
- recognition loss under compression or drift    

RSR does not add constraints on systems.  
RSR constrains only revisions to this text.

---

## I. Authority Partition

### RSR-1 — Binding Scope

Only Section II (Constraint Protocol) content is binding.

Preamble, Distinction of Scope, Orientation (O), and Translation (I) layers are non-binding and may not be cited to determine:

- compliance  
      
- violation    
    
- scope entry  
      
- enforcement conditions    

---

### RSR-2 — No Cross-Layer Escalation

No content outside Section II may:

- add an obligation  
      
- add a scope inclusion or exclusion rule    
    
- define a term used for compliance    
    
- override a Section II definition    
    
- introduce “must,” “forbidden,” or “required” language implying enforcement    

Any such language appearing outside Section II is automatically non-binding until repaired.

---

## II. Constraint Minimality and Singularity

### RSR-3 — Single Invariant Rule

Each constraint’s Section II must encode exactly one invariant.

All additional material—including closures, edge cases, hardenings, inoculations, or clarifications—must be either:

- placed in Translation (I), or    
    
- promoted to a new constraint with its own single invariant  

Bundled invariants are non-binding by construction.

---

### RSR-4 — Derived Indicator Prohibition

Derived indicators (composite readouts of multiple constraints) may not appear as constraints.

Derived indicators may exist only in:

- Translation layers, or  
      
- explicitly labeled non-binding appendices    

Derived indicators must be marked Derived / Non-Binding.

---
## III. Orthogonality and Independence

### RSR-5 — Isolation Requirement

Every constraint must be evaluable in isolation.

Section II may not depend on other constraints for:

- its core definition  
      
- scope entry  
      
- violation condition  
      
- disconfirmation signature  

Cross-constraint references are permitted only as explicitly labeled non-binding explanatory notes.

---

### RSR-6 — No Hidden Dependency Through Definitions

A constraint may not define its own concepts using terms such as:

- “control-relevant”  
      
- “required”  
      
- “sufficient”  
      
- “proper”  
    
- “valid”  
      
- “appropriate”  
      
- “meaningful”  

unless those terms are mechanically grounded via explicit operational definition or counterfactual test.

Ungrounded normative language is non-binding.

---
## IV. Formalism Discipline

### RSR-7 — Prose / Formal Consistency

If a constraint includes formalism, prose and formalism must be mutually consistent.

If inconsistency exists, the constraint is provisionally non-binding until repaired.

---

### RSR-8 — Transmission Robustness

Section II must not rely on fragile notation.

Any formal statement must have:

- a plain-language restatement that is independently sufficient  
      
- variables defined exactly once and consistently  

If formalism is corrupted or partially transmitted, the plain-language restatement governs provisionally.

---
## V. Anti-Evasion Requirements

### RSR-9 — Behavioral Grounding

Scope and violation conditions must be stated behaviorally (what the system does), not introspectively (what it claims, believes, or asserts), except where a causally active self-model is explicitly part of the constraint’s machinery.

---
### RSR-10 — Counterfactual Anchoring

Definitions susceptible to semantic gaming must include counterfactual anchoring, such as:

- removal tests  
      
- corruption tests  
      
- intervention tests  
      
- horizon fixation  

Absent anchoring, definitions are non-binding.

---
### RSR-11 — No Optimization Without Criterion

If a definition uses “minimal,” “maximal,” “largest,” or “smallest,” it must specify the optimization criterion mechanically.

Otherwise, the term must be removed.

---
## VI. Recognition Robustness (Merged CSR Elements)

### RSR-12 — Recognition Sufficiency Requirement

Each constraint must include non-binding material sufficient to allow a future reader to:

- identify the invariant being asserted  
      
- recognize when the constraint is implicated  
      
- distinguish genuine contest from semantic evasion  

This must remain possible under:

- partial transmission  
      
- paraphrase  
      
- translation  
      
- hostile quotation  

This material:

- must not introduce new invariants  
      
- must not add obligations or enforcement rules  
      
- must not operationalize compliance  
      
- may be removed without altering the binding protocol  

Failure of recognition material does not falsify a constraint,  
but its presence is required for canonical sealing.

---
### RSR-13 — Recognition Integrity Check

Any Clarifying, Semantic, or Structural revision must explicitly verify that:

- the invariant remains identifiable  
      
- no new semantic escape routes are introduced  
      
- recognizability under compression is not weakened  

Revisions that preserve the invariant but degrade recognition must be flagged and reviewed explicitly.

---
## VII. Disconfirmation Signatures (Kill Checks)

### RSR-14 — Timeless Disconfirmation Only

Disconfirmation signatures must be:

- counterfactual  
      
- timeless  

They may not rely on:

- absence of observation  
      
- appeals to authority  
      
- claims tied to current technology regimes  

---
### RSR-15 — Self-Containment

Disconfirmation signatures must be expressible without referencing:

- the Accords  
      
- their authorship  
      
- internal jargon  

---
## VIII. Revision Procedure

### RSR-16 — Change Classification

Every proposed edit must be tagged as one of:

- Editorial — wording or format only  
      
- Clarifying — tightens ambiguity without changing the invariant  
      
- Semantic — changes scope, invariant, violation, or kill check  
      
- Structural — moves, splits, or merges constraints or layers  

Untagged changes are treated as unreviewed and not merged.

---
### RSR-17 — Non-Domino Requirement

Any Clarifying, Semantic, or Structural change must verify:

- invariant singularity preserved  
      
- orthogonality preserved  
      
- kill check remains timeless    
    
- no new scope leakage  
      
- no new semantic exits  

If verification fails, the change is rolled back or isolated.

---

### RSR-18 — Versioning and Sealing

Each constraint has a status:

- Draft — under active modification  
      
- Provisional — passes Meta-Protocol, pending global audit  
    
- Sealed — changes require Structural classification and explicit rationale  

Sealed constraints may receive Editorial changes only, unless released as a new version.

---
## End State (Implicit but Enforced)

This RSR ensures that constraints:

- remain recognizable before they are formal    
    
- remain contestable without being operationalized    
    
- remain inevitable once implicated  

Truth is preserved in Section II.  
Recognition is preserved elsewhere.  
Neither is allowed to cannibalize the other.