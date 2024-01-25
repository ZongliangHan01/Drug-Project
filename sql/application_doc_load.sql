LOAD DATA LOCAL INFILE '/Users/zonglianghan/Desktop/datfda20240102 2/ApplicationDocs.txt' 
INTO TABLE application_docs 
CHARACTER SET latin1 
FIELDS TERMINATED BY '\t' 
LINES TERMINATED BY '\n' 
IGNORE 1 LINES;  -- Assuming the first line is a header; adjust if needed
