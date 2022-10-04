import random
from assets.controller import * 


def quote_publisher():
    
    cursor.execute('''SELECT count(quote) FROM quotes''')
    record = cursor.fetchall()
    random_row_number =  record[0][0] 
    randomRow = random.randint(1, random_row_number)
    
    cursor.execute(f'''
                    SELECT * FROM (
                        SELECT
                            ROW_NUMBER () OVER ( 
                                ORDER BY quote
                            ) RowNum,
                            quote,
                            source
                        FROM
                            quotes
                    )
                    WHERE 
                        RowNum = {randomRow}
                    ORDER BY quote ASC
                ''')
        
    record = cursor.fetchall()
    sqliteConnection.commit()
    
    quote = record[0][1] 
    # source = record[0][2]
    
    tweet = "“"+quote+"”"+bot_end_message
    
    api.update_status(status=tweet)
    
