-- Prints the full description of `first_table`
-- Without using DESCRIBE or EXPLAIN
SELECT COLUMN_NAME, COLUMN_TYPE, IS_NULLABLE, COLUMN_KEY,
COLUMN_DEFAULT, EXTRA FROM information_schema.columns
WHERE table_schema = 'hbtn_0c_0'
and table_name = 'first_table';
