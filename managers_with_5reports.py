import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    
    # Merge the DataFrame with itself to get the manager of each employee
    merged_df = pd.merge(employee, employee, how="inner", left_on='managerId', right_on='id')
    
    # Group by manager id and name, calculate the counts of each manager
    manager_counts_df = merged_df.groupby(by=['id_y', 'name_y']).size().reset_index(name='counts')
    
    # Rename columns for clarity
    manager_counts_df.rename(columns={'id_y': 'id', 'name_y': 'name'}, inplace=True)
    
    # Filter managers with at least 5 employees and select only the 'name' column
    
    return manager_counts_df[manager_counts_df['counts'] >= 5][['name']]