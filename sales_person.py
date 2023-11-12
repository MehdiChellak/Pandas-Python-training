import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    # Get the ID of the company named 'RED'
    red_company = company[company['name'] == 'RED']
    
    # If 'RED' company is not found, return all salesperson names
    if red_company.empty:
        return sales_person[['name']]
    
    id_red = red_company.iloc[0]['com_id']
    
    # Select sales IDs from the 'orders' table associated with the 'RED' company
    red_sales_ids = orders.loc[orders['com_id'] == id_red, 'sales_id'].unique()
    
    # Filter salespersons whose IDs are not in the 'red_sales_ids' array
    result = sales_person[~sales_person['sales_id'].isin(red_sales_ids)][['name']]
    
    return result