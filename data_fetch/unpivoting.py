import pandas as pd

def sub_pivots(df, label_1, label_2, value_column, subgroup_column=None, subgroup_tag=None):
    """
     Receives a dataframe (df) containing a binary function f(x,y) = z. This is, we have a column where we store x(label_1)
     another one where we store y (label_2) , and another one whre we store z (value_column). The dataframe can also have
     an extra argument(subgroup_column) (thinkable as a condition/flag). If no subgroup_column is given, 
     the df is assumed not to have ordered (x, y) duplicates. For every the condition value (subgroup_tag) from the
     subgroup_column, the function filters the df. The filtered df should have no duplicates (x, y).

     The df returns a matrix representation of a the function. Fills with NaN the non given (y, x) outputs, 
     if (x, y) is given.
    """
    if subgroup_column is not None:
        filtered = df[df[subgroup_column] == subgroup_tag]
    else:
        filtered = df
    pivoted = filtered.pivot(index=label_1, columns=label_2, values=value_column)
    return pivoted
