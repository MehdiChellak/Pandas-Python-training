import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    activities.sort_values("product", inplace = True)
    activities1 = activities.groupby(by="sell_date")["product"].nunique().reset_index(name="num_sold")

    activities1["products"] = activities.groupby(by="sell_date")["product"].unique().agg(lambda x: ','.join(x)).reset_index(name = "products")["products"]
    
    return pd.DataFrame(activities1)


# Good Practice 

def categorize_products2(activities: pd.DataFrame) -> pd.DataFrame:
    return activities.groupby(
        'sell_date'
    )['product'].agg([
        ('num_sold', 'nunique'),
        ('products', lambda x: ','.join(sorted(x.unique())))
    ]).reset_index()
