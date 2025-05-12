import os

def main():
    
    print("imprimir datos")
    print(df.shape)
    print(df.head())


    output_dir = "src/edu_bigdata/static/csv"
    os.makedirs(output_dir, exist_ok=True)

    
    df.to_csv(os.path.join(output_dir, "data_web.csv"), index=False)