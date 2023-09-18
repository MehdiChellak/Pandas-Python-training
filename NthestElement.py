import pandas

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
      
    result = pd.DataFrame()
    result.loc[0,f"getNthHighestSalary({N})"] = nan
    employee.sort_values(["salary"], inplace=True,ascending=False)
    employee = employee.salary.unique()

    if len(employee) >= N:
        result.loc[0,f"getNthHighestSalary({N})"] = employee[N-1]

    return result