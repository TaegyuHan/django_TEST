SELECT COLUMN_NAME 
FROM INFORMATION_SCHEMA.COLUMNS 
WHERE 
    TABLE_SCHEMA = Database()
AND TABLE_NAME = 'sale_details' ;

