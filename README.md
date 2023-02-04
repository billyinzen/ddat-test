# DIT-DDAT Time Parser Function

Craig Duggan

## 1.  Run the Virtual Environment
1.  Open the folder containing the project in the terminal
2. Run the command `.\.venv\Scripts\activate`

## 2. Run the Parser

    py app.py [modification commands...]

To call the parser from the virtual environment, use the command `py app.py` followed by one or more time modification strings.
Please note that modification strings must be enclosed in quotation marks (`"`).

Output will return in a tab-separated format with one line for each modification string provided:
    Modified date & time    modification string
    YYYY-MM-DDTHH:mm:ssZ    now()+1h...

## 3. Import the Parser
The `app.py` file exposes the parse method and can be imported into another project.

### Extra - Run the Tests
To run all unit tests from the venv, run the command:
    python -m unittest discover -p "*_tests.py"