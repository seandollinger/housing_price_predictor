import pandas as pd

def read_from_file(file_name: str) -> pd.DataFrame:
    """Reads data from an Excel file and returns it as a DataFrame."""
    return pd.read_excel(file_name)

def write_to_file(file_name: str, content: pd.DataFrame) -> None:
    """Writes a DataFrame back to an Excel file."""
    content.to_excel(file_name, index=False)

