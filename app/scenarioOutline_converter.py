import openpyxl

def transform_scenario_outline(lines):
    examples_index = None
    for i, line in enumerate(lines):
        if line.strip() == "Examples:":
            examples_index = i
            break

    if examples_index is None:
        raise ValueError("Examples table not found in feature file")

    example_header = lines[examples_index + 1].strip().split("|")[1:-1]

    scenarios = []

    for row in lines[examples_index + 2:]:
        row_values = row.strip().split("|")[1:-1]
        scenario = lines[:examples_index]
        for index, value in enumerate(row_values):
            for i, line in enumerate(scenario):
                if f"<{example_header[index].strip()}>" in line:
                    scenario[i] = line.replace(f"<{example_header[index].strip()}>", value.strip())
        scenarios.append("".join(scenario))

    return scenarios

def get_feature_title(lines):
    feature_title = ""
    for line in lines:
        if line.startswith("Feature:"):
            feature_title = line.strip().split("Feature:")[1].strip()
        elif line.startswith("  Scenario Outline:"):
            feature_title += "=> " + line.strip().split("Scenario Outline:")[1].strip()
            break
    return feature_title

def get_user_input(prompt):
    return input(prompt).strip()

def main():
    path = "./scenario.feature"
    feature_file = path.strip()

    with open(feature_file, 'r') as file:
        lines = file.readlines()

    feature_title = get_feature_title(lines)
    scenarios = transform_scenario_outline(lines)

    wb = openpyxl.Workbook()
    ws = wb.active
    ws.append(["#", "Summary", "Description", "Countries", "Issue Type", "Component Names", "Labels", "Assignee Name", "Test Type", "Test Repository Folder"])

    countries = get_user_input("Enter Countries: ")
    issue_type = get_user_input("Enter Issue Type: ")
    component_names = get_user_input("Enter Components: ")
    labels = get_user_input("Enter Labels: ")
    assignee_name = get_user_input("Enter Assignee: ")
    test_type = get_user_input("Enter Test Type: ")
    test_repository_folder = get_user_input("Enter Test Repository Folder: ")

    for i, scenario in enumerate(scenarios, start=1):
        example = scenario.split(':')[-1].split('=')[1].split(';')[0].strip() if 'Example =' in scenario else ''
        ws.append([i, f"{feature_title}: Example = {i} {example}", scenario.strip(), countries, issue_type, component_names, labels, assignee_name, test_type, test_repository_folder])

    wb.save('scenarios.xlsx')

if __name__ == "__main__":
    main()
