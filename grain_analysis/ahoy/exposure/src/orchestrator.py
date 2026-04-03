%%writefile orchestrator.py
from validation_runner import load_validation_modules

class Run:
    """
    Orchestrator for the data pipeline.

    Purpose:
    ---------
    Coordinate the execution of modular functions and report overall execution status.

    Role:
    -----
    - Collect results from each module.
    - Print only high-level execution outcomes.
    - Handle errors or failed executions centrally.

    Usage:
    ------
    Instantiate the class and call `Run()` to execute the pipeline.
    """

    def __init__(self):
        self.df = None
        self.filename = None
        # Dynamically get functions/classes from validation_runner
        modules = load_validation_modules()
        self.load = modules["load"]
        self.valid_key = modules["valid_key"]
        self.valid_date = modules["valid_date"]

    def run(self):
        # Step 1: Upload
        result = self.file_upload()
        if not result:
            return  # 🚫 STOP ENTIRE PIPELINE

        # Step 2: Date validation
        exec_success, valid_date = self.validate_date()
        if not exec_success:
            return  # 🚫 STOP if function itself failed
        if not valid_date:
            print("Invalid reporting date.")
            return  # 🚫 STOP if validation failed

        # Step 3: Primary key validation
        if not self.validate_key():
            return  # 🚫 STOP if key validation failed

        print("✅ Pipeline completed successfully")

    def file_upload(self):

        self.df, self.filename = self.load()
        if self.df is None:
            print("Upload failed or wrong file.")
            return False
            """
            return only exits the current function.
            If df is None, the function returns False immediately.
            If df is not None, the return False line is skipped and execution continues.
            """
        print(f"File uploaded successfully: {self.filename}")
        return self.df, self.filename

    def validate_date(self):
        """
        Validates the filename reporting date and prints execution status.

        Returns:
            tuple:
                execution_success (bool): True if the validation function executed without errors
                validation_result (bool): True if filename matches expected reporting date, False otherwise
        """
        try:
            validator = self.valid_date()
            execution_success, validation_result = validator.is_filename_current(self.filename)

            if execution_success:
                print("Date validation function executed successfully")
            else:
                print("Date validation function failed")

            # Return both flags so orchestrator knows function execution vs validation result
            return execution_success, validation_result

        except Exception as e:
            print(f"Unexpected error in validate_date: {e}")
            return False, False

    def validate_key(self):

        is_valid_key = self.valid_key(self.df)

        if is_valid_key:
            print("Primary key validation is successful")
        else:
            print("Primary key validation failed")

        return is_valid_key
