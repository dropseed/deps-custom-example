import os
import sys
import json
import yaml


def load_deps(yaml_path):
    # INSERT CUSTOM CODE HERE!
    with open(yaml_path, "r") as f:
        data = yaml.safe_load(f)
    return data


def get_latest_version(name):
    # INSERT CUSTOM CODE HERE!
    if name == "dependency-a":
        return "1.1.0"


def collect(input_path, output_path):
    # Load the YAML (user input from deps.yml "path")
    deps = load_deps(input_path)

    current_dependencies = {}
    updated_dependencies = {}

    for name, version in deps.items():
        print(f"Collecting {name}")

        installed_version = version

        current_dependencies[name] = {
            "constraint": installed_version,
            "source": "custom",
        }

        latest_version = get_latest_version(name)

        if latest_version and latest_version != installed_version:
            updated_dependencies[name] = {
                "constraint": latest_version,
                "source": "custom",
            }

    # Put the data into the expected JSON schema format
    output = {
        "manifests": {
            input_path: {
                "current": {"dependencies": current_dependencies,},
                "updated": {"dependencies": updated_dependencies,},
            }
        }
    }

    # Save the results
    with open(output_path, "w+") as f:
        json.dump(output, f)


if __name__ == "__main__":
    collect(sys.argv[1], sys.argv[2])
