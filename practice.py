import pandas as pd


imported_csv = pd.read_csv(r'practice_names.csv')

print(type(imported_csv))

new_df = imported_csv.query("age > 35 ")
print(new_df)
print(type(new_df))

result = pd.DataFrame(imported_csv, "\n")
# imported_csv.insert(3, "seniority", "")
# print(imported_csv.loc[imported_csv['age'] >= 35])

# print(imported_csv.loc[imported_csv['age'] >= 35, "seniority"])

# imported_csv.loc[imported_csv['age'] >= 35, "seniority"] = "hello"

# print()
# print(imported_csv)