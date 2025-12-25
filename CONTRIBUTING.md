# Contribution Rules (Binding on edits)

1) Only Section II is binding.
2) Section II is protected:
   - edits inside II require an RSR bump and an "RSR-BUMP:" entry in CHANGELOG,
   - OR must be whitespace-only.
3) O and I may be edited for clarity, but must not introduce new invariants, scope, or requirements.
4) No moving text across O/I/II boundaries without an RSR bump.
5) All changes must pass: `python tools/lint.py`.