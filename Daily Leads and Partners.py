import pandas as pd


def daily_leads_and_partners(daily_sales: pd.DataFrame) -> pd.DataFrame:
    result =  daily_sales.groupby(by=["date_id", "make_name"])["lead_id"].nunique().reset_index(name="unique_leads")
    result["unique_partners"]  = daily_sales.groupby(by=["date_id", "make_name"])["partner_id"].nunique().reset_index(name="unique_partners")["unique_partners"]
    return result

# Best Practice
def daily_leads_and_partners2(daily_sales: pd.DataFrame) -> pd.DataFrame:
    daily_sales =  daily_sales.groupby(by=["date_id", "make_name"]).agg({'lead_id' : 'nunique', 'partner_id' : 'nunique'}).reset_index()
    return daily_sales.rename(columns = {"lead_id" :"unique_leads", "partner_id" : "unique_partners"})