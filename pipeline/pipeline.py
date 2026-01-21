import sys
try:
    import pandas as pd
    print(f"Pandas is installed! Version: {pd.__version__}")
except ImportError:
    print("Pandas is NOT installed.")

    

print("Argument:", sys.argv)
month = sys.argv[1]

df = pd.DataFrame({"Day":[1, 2], "Num_Passengers":[3,4]})

# Add month Column
df['month'] = month
print(df.head())

#convert DF for Parquet file
#Later-on we can upload this to S3 for example
df.to_parquet(f"output_{month}.parquet")


print(f"Hello pipeline, month: {month}")