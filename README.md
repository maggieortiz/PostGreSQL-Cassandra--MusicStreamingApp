# PostGreSQL-Cassandra--MusicStreamingApp
 - This repository has the code fo both making the Sparkify database with POSTGRESQL and Apache Cassandra 
 - 
##Sparkifydb
- The sparkifydb database contains lots of information about songs, artists albums and users. The data was originally in multiple .json files divided into song_data and log_data. By parsing this information the Sparkify startup is able to search their songs to find artists and songs by the Song Title, Artist Name, or Song Duration. This helps catalog their information and make it usable.

#PostGreSql 
##The Database Schema we used was a PostGreSQL Star Schema. This allows for simple queries, easy aggregations, and denormalized tables. The ETL pipeline allows for the json files to be easily parsed and inserted into the tables.

#HOW TO RUN THE SCRIPT: 
1. Open test.ipynb & run Cells one at a time. 
2. After Cell 4 you are able to run any queries you would like. All the tables are made and values are inserted.

##Files: 
- test.ipynb 
- create_tables.py 
- etl.py 
- etl.ipynb 
- data folder - full of the .json data

##Example Queries: Provide example queries and results for song play analysis. https://www.postgresqltutorial.com/postgresql-group-by/

###Select Count(user_id) from users Where level = paid; - this would tell us the amount of users that pay for the services

###Select artist_id count(songplays_id) from songplays group by artist_id - this would give you the number of plays from each artist
