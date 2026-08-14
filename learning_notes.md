# Phase 1 — Learning Notes

## Live Pharmacovigilance Evidence & Drug Safety Intelligence Pipeline v1

### 1. Purpose of Phase 1

The purpose of Phase 1 was to learn the technical and pharmacovigilance concepts required to build a live drug-safety evidence pipeline.

The task is not to build a medical decision-making system. The objective is to create a research-oriented system that can collect, structure, search, and trace publicly available drug-safety evidence while preserving the distinction between source evidence and system interpretation.

The primary source selected for the initial implementation is **OpenFDA drug adverse-event data based on the FDA Adverse Event Reporting System (FAERS)**.

---

## 2. What I Learned

### 2.1 Pharmacovigilance

Pharmacovigilance involves monitoring and evaluating medicine-related safety information.

For this project, pharmacovigilance data is treated as research evidence that can be collected and organized for safety analysis.

The system should not make clinical decisions or provide treatment recommendations.

### 2.2 FDA Adverse Event Reporting System (FAERS)

FAERS is an FDA system containing reports of adverse events and medication errors associated with FDA-regulated products.

FAERS is useful for post-market drug-safety surveillance.

An important limitation is that an adverse-event report does not automatically establish that a particular drug caused a particular reaction.

Therefore, the system must preserve the reported evidence without converting it into an unsupported causal conclusion.

### 2.3 OpenFDA

OpenFDA provides programmatic access to public FDA datasets.

For this project, the relevant endpoint is the drug adverse-event endpoint:

`https://api.fda.gov/drug/event.json`

Using an API allows the Python application to retrieve public drug-safety information programmatically instead of manually downloading and processing data.

### 2.4 REST APIs

An API allows one software system to communicate with another.

The basic workflow learned for this project is:

```text
Python Application
       ↓
API Request
       ↓
OpenFDA
       ↓
API Response
       ↓
Python Application
```

The HTTP `GET` method is used to request information.

OpenFDA supports field-based searches and limits on the number of returned records.

### 2.5 JSON

OpenFDA returns data in JSON format.

JSON allows structured information to be represented using objects, arrays, fields, and values.

A simplified example is:

```json
{
    "drug": "Example Drug",
    "reaction": "Example Reaction",
    "source": "OpenFDA"
}
```

The actual OpenFDA response is more complex and contains nested information.

The application therefore needs to extract the relevant fields rather than treating the response as a simple flat table.

### 2.6 FAERS Record Structure

A drug adverse-event record can contain information related to:

- report information
- patient information
- drugs
- reactions

Important fields identified during learning include the report identifier, drug information, reaction information, and relevant date fields.

The report identifier is important because the normalized evidence needs to maintain a reference to the original source record.

### 2.7 Adverse Event and ADR Terminology

An important concept learned during Phase 1 is the distinction between an **adverse event** and a confirmed causal relationship.

A reported event involving a drug should not automatically be described as:

> "The drug caused the reaction."

Instead, the system should preserve the source wording and communicate that the event was reported in a safety record involving the drug.

This prevents the research system from making unsupported clinical conclusions.

### 2.8 Drug Names and Identifiers

Drug information may be represented through different names or identifiers.

Drug names in adverse-event reports may not always be perfectly standardized.

OpenFDA may also provide harmonized drug information when available.

The system should distinguish between information supplied by the original source and information added or harmonized by OpenFDA.

If a required value is not provided by the source, the system should use an explicit `NULL` or `UNKNOWN` representation rather than inventing a value.

---

## 3. Evidence Schema

The assignment requires a normalized internal evidence schema.

The minimum conceptual fields identified are:

| Field | Purpose |
|---|---|
| `evidence_id` | Unique identifier created by the system |
| `drug_name` | Reported drug name |
| `drug_identifier` | Drug identifier when available |
| `adverse_event` | Reported adverse event/reaction |
| `source` | Source of the evidence |
| `source_record_id` | Original source record identifier |
| `evidence_type` | Type of evidence |
| `event_date` | Relevant source date when available |
| `retrieved_at` | Time the system retrieved the data |
| `source_url` | Source/API reference |
| `schema_version` | Version of the internal schema |
| `provenance` | Traceability information |
| `raw_record_reference` | Reference to the original raw record |

The schema is intended to create a consistent representation of evidence without changing the meaning of the original source data.

---

## 4. Provenance

One of the most important concepts learned was **data provenance**.

Provenance answers questions such as:

- Where did this record come from?
- When was it retrieved?
- Which source record produced it?
- What transformation was applied?
- Which schema version was used?
- Where can the original record be traced?

The intended evidence flow is:

```text
OpenFDA / FAERS
       ↓
Raw Source Record
       ↓
Validation
       ↓
Normalization
       ↓
Evidence Record
       ↓
Provenance
```

Provenance is necessary because a researcher should be able to trace a normalized evidence record back toward its originating source.

---

## 5. Normalization

The source API uses a nested JSON structure, while the research application needs a consistent internal structure.

Normalization means transforming the source representation into the project's evidence schema.

Conceptually:

```text
OpenFDA JSON
      ↓
Extract relevant information
      ↓
Validate
      ↓
Normalize
      ↓
Internal Evidence Schema
```

Normalization must not silently change the scientific meaning of the source evidence.

---

## 6. Important Data Limitation

A major learning point is that one FAERS report may contain multiple drugs and multiple reactions.

Therefore, the presence of a drug and a reaction in the same report does not automatically establish that the specific drug caused the specific reaction.

For example:

```text
Report
 ├── Drug A
 ├── Drug B
 ├── Reaction X
 └── Reaction Y
```

The system should preserve this as source evidence rather than automatically creating an unsupported causal statement such as:

```text
Drug A caused Reaction X
```

This limitation is important for both the schema design and the final research interface.

---

## 7. Data Quality and Source Limitations

The following limitations were identified during Phase 1:

1. Adverse-event reporting does not represent every event that occurs.
2. Reports may contain multiple drugs.
3. Reports may contain multiple reactions.
4. Reported events should not automatically be interpreted as confirmed causation.
5. Drug names may not always be standardized.
6. Some fields may be unavailable for particular records.
7. OpenFDA data may not represent real-time information.
8. OpenFDA data can lag the underlying FAERS data.
9. Missing fields should not be fabricated.
10. Source information and system-generated information must remain distinguishable.

These limitations will be considered during the build and testing phases.

---

## 8. What Was Confusing

The following concepts required additional understanding:

### 8.1 Adverse event vs causation

Initially, it can be easy to interpret a drug and reaction appearing in the same safety report as proof that the drug caused the reaction.

The important clarification is that the system must preserve the reported association without making a causal medical conclusion.

### 8.2 Multiple drugs and reactions

A single safety report can contain multiple drugs and multiple reactions. This makes it important to preserve the original report identifier and avoid creating unsupported drug-reaction relationships.

### 8.3 Source fields vs application fields

It was necessary to distinguish between:

- fields provided by OpenFDA/FAERS,
- fields generated by the application,
- fields describing the transformation and provenance.

### 8.4 Event date vs retrieval date

The date associated with the source record and the date when the application retrieves the record are different concepts.

The system therefore needs both source-related date information and a `retrieved_at` timestamp.

---

## 9. How AI Assisted Me

AI was used as a learning and development support tool during Phase 1.

AI assistance was used to:

- explain pharmacovigilance terminology;
- explain the difference between adverse events and causal conclusions;
- explain REST APIs and JSON;
- explain the OpenFDA data structure;
- identify concepts relevant to provenance;
- explain normalization;
- help map source information to the proposed internal evidence schema;
- identify potential limitations and failure cases that should be considered during implementation.

AI explanations were treated as guidance rather than as the final authority for biomedical or technical facts.

---

## 10. What I Independently Verified

Important technical information was checked against official FDA/openFDA documentation.

The verification focused on:

- the OpenFDA drug adverse-event endpoint;
- FAERS as the underlying adverse-event reporting system;
- the general structure of adverse-event records;
- report identifiers;
- drug and reaction information;
- OpenFDA search behavior;
- API response structure;
- API limitations and data-update considerations.

Official documentation was preferred over relying solely on AI-generated explanations.

---

## 11. Unresolved Assumptions

The following points will be verified during implementation rather than assumed:

1. Exact field mappings from every required internal schema field to OpenFDA fields.
2. Handling of records containing multiple drugs and multiple reactions.
3. The final method for generating unique `evidence_id` values.
4. The exact raw-record storage/reference strategy.
5. The final provenance structure.
6. Duplicate-record handling.
7. Repeat-ingestion behavior.
8. API failure and malformed-response behavior.
9. The final search interface/API implementation.
10. The exact validation rules for the normalized evidence schema.

These issues will be addressed and tested during Phase 2 and Phase 4.

---

## 12. Phase 1 Technical Understanding

The complete system concept learned during Phase 1 is:

```text
Public Biomedical Source
          ↓
Source Retrieval
          ↓
Raw Evidence Capture
          ↓
Validation
          ↓
Normalization
          ↓
Provenance Record
          ↓
Drug/Safety Evidence Store
          ↓
Search
          ↓
Research View
          ↓
Evidence Trace
```

The central principle is:

```text
Real Evidence
      ↓
Structured Evidence
      ↓
Traceable Result
```

The system should preserve the distinction between:

```text
SOURCE EVIDENCE
       and
SYSTEM INTERPRETATION
```

---

## 13. Phase 1 Conclusion

Phase 1 established the foundational knowledge required to begin development of the Live Pharmacovigilance Evidence & Drug Safety Intelligence Pipeline.

The main concepts learned were OpenFDA/FAERS, REST APIs, JSON, pharmacovigilance terminology, drug and reaction information, normalization, provenance, reproducible ingestion, and the limitations of spontaneous adverse-event reporting.

The next phase will move from learning to implementation.

The first implementation component will be the **OpenFDA Source Connector**, which will retrieve real public drug-safety data, handle API failures safely, preserve the raw response where practical, and prepare structured data for validation and normalization.

**Phase 1 Status: COMPLETE**
