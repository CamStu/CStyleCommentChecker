# CStyleCommentChecker
A python script counts the total lines of all the files in the directory (excluding the script)
as well as the total lines commented, and returns a percentage of lines commented for each file
and for the entire directory.

The script is specifically looking for C style comments (//,/*, etc.).

Known Bugs:
1.String literals with C style comments in them like "This is a string//" or "/*Another string"

