from dataclasses import dataclass, asdict
from typing import Optional, Dict, Any


SCHEMA_VERSION = "1.0"


@dataclass
class EvidenceRecord:
    evidence_id: str
    drug_name: Optional[str]
    drug_identifier: Optional[str]
    adverse_event: Optional[str]
    source: str
    source_record_id: Optional[str]
    evidence_type: str
    event_date: Optional[str]
    retrieved_at: str
    source_url: str
    schema_version: str
    provenance: Dict[str, Any]
    raw_record_reference: Optional[str]

    def to_dict(self):
        return asdict(self)


def generate_evidence_id(index: int) -> str:
    return f"EV-{index:06d}"


def validate_evidence(record: EvidenceRecord):
    errors = []

    if not record.evidence_id:
        errors.append("Missing evidence_id")

    if not record.source:
        errors.append("Missing source")

    if not record.evidence_type:
        errors.append("Missing evidence_type")

    if not record.retrieved_at:
        errors.append("Missing retrieved_at")

    if not record.source_url:
        errors.append("Missing source_url")

    if not record.schema_version:
        errors.append("Missing schema_version")

    if not isinstance(record.provenance, dict):
        errors.append("Provenance must be a dictionary")

    return len(errors) == 0, errors