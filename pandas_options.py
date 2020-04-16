import pandas as pd

pd.set_option('display.max_columns', 15)
pd.set_option('display.max_rows', 50)
pd.set_option('display.width', 500)
pd.set_option('display.precision', 3)
pd.set_option('display.colheader_justify', 'center')

# use to limit pd.info() because null checks on large
# datasets can be slow.

# pd.set_option('max_info_columns', 5)
# pd.set_option('max_info_rows', 1000)

