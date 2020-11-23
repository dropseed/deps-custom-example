import json
import sys

import yaml

from collect import load_deps


def update_dep(path, name, version):
    # INSERT CUSTOM CODE HERE!
    deps = load_deps(path)

    deps[name] = version  # change the version

    with open(path, "w+") as f:
        yaml.dump(deps, f)


def act(input_path, output_path):
    # Load the schema from collect to find updates we need to make
    with open(input_path, "r") as f:
        data = json.load(f)

    for manifest_path, manifest_data in data.get("manifests", {}).items():
        for dependency_name, updated_dependency_data in manifest_data["updated"][
            "dependencies"
        ].items():
            version_to_update_to = updated_dependency_data["constraint"]
            update_dep(
                path=manifest_path,
                name=dependency_name,
                version=version_to_update_to,
            )

    # Store the results back to disk (including any modifications)
    with open(output_path, "w+") as f:
        json.dump(data, f)


if __name__ == "__main__":
    act(sys.argv[1], sys.argv[2])
