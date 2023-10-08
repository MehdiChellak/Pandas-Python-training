import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:

    df_top1 = employee.groupby('departmentId').apply(lambda x : x.nlargest(1,'salary', keep='all')).reset_index(drop = True)
    df_joined = pd.merge(df_top1, department, left_on='departmentId', right_on='id', how='inner')

    df_joined.rename(columns = {"name_x":"Employee", "name_y" : "Department", "salary" : "Salary"}, inplace=True)
    return df_joined[["Department","Employee","Salary"]]
