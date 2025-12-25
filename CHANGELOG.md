# Changelog

All notable changes to the Substrate Accords will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to semantic versioning for the RSR protocol.

## [1.1] - 2024-12-25

### Changed
- Converted monolithic document into modular structure
- Separated constraints into individual markdown files
- Created assembly tooling for canonical reconstruction

### Added
- `/frontmatter/` directory for non-binding interpretive guidance
- `/meta/` directory for meta-structural protocols (RSR)
- `/constraints/` directory with eight individual constraint files
- `/tools/` directory with assembly script and linting rules
- README.md with project overview and usage instructions
- This CHANGELOG.md

### Technical
- Each constraint follows three-layer architecture (O/I/II)
- Assembly preserves canonical ordering via numbered filenames
- Linting rules enforce structural and content consistency

### Invariant
- No binding constraint semantics were altered in this release.
- All changes are structural, organizational, or tooling-related only.

## [1.0] - 2024-12-XX

### Added
- Initial formulation of The Substrate Accords
- Eight core constraints (Lambda through Sigma)
- Revision Safety Constraints (RSR) v1.0
- Interpretive Exclusions and Applicability Boundaries
- Formal mathematical specifications for each constraint
- Disconfirmation signatures (Kill Checks) for each constraint

---

## Version Numbering

Two version numbers are tracked independently:

**RSR Version**
- Defines the currently binding Revision Safety Constraints.
- Determines which edits to the Accords are authoritative.
- Semantic changes to constraint meaning require an RSR version update.

**Document Version**
- Tracks changes to structure, formatting, organization, tooling, or presentation.
- Does not imply semantic modification of any constraint.
- May change without affecting compliance or interpretation.

Current versions:
- RSR: 1.1
- Document: 1.1 (modular)
