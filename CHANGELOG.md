# Changelog

## Pharmacovigilance Intelligence System

All notable development changes to the project are documented in this file.

The project is currently a research and development prototype.

---

## [Phase 6] — Documentation and Project Packaging

### Added

- Completed the main project `README.md`.
- Added `ARCHITECTURE.md`.
- Added `INTEGRATION.md`.
- Added `HANDOVER.md`.
- Added `CHANGELOG.md`.
- Added supporting documentation under `docs/`.
- Added `docs/dataset_registry.md`.
- Added `docs/dataset_evaluation.md`.
- Added `docs/data_dictionary.md`.
- Added `docs/learning_notes.md`.
- Added `docs/runtime_proof.md`.
- Created the `evidence_packet/` directory structure for supporting project evidence.

### Documentation Coverage

The documentation now covers:

- Project overview
- System architecture
- Component integration
- Evidence workflow
- Dataset information
- Data dictionary
- Runtime verification
- Learning notes
- Project handover
- Current limitations
- Future development

---

## [Phase 5] — Evidence and Project Documentation

### Completed

- Organized the project documentation structure.
- Prepared evidence-related documentation.
- Documented the implemented pharmacovigilance workflow.
- Prepared supporting runtime and project evidence areas.
- Continued organizing the project for review and handover.

---

## [Phase 4] — Automated Testing

### Completed

- Implemented the Phase 4 automated testing workflow.
- Executed the pytest test suite.
- Verified the implemented test cases.
- Recorded the final test result:

`10 passed`

### Verification

The successful test execution provided runtime evidence that the defined Phase 4 automated tests completed successfully.

---

## [Phase 3] — Evidence Processing and Normalization

### Completed

- Developed the structured evidence-processing workflow.
- Added evidence normalization functionality.
- Defined the internal evidence representation.
- Added evidence schema handling.
- Connected retrieved safety information with the normalized evidence model.

### Evidence Concepts

The normalized evidence model includes concepts such as:

- Evidence ID
- Drug name
- Adverse event
- Source
- Source record ID
- Evidence type
- Retrieval timestamp
- Source URL
- Schema version
- Provenance

---

## [Phase 2] — API and Data Retrieval

### Completed

- Set up the Python development environment.
- Configured the project in Visual Studio Code.
- Installed required Python packages.
- Added API request functionality using `requests`.
- Connected the project to the OpenFDA drug-event API.
- Implemented drug safety-data retrieval.
- Added handling for API responses.
- Tested the application runtime.

### Primary Source

The project uses OpenFDA / FAERS-related drug-event data as the primary external safety-data source.

---

## [Phase 1] — Project Foundation

### Completed

- Established the pharmacovigilance intelligence project objective.
- Defined the initial drug safety evidence workflow.
- Reviewed the role of public biomedical safety data.
- Established the initial project structure.
- Documented learning and implementation requirements.
- Prepared the foundation for the Python-based evidence pipeline.

---

## Current Project Structure

The project currently contains:

```text
Pharmacovigilance_Project/
│
├── src/
├── tests/
├── docs/
├── evidence_packet/
│   ├── screenshots/
│   ├── code_packet/
│   ├── runtime_logs/
│   ├── api_samples/
│   └── deployment_proof/
│
├── app.py
├── openfda_test.py
├── test_normalization.py
├── evidence_output.json
│
├── README.md
├── ARCHITECTURE.md
├── INTEGRATION.md
├── HANDOVER.md
├── CHANGELOG.md
└── REVIEW_PACKET.md