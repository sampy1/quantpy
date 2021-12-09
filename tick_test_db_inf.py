""" tick_test_db.py

    Start of a database that will interface with stock ticker tests.
    In theory this db will be generated and interfaced to store collected database
    from different sources in a clean method.

"""

__author__ = "Samuel Stephens"
__copyright__ = "Copyright 2021, TwoBarSlash LLC"
__credits__ = [""]
__license__ = "All Rights Reserved."
__version__ = "0.1"
__maintainer__ = "Samuel Stephens"
__email__ = "sam@twobarslash.com"
__status__ = "Developement"

import sqlite3


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
        :param db_file: database file
        :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn

def main(db_file):
    # ==============================================================================
    # Building the Database Tables.
    # ==============================================================================
    connection = create_connection(db_file) # :memory:
    cursor = connection.cursor()

    company_table =""" CREATE TABLE IF NOT EXISTS
        company_table(
            company_id INTERGER PRIMARY KEY,
            ticker TEXT,
            company_name TEXT,
            company_address TEXT,
            company_description TEXT
        )
                   """
    cursor.execute(company_table)

    ticker_table =  """CREATE TABLE IF NOT EXISTS
        ticker_table (
            timestamp DATETIME NOT NULL DEFAULT (datetime(CURRENT_TIMESTAMP,'utc')) 
                PRIMARY KEY,
            company_id INTEGER,
            price      DECIMAL(17, 8), /* See Ref[2,3,4] */
            FOREIGN KEY(company_id) References company_table(company_id)
        )

                    """
    cursor.execute(ticker_table)

    # new calculated parameters should be added to the following table. 
    calc_table =  """CREATE TABLE IF NOT EXISTS
        calc_table (
            timestamp DATETIME NOT NULL DEFAULT (datetime(CURRENT_TIMESTAMP, 'utc'))
                PRIMARY KEY, /* Time inserted into database *See Ref[8]*/
            company_id INTEGER,
            pe_ratio DECIMAL(17, 8), /* See Ref[2,3,4] */
            FOREIGN KEY(company_id) References company_table(company_id)
        )

                    """
    cursor.execute(calc_table)



if __name__ == '__main__':
    db_file = "ticker.db"
    main(db_file)

"""
References
1. https://www.sqlite.org/datatype3.html
2. https://dzone.com/articles/how-should-i-store-currency-values-in-sql-server
   Not sure this is suffient for Bitcoin type rounding accuracy.
3. https://stackoverflow.com/questions/47889200/how-to-store-bitcoin-and-other-currencies-in-mysql-database
4. https://bitcoin.stackexchange.com/questions/31933/why-is-bitcoin-defined-as-having-8-decimal-places
5. https://sqlitebrowser.org/dl/
6. https://www.programiz.com/python-programming/datetime/timestamp-datetime
7. https://stackoverflow.com/questions/14461851/how-to-have-an-automatic-timestamp-in-sqlite
8. https://sqlite.org/lang_datefunc.html
"""