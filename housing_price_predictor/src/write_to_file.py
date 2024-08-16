import pandas as pd 

def write_to_file(file_name: str, content: pd.DataFrame) -> None:
    """Writes a DataFrame back to an Excel file."""
    content.to_excel(file_name, index=False)