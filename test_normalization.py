import json

from src.openfda_connector import search_drug
from src.normalize_evidence import normalize_record
from src.evidence_schema import validate_evidence


# Search OpenFDA
result = search_drug("ibuprofen", limit=3)


if not result["success"]:

    print("API ERROR:")
    print(result["error"])

else:

    print("OpenFDA connection successful!")
    print("Records received:", result["record_count"])
    print()

    evidence_records = []

    # Normalize each record
    for index, raw_record in enumerate(
        result["raw_response"].get("results", []),
        start=1
    ):

        evidence = normalize_record(
            raw_record,
            index,
            result["retrieved_at"],
            result["source_url"]
        )

        valid, errors = validate_evidence(evidence)

        if valid:

            evidence_records.append(evidence.to_dict())

            print("Evidence Record")
            print("------------------------")
            print("Evidence ID:", evidence.evidence_id)
            print("Drug:", evidence.drug_name)
            print("Adverse Event:", evidence.adverse_event)
            print("Source:", evidence.source)
            print("Source Record ID:", evidence.source_record_id)
            print("Evidence Type:", evidence.evidence_type)
            print("Retrieved At:", evidence.retrieved_at)
            print("Schema Version:", evidence.schema_version)
            print()

        else:

            print("Validation failed:")
            print(errors)


    # Save normalized evidence
    with open("evidence_output.json", "w", encoding="utf-8") as file:

        json.dump(
            evidence_records,
            file,
            indent=4
        )


    print("Evidence saved to evidence_output.json")