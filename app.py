from src.openfda_connector import search_drug
from src.normalize_evidence import normalize_record
from src.evidence_schema import validate_evidence
from src.evidence_store import add_evidence


print("========================================")
print(" PHARMACOVIGILANCE DRUG SAFETY SEARCH")
print("========================================")

drug_name = input("Enter drug name: ").strip()

if not drug_name:

    print("Please enter a drug name.")

else:

    print()
    print("Searching OpenFDA...")
    print()

    result = search_drug(drug_name, limit=5)

    if not result["success"]:

        print("ERROR:")
        print(result["error"])

    elif result["record_count"] == 0:

        print("No safety records found for:", drug_name)

    else:

        print("Records found:", result["record_count"])
        print()

        new_evidence = []

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

                new_evidence.append(evidence.to_dict())

                print("----------------------------------------")
                print("Evidence ID:", evidence.evidence_id)
                print("Drug:", evidence.drug_name)
                print("Adverse Event:", evidence.adverse_event)
                print("Source:", evidence.source)
                print("Source Record ID:", evidence.source_record_id)
                print("Evidence Type:", evidence.evidence_type)
                print("Retrieved At:", evidence.retrieved_at)
                print("----------------------------------------")
                print()

            else:

                print("Validation failed:")
                print(errors)

        added = add_evidence(new_evidence)

        print("----------------------------------------")
        print("New evidence records saved:", added)
        print("----------------------------------------")