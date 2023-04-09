import json
import jsonschema
import sys
import glob

# JSON schema
schema = {
    "type": "object",
    "required": ["mods", "desc", "name", "authors"],
    "properties": {
        "mods": {
            "type": "array",
            "items": {
                "type": "string"
            }
        },
        "desc": {"type": "string"},
        "name": {"type": "string"},
        "authors": {
            "type": "array",
            "items": {
                "type": "string"
            }
        }
    }
}

# Validate JSON files
for file_path in glob.glob("**/*.json", recursive=True):
    with open(file_path) as f:
        try:
            json_data = json.load(f)
            jsonschema.validate(instance=json_data, schema=schema)
        except (json.JSONDecodeError, jsonschema.exceptions.ValidationError) as e:
            print(f"{file_path}: {e}")
            sys.exit(1)
