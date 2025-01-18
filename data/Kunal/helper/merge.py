import json
from pathlib import Path


def merge_json_files(input_files, output_file):
    merged_data = {"intents": []}

    # Read and combine data
    for file_path in input_files:
        try:
            with open(file_path, "r") as f:
                data = json.load(f)
                if "intents" in data:
                    merged_data["intents"].extend(data["intents"])
        except FileNotFoundError:
            print(f"Error: File not found - {file_path}")
            continue
        except json.JSONDecodeError:
            print(f"Error decoding JSON in {file_path}")
            continue

    # Remove duplicate intents based on the tag, ensuring unique tags
    unique_intents = {}
    for intent in merged_data["intents"]:
        unique_intents[intent["tag"]] = intent

    # Update merged data with the unique intents
    merged_data["intents"] = list(unique_intents.values())

    # Write the merged data to the output file
    with open(output_file, "w") as f:
        json.dump(merged_data, f, indent=4)


# File paths for the input files using relative paths
input_files = [
    Path(__file__).parent / "accounts.json",
    Path(__file__).parent / "alumni_affairs.json",
    Path(__file__).parent / "academic_affair.json",
    Path(__file__).parent / "procurement_section.json",
    Path(__file__).parent / "cds.json",
    Path(__file__).parent / "cep.json",
    Path(__file__).parent / "counselling.json",
    Path(__file__).parent / "eg_saral.json",
    Path(__file__).parent / "library.json",
    Path(__file__).parent / "medical_centre.json",
    Path(__file__).parent / "research_and_consultancy.json",
    Path(__file__).parent / "security_section.json",
    Path(__file__).parent / "student_affairs.json",
    Path(__file__).parent / "tinkerers_lab.json",
    Path(__file__).parent / "tlu.json",
]

# Output file path using relative path
output_file = Path(__file__).parent / "merged_output.json"

# Run the merge function
merge_json_files(input_files, output_file)
