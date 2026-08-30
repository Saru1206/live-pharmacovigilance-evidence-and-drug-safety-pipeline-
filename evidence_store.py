import json
import os


EVIDENCE_FILE = "evidence_output.json"


def load_evidence():
    """Load existing evidence records."""

    if not os.path.exists(EVIDENCE_FILE):
        return []

    try:
        with open(EVIDENCE_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)

        if isinstance(data, list):
            return data

        return []

    except (json.JSONDecodeError, OSError):
        return []


def save_evidence(records):
    """Save evidence records."""

    with open(EVIDENCE_FILE, "w", encoding="utf-8") as file:
        json.dump(records, file, indent=4)


def add_evidence(new_records):
    """Add only records that are not already stored."""

    existing_records = load_evidence()

    existing_source_ids = {
        record.get("source_record_id")
        for record in existing_records
        if record.get("source_record_id")
    }

    added = 0

    for record in new_records:

        source_id = record.get("source_record_id")

        if source_id and source_id in existing_source_ids:
            continue

        existing_records.append(record)

        if source_id:
            existing_source_ids.add(source_id)

        added += 1

    save_evidence(existing_records)

    return added