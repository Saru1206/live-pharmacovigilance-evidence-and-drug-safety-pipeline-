# Pharmacovigilance Intelligence System

## AI-Assisted Drug Safety Evidence Pipeline

A Python-based pharmacovigilance intelligence prototype designed to retrieve, process, normalize, validate, store, and test drug safety evidence from public biomedical safety data sources.

---

## 1. Project Overview

Pharmacovigilance involves the continuous detection, assessment, understanding, and prevention of adverse effects and other drug-related safety problems.

This project demonstrates a structured software pipeline for working with drug safety evidence.

The system connects to the OpenFDA drug-event API, retrieves safety information, converts the retrieved information into a structured evidence representation, validates the evidence, and stores the resulting records.

The project also includes automated testing to verify important system behaviors.

---

## 2. Project Objectives

The main objectives are:

1. Retrieve drug safety information from a trusted public source.
2. Process API responses into structured evidence.
3. Normalize evidence into a consistent schema.
4. Preserve source and provenance information.
5. Store normalized evidence records.
6. Prevent unnecessary duplicate ingestion.
7. Provide a simple drug-search workflow.
8. Handle API and no-result situations.
9. Create automated tests for important system behaviors.
10. Maintain documentation and runtime evidence for reproducibility.

---

## 3. System Workflow

The implemented workflow can be summarized as:

User Input
→ OpenFDA API Request
→ Retrieved Safety Data
→ Data Processing
→ Evidence Normalization
→ Schema Validation
→ Evidence Storage
→ Search / Retrieval

The project separates data retrieval, evidence modeling, normalization, storage, and testing into different components.

---

## 4. Main Components

### 4.1 OpenFDA Connector

File:

`src/openfda_connector.py`

Responsible for communicating with the OpenFDA drug-event API and retrieving drug safety information.

---

### 4.2 Evidence Schema

File:

`src/evidence_schema.py`

Defines the structured representation used for normalized evidence.

Important evidence concepts include:

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

### 4.3 Evidence Normalization

File:

`src/normalize_evidence.py`

Converts retrieved source information into the project's normalized evidence structure.

The normalization stage helps maintain consistency between evidence records.

---

### 4.4 Evidence Store

File:

`src/evidence_store.py`

Responsible for storing normalized evidence records and handling duplicate ingestion behavior.

The project uses structured JSON evidence storage during the prototype stage.

---

### 4.5 Application

File:

`app.py`

Provides the main application workflow for searching drug safety information and processing the resulting evidence.

---

### 4.6 Automated Tests

File:

`tests/test_phase4.py`

Contains the Phase 4 automated tests used to verify important system behaviors.

The completed test execution produced:

`10 passed`

---

## 5. Project Structure

The current project structure is:

Pharmacovigilance_Project/
    
    src/
        __init__.py
        evidence_schema.py
        evidence_store.py
        normalize_evidence.py
        openfda_connector.py

    tests/
        test_phase4.py

    docs/
        data_dictionary.md
        dataset_evaluation.md
        dataset_registry.md
        learning_notes.md
        runtime_proof.md

    evidence_packet/
        screenshots/
        code_packet/
        runtime_logs/
        api_samples/
        deployment_proof/

    app.py
    openfda_test.py
    test_normalization.py
    evidence_output.json

    README.md
    ARCHITECTURE.md
    INTEGRATION.md
    HANDOVER.md
    CHANGELOG.md
    REVIEW_PACKET.md

---

## 6. Requirements

The project requires:

- Python 3.x
- Visual Studio Code or another Python development environment
- Internet connectivity for API access
- `requests`
- `pytest`

---

## 7. Installation

### Step 1 — Open the project

Open the project folder in Visual Studio Code.

### Step 2 — Open the terminal

Use:

`Ctrl + ``

or open:

`Terminal → New Terminal`

### Step 3 — Install required packages

Run:

`pip install requests pytest`

If `pip` is not recognized, use:

`python -m pip install requests pytest`

---

## 8. Running the Application

From the project root, run:

`python app.py`

The application starts the pharmacovigilance drug safety search workflow.

The user can provide a drug name, after which the application communicates with the configured OpenFDA source.

---

## 9. Testing

The project uses pytest for automated verification.

Run the Phase 4 test suite using:

`python -m pytest tests/test_phase4.py -v`

The completed test execution produced:

`10 passed`

This confirms that all ten tests included in the recorded Phase 4 test suite passed.

---

## 10. Example Runtime Workflow

A typical workflow is:

1. Start the application.
2. Enter a drug name.
3. The application sends a request to OpenFDA.
4. The returned information is processed.
5. Relevant information is normalized.
6. The normalized evidence is validated.
7. Evidence can be stored.
8. Duplicate ingestion is controlled.
9. Results can be reviewed.

---

## 11. Error and No-Result Handling

The application includes handling for unsuccessful or empty API responses.

For example, an invalid or nonexistent drug search may result in no matching safety records.

The system should handle such situations without treating them as successful evidence retrieval.

API failures are also surfaced as errors rather than silently producing incorrect evidence.

---

## 12. Evidence Provenance

A major design principle of the project is preservation of evidence provenance.

The evidence lifecycle follows:

Source
→ Source Record
→ Retrieval
→ Transformation
→ Normalized Evidence
→ Storage

The normalized evidence model includes information that helps identify where the evidence originated and when it was retrieved.

This is important for traceability in pharmacovigilance workflows.

---

## 13. Duplicate Ingestion

The evidence storage component includes duplicate handling.

The intended behavior is:

First ingestion
→ Evidence is stored.

Repeated ingestion of the same evidence
→ Duplicate is detected.
→ Additional duplicate storage is prevented.

This helps maintain a cleaner evidence store.

---

## 14. Documentation

Additional project documentation is available in the `docs/` directory.

### Dataset Registry

`docs/dataset_registry.md`

Documents the datasets and source information used by the project.

### Dataset Evaluation

`docs/dataset_evaluation.md`

Documents the evaluation and limitations of the available safety data.

### Data Dictionary

`docs/data_dictionary.md`

Defines the important fields and terminology used within the project's structured evidence records.

### Learning Notes

`docs/learning_notes.md`

Records important implementation and learning outcomes from the project.

### Runtime Proof

`docs/runtime_proof.md`

Documents runtime verification and the recorded automated testing result.

---

## 15. Evidence Packet

The `evidence_packet/` directory is intended to organize project evidence supporting implementation and testing.

It contains:

- Screenshots
- Code evidence
- Runtime logs
- API samples
- Deployment-related evidence

This structure supports easier review and handover of the project.

---

## 16. Testing Result

The final recorded Phase 4 automated test result is:

`10 passed`

This provides evidence that the defined automated test cases completed successfully in the configured development environment.

Runtime proof is documented separately in:

`docs/runtime_proof.md`

---

## 17. Current Capabilities

The current prototype supports:

- Drug safety searching
- OpenFDA API interaction
- Structured evidence representation
- Evidence normalization
- Schema validation
- Evidence storage
- Duplicate ingestion handling
- Provenance tracking
- Automated testing
- Documentation of runtime behavior

---

## 18. Current Limitations

This project is a prototype and should not be considered a production clinical pharmacovigilance system.

Current limitations include:

- Dependence on external API availability
- Dependence on the quality and completeness of source data
- Limited source coverage
- Prototype-level storage
- No automatic clinical causality determination
- No replacement for expert pharmacovigilance assessment
- No guarantee that an adverse event was caused by the associated drug

The system is intended for research, learning, evidence organization, and prototype development.

---

## 19. Pharmacovigilance Interpretation

The presence of an adverse event report does not automatically establish that a drug caused the event.

The system retrieves and organizes safety evidence.

Clinical interpretation, causality assessment, signal evaluation, and regulatory decision-making require appropriate expert review.

Therefore, system output should be treated as evidence for further assessment rather than as a definitive clinical conclusion.

---

## 20. Reproducibility

The main application can be executed using:

`python app.py`

The automated Phase 4 tests can be executed using:

`python -m pytest tests/test_phase4.py -v`

The recorded successful result was:

`10 passed`

Future executions may differ because external API responses and source datasets can change over time.

---

## 21. Future Development

Potential future improvements include:

- Additional pharmacovigilance data sources
- Larger-scale evidence ingestion
- Advanced adverse-event normalization
- Improved search and filtering
- Signal detection capabilities
- Evidence ranking
- Natural-language evidence summarization
- Dashboard-based visualization
- More extensive automated testing
- Production-grade database storage
- Authentication and access control
- Monitoring and logging
- Deployment to a managed environment

These are future development possibilities and are not represented as completed functionality in the current prototype.

---

## 22. Project Status

### Implementation

**Status: Completed prototype**

### Automated Testing

**Status: Completed**

Recorded result:

`10 passed`

### Documentation

**Status: In progress / maintained alongside development**

### Production Deployment

**Status: Not claimed**

The current system should be considered a development and research prototype.

---

## 23. Conclusion

The Pharmacovigilance Intelligence System demonstrates a structured approach to retrieving and managing drug safety evidence.

The project combines:

- Public safety-data retrieval
- Evidence normalization
- Schema validation
- Provenance preservation
- Structured storage
- Duplicate handling
- Automated testing
- Runtime documentation

The completed automated testing result of `10 passed` provides evidence that the implemented Phase 4 test suite executed successfully.

The project provides a foundation that can be extended into a more comprehensive pharmacovigilance evidence intelligence platform.

---

## 24. Disclaimer

This software is a research and development prototype.

It is not intended to replace qualified pharmacovigilance professionals, clinicians, regulatory authorities, or formal safety assessment procedures.

Information retrieved from public safety databases should be interpreted within the limitations of the underlying source data and appropriate pharmacovigilance methodology.

---