# Tuple Unpacking / Multiple Assignment in Python
# -----------------------------------------------
#
# Concept:
#     In Python, functions can return multiple values at once by returning a tuple.
#     A tuple is an ordered collection of values, and Python allows you to "unpack"
#     the values from a tuple directly into multiple variables in a single line.
#
# Example:
#
#     # Function returning multiple values as a tuple
#     def load_file():
#         df = read_csv("data.csv")  # a pandas DataFrame
#         filename = "data.csv"      # filename string
#         return df, filename         # returns a tuple (df, filename)
#
#     # Unpacking the returned tuple into separate variables
#     self.df, self.filename = load_file()
#
#     # Now:
#     # self.df contains the DataFrame
#     # self.filename contains the filename string
#
# Explanation:
#     1. The function returns a tuple with two elements: (df, filename).
#     2. The left-hand side of the assignment contains two variables separated by commas.
#     3. Python assigns the first element of the tuple to the first variable,
#        and the second element to the second variable.
#     4. This allows multiple values to be returned and assigned in a single line.
#
# Application in Data Pipeline:
#
#     - upload_file() returns (df, filename)
#         -> Assigned as: self.df, self.filename = upload_file()
#         -> self.df holds the DataFrame, self.filename holds the file name.
#
#     - validate_primary_key(df) returns (duplicates_df, status)
#         -> Assigned as: duplicates_df, status = validate_primary_key(df)
#         -> duplicates_df holds the DataFrame of duplicates
#         -> status holds a Boolean indicating if the primary key is valid
#
# Benefits:
#     - Cleaner code without needing intermediate variables or containers like lists or dicts.
#     - Easy to read and maintain, especially when a function naturally produces multiple outputs.
#     - Common pattern in Python for returning multiple related values.
