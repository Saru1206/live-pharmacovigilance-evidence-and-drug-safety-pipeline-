# System Architecture

## Pharmacovigilance Intelligence System

## 1. Overview

The Pharmacovigilance Intelligence System is organized as a modular Python application for retrieving, processing, normalizing, validating, storing, and testing drug safety evidence.

The architecture separates the major responsibilities of the system so that each component can be developed and tested independently.

The overall architecture is:

User
→ Application
→ OpenFDA Connector
→ Evidence Processing
→ Evidence Normalization
→ Schema Validation
→ Evidence Store
→ Stored Evidence

Automated tests provide an additional verification layer across the implemented components.

---

## 2. High-Level Architecture

The system consists of the following major layers:

### Layer 1 — User / Application Layer

The user interacts with the application through `app.py`.

The application accepts the drug name and initiates the safety evidence retrieval workflow.

---

### Layer 2 — Data Retrieval Layer

The OpenFDA connector communicates with the OpenFDA drug-event API.

File:

`src/openfda_connector.py`

Responsibilities include:

- Sending API requests
- Passing drug-search parameters
- Receiving API responses
- Handling API-related failures
- Returning retrieved information to the application

---

### Layer 3 — Evidence Processing Layer

Retrieved source information is processed before being stored as project evidence.

The processing stage extracts the information required by the project's evidence model.

The objective is to convert source-specific information into a form that can be normalized consistently.

---

### Layer 4 — Evidence Normalization Layer

File:

`src/normalize_evidence.py`

The normalization component converts processed information into the project's standardized evidence representation.

Normalization helps ensure that evidence records follow a consistent structure.

The normalized representation includes concepts such as:

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

### Layer 5 — Validation / Schema Layer

File:

`src/evidence_schema.py`

The evidence schema defines the expected structure of normalized evidence.

Validation helps identify records that do not conform to the expected evidence structure.

The validation layer provides a controlled boundary between raw or processed information and stored evidence.

---

### Layer 6 — Evidence Storage Layer

File:

`src/evidence_store.py`

The evidence store manages persistence of normalized evidence records.

The prototype uses structured JSON-based storage.

The storage layer also supports duplicate-ingestion control so that the same evidence is not unnecessarily stored multiple times.

---

## 3. Component Architecture

The main components are:

| Component | File | Primary Responsibility |
|---|---|---|
| Application | `app.py` | Main user-facing workflow |
| OpenFDA Connector | `src/openfda_connector.py` | API communication |
| Evidence Schema | `src/evidence_schema.py` | Evidence structure and validation |
| Evidence Normalizer | `src/normalize_evidence.py` | Evidence normalization |
| Evidence Store | `src/evidence_store.py` | Evidence persistence and duplicate handling |
| Phase 4 Tests | `tests/test_phase4.py` | Automated verification |

---

## 4. Data Flow

The main data flow is:

User Input
→ Drug Name
→ API Request
→ OpenFDA Response
→ Response Processing
→ Evidence Normalization
→ Schema Validation
→ Evidence Storage
→ Retrieved / Stored Evidence

Each stage has a specific responsibility.

---

## 5. API Retrieval Flow

The API retrieval process follows:

1. The user provides a drug name.
2. `app.py` receives the input.
3. The application calls the OpenFDA connector.
4. The connector constructs the API request.
5. OpenFDA returns the response.
6. The response is processed by the application.
7. Relevant information is passed to the evidence-processing workflow.

If the API request fails, the application reports the error rather than treating the request as successful evidence retrieval.

---

## 6. Evidence Normalization Flow

The normalization process follows:

Raw / Retrieved Information
→ Field Extraction
→ Standardized Evidence Fields
→ Evidence Object
→ Validation

The purpose of normalization is to reduce variation in how evidence is represented internally.

This allows evidence retrieved from the source to follow a consistent project-level structure.

---

## 7. Evidence Schema

The normalized evidence model provides a structured representation of safety evidence.

Important fields include:

### Evidence ID

A project-level identifier for the evidence record.

### Drug Name

The drug associated with the evidence.

### Adverse Event

The reported safety event associated with the record.

### Source

The external source from which the evidence originated.

### Source Record ID

The identifier associated with the original source record.

### Evidence Type

The type or category assigned to the evidence.

### Retrieved At

The time at which the evidence was retrieved.

### Source URL

The source location associated with the evidence where available.

### Schema Version

The version of the internal evidence structure.

### Provenance

Information describing the origin and processing history of the evidence.

---

## 8. Provenance Architecture

Provenance is maintained through the evidence lifecycle.

The conceptual provenance chain is:

External Source
→ Source Record
→ Retrieval
→ Processing
→ Normalization
→ Validation
→ Storage

This allows an internal evidence record to retain information about its source.

Provenance is important because pharmacovigilance evidence should remain traceable to the information from which it was derived.

---

## 9. Evidence Storage Architecture

The prototype uses structured JSON storage.

The evidence storage workflow is:

Validated Evidence
→ Evidence Store
→ JSON File

The stored evidence can subsequently be read and used by other parts of the system.

The storage layer also checks for duplicate evidence before adding a new record.

---

## 10. Duplicate Handling

Duplicate handling is implemented at the evidence-storage stage.

The conceptual behavior is:

New Evidence
→ Check Existing Records
→ If New → Store
→ If Duplicate → Do Not Store Again

This reduces unnecessary duplication when the same evidence is ingested repeatedly.

---

## 11. Error Handling Architecture

The system handles errors at important boundaries.

### API Errors

If the external API request fails, the application reports the failure.

### No-Result Responses

If a drug search produces no matching records, the system can report that no safety records were found.

### Validation Errors

If an evidence record does not satisfy the expected schema, the validation stage reports the relevant errors.

### Storage Errors

Storage operations are separated into the evidence-store component so that persistence-related behavior can be handled independently from API retrieval.

---

## 12. Testing Architecture

Automated testing is implemented using pytest.

Test file:

`tests/test_phase4.py`

The testing layer verifies important behaviors of the implemented system.

The recorded Phase 4 execution produced:

`10 passed`

The testing architecture provides a separate verification layer rather than relying only on manual application execution.

---

## 13. Module Dependency Concept

The main dependency relationship can be represented as:

`app.py`
→ `openfda_connector.py`

`app.py`
→ `normalize_evidence.py`

`normalize_evidence.py`
→ `evidence_schema.py`

`app.py`
→ `evidence_store.py`

`tests/test_phase4.py`
→ Project Components

This modular arrangement separates external data retrieval from internal evidence processing and storage.

---

## 14. Project Directory Architecture

The project is organized approximately as follows:

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

## 15. Design Principles

The architecture follows several basic principles.

### Modularity

Different responsibilities are separated into individual modules.

### Traceability

Evidence retains information about its source and processing history.

### Consistency

Normalization and schema validation provide a consistent internal representation.

### Testability

Important components can be tested independently.

### Reproducibility

Runtime commands and test results are documented.

### Separation of Concerns

API communication, evidence processing, validation, storage, and testing are handled as distinct responsibilities.

---

## 16. Security and Reliability Considerations

The current system is a prototype and does not claim production-grade security.

Important considerations for future development include:

- Secure configuration management
- API request monitoring
- Rate-limit handling
- Input validation
- Logging
- Access control
- Database security
- Audit logging
- Error monitoring
- Backup and recovery

These are future considerations rather than claims of completed production functionality.

---

## 17. Scalability Considerations

The current JSON-based storage approach is appropriate for prototype development and testing.

For larger deployments, the storage architecture could be extended to a dedicated database.

Possible future improvements include:

- Relational database storage
- Document database storage
- Search indexing
- Batch ingestion
- Background processing
- API caching
- Distributed processing
- Evidence versioning

These improvements would allow the system to handle larger evidence volumes.

---

## 18. Current Architecture Limitations

The current architecture has several limitations:

- It primarily demonstrates a prototype workflow.
- It depends on the availability of the OpenFDA API.
- The current source coverage is limited.
- JSON storage is not intended for large-scale production workloads.
- Automated signal detection is not implemented as a production capability.
- Clinical causality is not automatically established.
- Expert pharmacovigilance assessment remains necessary.

---

## 19. Future Architecture

A future production-oriented architecture could expand the current design to:

Data Sources
→ Ingestion Layer
→ Data Validation
→ Normalization
→ Evidence Store
→ Search / Indexing
→ Signal Detection
→ Evidence Ranking
→ Human Review
→ Reporting / Dashboard

Additional data sources could be integrated while retaining the same normalized evidence model.

---

## 20. Architecture Summary

The current system uses a modular pipeline architecture:

**Input → Retrieval → Processing → Normalization → Validation → Storage → Testing**

The architecture separates external API communication from evidence representation and storage.

This provides a foundation for future expansion into a broader pharmacovigilance evidence intelligence platform while keeping the current prototype understandable, testable, and traceable.

---

## 21. Architecture Status

**Current Status: Prototype Architecture Completed**

Implemented architectural areas include:

- Application layer
- OpenFDA retrieval layer
- Evidence normalization
- Evidence schema
- Evidence validation
- Evidence storage
- Duplicate handling
- Automated testing
- Documentation

The architecture is suitable for the current research and development stage of the project.