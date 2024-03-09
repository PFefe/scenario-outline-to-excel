# Scenario Outline to Excel Converter

This script converts a Gherkin scenario outline file (`.feature`) into an Excel file (`.xlsx`). It extracts the scenarios from the outline and populates an Excel sheet with the scenario details.

----------
# Converting Scenario Outlines to Excel

This script converts a Gherkin scenario outline file (.feature) into an Excel file (.xlsx). It extracts the scenarios from the outline and populates an Excel sheet with the scenario details.

## Repository and Files

- Repository URL: [GitHub - scenario-outline-to-excel](https://github.com/PFefe/scenario-outline-to-excel)
- Scenario Outline Converter App: `scenarioOutline_converter.py`
- Feature File Sample: `scenario.feature`
- Xray Import Configuration File: `importConfiguration.json`

## Installation

1. **Install Python3:** If you don't have Python3 installed, you can download it from the [official Python website](https://www.python.org/downloads/).

    ```bash
    brew install python@3.11
    ```
     ```bash
    yarn add python3.11
    ```

2. **Install OpenPyXL:** OpenPyXL is used to work with Excel files in Python. You can install it via pip, Python's package manager, by running the following command in your terminal or command prompt:

    ```bash
    pip3 install openpyxl
    ```

## Usage

1. **Clone the Repository:** Clone the `scenario-outline-to-excel` repository to your local machine using Git:

    ```bash
    git clone https://github.com/PFefe/scenario-outline-to-excel.git
    ```

    Alternatively, you can download the ZIP file and extract it.

2. **Navigate to the Directory:** Change your current directory to the project directory:

    ```bash
    cd scenario-outline-to-excel/app
    ```

3. **Change Feature file content:** Copy your scenario outline block with feature name into the `scenario.feature` file. Please match with the default format as `Feature:` => `Scenario Outline:` => `Examples:` . Please note that, it supports only one scenario outline file per iterations. So you can simply copy paste the scenario outlines one by one wirh feature block and save the output by appending the csv or xlsx file to be imported. 

4. **Run the Script:** Run the Python script `scenarioOutline_converter.py` using Python3:

    ```bash
    python3 scenarioOutline_converter.py
    ```

5. **Provide Additional Column Values:** After running the script, you will be prompted to enter values for additional columns (Countries, Issue Type, Components, Labels, Assignee, Test Type, Test Repository Folder{like:PF-Website/Baseline/Front-End/Partners}). Enter the values and press Enter.

6. **View the Excel File:** Once the script finishes execution, a file named `scenarios.xlsx` will be generated in the same directory. You can open this file with Microsoft Excel or any other compatible spreadsheet software to view the converted scenarios.

# Bulk Import of Test Cases in Xray

Follow the steps below to import Test Cases into Xray using a CSV file:

1. **Convert the xlxs format to a CSV:** You can use Excel, Numbers, or Google Sheets. Please note that csv delimiter type is `;` in excel, it is `,` for others.

2. **Navigate to Xray Test Case Importer:** In Jira, go to `Apps` ➜ `Xray` ➜ `Test Case Importer`.

3. **Upload CSV File:** Choose the `.csv` file you downloaded in step 1.

4. **Upload importConfiguration File:**  `importConfiguration.json` (change delimiter with your version)

5. **Select Project:** Choose the appropriate project (e.g., PF-QA).(Import Configuration File will choose automatically)

6. **Create Test Repository Folders (Optional):** If the Folder structure is not already existing in the PF-QA Test Repository, select the `Create Test Repository folders if needed` toggle in the setup screen to create the required folder structure.

7. **Map Fields:** Refer to the Xray - Map Fields document for guidance on mapping fields correctly.(Import Configuration File will choose automatically)

8. **Begin Import:** Once all fields are mapped, click `Begin Import` to start the import process.

---------
## License

--------------
