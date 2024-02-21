# Scenario Outline to Excel Converter

This script converts a Gherkin scenario outline file (`.feature`) into an Excel file (`.xlsx`). It extracts the scenarios from the outline and populates an Excel sheet with the scenario details.

----------
## Installation

1. **Install Python3:** If you don't have Python3 installed, you can download it from the official [Python website](https://www.python.org/downloads/).

2. **Install OpenPyXL:** OpenPyXL is used to work with Excel files in Python. You can install it via pip, Python's package manager, by running the following command in your terminal or command prompt:

`pip install openpyxl`

----------
## Usage

1. **Clone the Repository:** Clone this repository to your local machine using Git:

`git clone https://github.com/your-username/scenario-outline-to-excel.git`



Alternatively, you can download the ZIP file and extract it.

2. **Navigate to the Directory:** Change your current directory to the project directory:

`cd scenario-outline-to-excel`


3. **Run the Script:** Run the Python script `scenarioOutline_converter.py` using Python3. You can specify the path to your scenario outline file as a command-line argument, or you can run the script and input the file path when prompted:

`python3 scenarioOutline_converter.py`


If you choose to input the file path when prompted, make sure your scenario outline file is in the same directory as the script, or provide the full path to the file.

4. **Provide Additional Column Values:** After running the script, you will be prompted to enter values for additional columns (Countries, Issue Type, Components, Labels, Assignee, Test Type, Test Repository Folder). Enter the values and press Enter.

5. **View the Excel File:** Once the script finishes execution, a file named `scenarios.xlsx` will be generated in the same directory. You can open this file with Microsoft Excel or any other compatible spreadsheet software to view the converted scenarios.
---------
## License

--------------