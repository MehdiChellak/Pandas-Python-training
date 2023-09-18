import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    ll  = list(employee.sort_values(by="salary",ascending = False)["salary"].unique())
    df = pd.DataFrame(columns = ["SecondHighestSalary"])
    temp = ll[1]
    df.loc[0,"SecondHighestSalary "] = temp
    return df