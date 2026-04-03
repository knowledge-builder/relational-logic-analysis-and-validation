%%writefile validate_key.py

def validate_primary_key(df):
    """
    Checks uniqueness of Policy + RiskNum primary key.
    Returns:
        duplicates_df: DataFrame of duplicates (empty if none)
        status: True if primary key passes, False if duplicates or error
    """
    try:
        required_columns = ['Policy', 'RiskNum']
        for col in required_columns:
            if col not in df.columns:
                raise KeyError(f"Required column '{col}' is missing.")

        duplicates_df = df[df.duplicated(subset=['Policy', 'RiskNum'], keep=False)]

        status = duplicates_df.empty
        # True if df has 0 rows, False if df has ≥1 row
        # Internally equivalent to: len(df.index) == 0
        # .empty just checks the number of rows.
        # No need to iterate — it’s fast and memory-efficient.

        return duplicates_df, status

    except Exception as e:
        print(f"Error during primary key validation: {e}")
        return pd.DataFrame(), False
        # Fallback for exceptions: ensures two values are returned so unpacking works,
        # duplicates_df is a valid DataFrame, and status=False indicates validation failed
