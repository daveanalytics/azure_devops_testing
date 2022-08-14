from typing import List

from pyspark.sql import DataFrame


def get_cols(df: DataFrame) -> List[str]:
    return df.columns
