%%writefile upload.py

from google.colab import files
import pandas as pd

def upload_file():
    """
    Upload a single CSV file in Colab that starts with
    'Ahoy_IMPersonalBoatownersExposure_ITD_'.
    Returns the DataFrame and the filename.
    """
    try:
        uploaded = files.upload()
        # {filename: bytes}, saved to disk
        # Opens file picker and returns a dictionary {filename: bytes}

        valid_files = [f for f in uploaded.keys()
                       if f.startswith("Ahoy_IMPersonalBoatownersExposure_ITD_")
                       and f.endswith(".csv")]

        if not valid_files:
            raise ValueError(
                "No valid file uploaded. File must start with "
                "'Ahoy_IMPersonalBoatownersExposure_ITD_' and be a CSV."
            )
        return None, None

        filename = valid_files[0]
        df = pd.read_csv(filename)

        return df, filename

    except Exception as e:
        print(f"Error uploading or reading file: {e}")
        return None, None
        # Two None values correspond to the usual return (df, filename)
