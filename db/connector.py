import pandas as pd
from clickhouse_connect import get_client


from .configs import Config
from .structure import *


class Connector:
    def __init__(self, config: Config):
        self.config = config
        self.client = get_client(
            host=self.config.host,
            port=self.config.port,
            user=self.config.username,
            password=self.config.password
        )
        self.db = None
        self.structure = Structure()
        databases = self.databases()
        self.structure.databases = [Database(name=db) for db in databases['name'].to_list()]

    def close(self):
        self.client.disconnect()

    def query(self, query: str):
        results = self.client.query(query)
        return  pd.DataFrame(results.result_rows, columns=results.column_names)

    def set_db(self, database: str):
        _ = self.query(f'USE {database};')
        self.db = database


    def databases(self) -> pd.DataFrame:
        return self.query('SHOW DATABASES;')
    
    def tables(self, database: str) -> pd.DataFrame:
        return self.query(f'SHOW TABLES FROM {database};')

    def describe(self, table: str, database: str=None) -> pd.DataFrame:
        if database is None and self.db is None:
            raise ValueError("Database not set.")
        if database is None:
            database = self.db
        return self.query(f'DESCRIBE TABLE {database}.{table};')
    
    def build_structure(self):
        for db in self.structure.databases:
            tables = self.tables(db.name)
            db.tables = [Table(name=table, columns=[]) for table in tables['name'].to_list()]
            for table in db.tables:
                details = self.describe(table.name, db.name)
                for _, row in details.iterrows():
                    column = Column(
                        name=row['name'],
                        type=row['type'],
                        default_type=row['default_type'],
                        default_expression=row['default_expression'],
                        comment=row['comment'],
                        codec_expression=row['codec_expression'],
                        ttl_expression=row['ttl_expression']
                    )
                    table.columns.append(column)
    