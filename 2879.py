import pandas as pd


def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.head(3)

# Runtime: 677 ms Beats 32.38% of users with Pandas
# Memory Usage: 65.31 MB Beats 54.49% of users with Pandas