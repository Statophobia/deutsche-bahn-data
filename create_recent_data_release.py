import pandas as pd
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from pathlib import Path

def merge_recent_dataframes(n_months=4):
    file_names = [(now - relativedelta(months=i)).strftime("data-%Y-%m.parquet") for i in range(4)]
    monthly_dataframes = [pd.read_parquet(data_dir/file_name) for file_name in file_names]
    combined_df = pd.concat(monthly_dataframes)
    return combined_df
    
def filter_train(df, train_type):
    date_threshold = now - timedelta(days=90)
    filtered_df = df[df.train_type.isin(train_type) & (df.time > date_threshold)]
    return filtered_df

def main():
    combined_df = merge_recent_dataframes()
    filtered_df = filter_train(combined_df, trains_considered)
    
    output_file = data_dir / "recent_data.parquet"
    filtered_df.to_parquet(
        output_file,
        index=False,
        compression="brotli",
    )

if __name__ == "__main__":
    now = datetime.now()
    data_dir = Path("monthly_data_releases")
    trains_considered = ['ICE', 'IC', 'EC']

    main()