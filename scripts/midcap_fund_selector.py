import pandas as pd

df = pd.read_csv("midcap.csv")

print(df.info())
print(df.head())

exp_r = df["Expense ratio"].rank(method="dense") 
avg_rr = df["5-year average Rolling Return"].rank(method="dense", ascending=False)
prob = df[">15% probability"].rank(method="dense", ascending=False)
dsr = df["5-year Downside Ratio"].rank(method="min", ascending=True)
usr = df["5-year Upside Ratio"].rank(method="min", ascending=False) 

df['final_number'] = exp_r * 0.30 + avg_rr * 0.25 + prob * 0.05 + dsr * 0.30 + usr * 0.10

df["final_rank"] = df["final_number"].rank(method="dense")

df.sort_values(by="final_rank", inplace=True)
# df.to_clipboard()
print(df.head())