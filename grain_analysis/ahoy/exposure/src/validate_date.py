%%writefile validate_date.py

from datetime import datetime

class DateValidation:
    """
    Utility class for validating filename dates against the current date.
    Methods:
        - get_current_yyyymm(): Returns current date in YYYYMM format
        - is_filename_current(filename): Checks if filename suffix matches current YYYYMM
    """

    @staticmethod
    def current_reporting_date():
        """
        Returns the reporting date in YYYYMM format.
        Logic: The reporting date is always the previous month from today.

        Example:
            If today is April 2, 2026 → returns '202603'
        """
        today = datetime.today() # datetime.today() returns the current date and time as a datetime object.
        year = today.year # get the year
        month = today.month - 1 # subtracts 1 from the current month to get the previous
        if month == 0:  # if the current month is January (1), its 1 -1 = 0
            # there’s no month 0, so we:
            month = 12 # set month = 12 (December)
            year -= 1 # go back one year (year -= 1)

        return f"{year}{month:02d}"
            # year → stays as-is, e.g., 2026
            # month:02d → ensures the month is two digits, padding with zero if necessary.
            # Example: March → "03", December → "12"

    @staticmethod
    def is_filename_current(filename):
        """
        Checks if the filename suffix (YYYYMM) matches the expected previous month.

        Logic to extract suffix:
            suffix = filename.split("_")[-1].replace(".csv", "")

        Step-by-step:
            1. filename.split("_")
                Splits the filename string into a list using "_" as the delimiter.
                Example:
                    "Ahoy_IMPersonalBoatownersExposure_ITD_202603.csv"
                    →
                    ["Ahoy", "IMPersonalBoatownersExposure", "ITD", "202603.csv"]
            2. [-1]
                Selects the last element of the list, which contains the date and file extension.
                Result: "202603.csv"
            3. .replace(".csv", "")
                Removes the ".csv" extension from the string.
                Result: "202603"

        Final Output:
            A string representing the date suffix in YYYYMM format.

        Assumptions:
            - The filename follows the pattern:
              <prefix>_<prefix>_<prefix>_YYYYMM.csv
            - The date suffix is always the last underscore-separated segment.
            - The file extension is always ".csv".

        Limitations:
            - Will fail or produce incorrect results if the filename structure changes.
            - Not robust against unexpected formats (e.g., extra underscores or different extensions).

        Returns:
            bool: True if suffix matches previous month, False otherwise.
        """
        try:
            # Extract the suffix
            suffix = filename.split("_")[-1].replace(".csv", "")
            expected = DateValidation.current_reporting_date()

            # Compare with expected previous month
            if suffix != expected:
                print(
                    f"Warning: File reporting date '{suffix}' "
                    f"does not match expected reporting date '{expected}'."
                )
                validation_result = False
            else:
                print(
                    f"File date '{suffix}' matches the expected reporting date '{expected}'."
                )
                validation_result = True

            # Function executed successfully
            # If we reach this line, it means no errors or exceptions occurred
            execution_success = True  # This variable indicates that the try block ran successfully

            return execution_success, validation_result

        except Exception as e:
            print(f"Error validating filename: {e}")
            return False, False
               # Return two False values:
                # 1. execution_success = False
                #    - Indicates the function itself did NOT run successfully (it raised an exception)
                # 2. validation_result = False
                #    - Indicates we could NOT determine whether the filename is valid,
                #      because the function failed before completing the check
