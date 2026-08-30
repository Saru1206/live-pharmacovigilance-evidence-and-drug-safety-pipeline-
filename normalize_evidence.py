from src.evidence_schema import EvidenceRecord, generate_evidence_id


def normalize_record(raw_record, index, retrieved_at, source_url):
    """
    Convert one OpenFDA/FAERS record into our standard EvidenceRecord.
    """

    patient = raw_record.get("patient", {})

    drugs = patient.get("drug", [])
    reactions = patient.get("reaction", [])

    # Get first available drug name
    drug_name = None
    drug_identifier = None

    if drugs:
        first_drug = drugs[0]

        drug_name = first_drug.get("medicinalproduct")

        openfda = first_drug.get("openfda", {})

        if openfda:
            identifiers = openfda.get("application_number", [])
            if identifiers:
                drug_identifier = identifiers[0]

    # Get first reported reaction
    adverse_event = None

    if reactions:
        adverse_event = reactions[0].get("reactionmeddrapt")

    # Original OpenFDA/FAERS report ID
    source_record_id = raw_record.get("safetyreportid")

    # Create provenance information
    provenance = {
        "source_system": "OpenFDA",
        "underlying_dataset": "FAERS",
        "retrieval_method": "REST API",
        "transformation": "raw JSON -> normalized evidence"
    }

    record = EvidenceRecord(
        evidence_id=generate_evidence_id(index),
        drug_name=drug_name,
        drug_identifier=drug_identifier,
        adverse_event=adverse_event,
        source="OpenFDA/FAERS",
        source_record_id=source_record_id,
        evidence_type="FAERS adverse-event report",
        event_date=None,
        retrieved_at=retrieved_at,
        source_url=source_url,
        schema_version="1.0",
        provenance=provenance,
        raw_record_reference=source_record_id
    )

    return record