
def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    orders  = orders.groupby(by="customer_number")["order_number"].count().reset_index(name="counts")
    max = orders["counts"].max()
    orders = orders[ max == orders["counts"]]
    print(max)
    return pd.DataFrame(orders["customer_number"])
    
    