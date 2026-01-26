import click
import pandas as pd
from sqlalchemy import create_engine
from tqdm import tqdm 
import pyarrow.parquet as pq

@click.command()
@click.option('--pg-user', default='root', help='PostgreSQL username')
@click.option('--pg-pass', default='root', help='PostgreSQL password')
@click.option('--pg-host', default='localhost', help='PostgreSQL host')
@click.option('--pg-port', default='5432', help='PostgreSQL port')
@click.option('--pg-db', default='ny_taxi', help='PostgreSQL database name')
@click.option('--year', default=2021, type=int, help='Year of the data')
@click.option('--month', default=1, type=int, help='Month of the data')
@click.option('--chunksize', default=100000, type=int, help='Chunk size for ingestion')
@click.option('--target-table', default='yellow_taxi_data', help='Target table name')


def main(pg_user, pg_pass, pg_host, pg_port, pg_db, year, month, chunksize, target_table):
    # pg_user = 'root'
    # pg_pass = 'root'
    # pg_host = 'localhost'
    # pg_port = 5432
    # pg_db = 'ny_taxi'

    # year = 2021
    # month = 1
    # chunksize = 100000
    # target_table = 'yellow_taxi_data'

    url= './green_tripdata_2025-11.parquet'
    url_zone = './taxi_zone_lookup.csv'
    engine = create_engine(f'postgresql://{pg_user}:{pg_pass}@{pg_host}:{pg_port}/{pg_db}')

    # 1. Open the Parquet file as a ParquetFile object
    parquet_file = pq.ParquetFile(url)

    # 2. Iterate through the file in batches (chunks) && # Use 'batch_size' to define how many rows you want per chunk
    first = True
    for batch in parquet_file.iter_batches(batch_size=chunksize):
        # 3. Convert each batch to a Pandas DataFrame
        df_chunk = batch.to_pandas()
        
        # Process your chunk here...
        print(f"Processing chunk with {len(df_chunk)} rows")
        if first == True:
            df_chunk.to_sql(name=target_table, con=engine, if_exists='replace') 
            # print(pd.io.sql.get_schema(df_chunk, name='green_taxi_data', con=engine))
            first=False
        else:
            df_chunk.to_sql(name=target_table, con=engine, if_exists='append') 




    # Now for the pickup zones
    df = pd.read_csv(
        url_zone,
        iterator=True,
        chunksize=chunksize
    )

    initiator = True
    for dfchunk in tqdm(df):
        if initiator == True:
            dfchunk.to_sql(name='pickup_zones', con=engine, if_exists='replace') 
            initiator=False
        else:
            dfchunk.to_sql(name='pickup_zones', con=engine, if_exists='append') 


if __name__ == '__main__':
    main()


