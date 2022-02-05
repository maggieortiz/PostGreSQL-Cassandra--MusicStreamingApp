# PostGreSQL-Cassandra--MusicStreamingApp
 - This repository has the code fo both making the Sparkify database with POSTGRESQL and Apache Cassandra 
## Sparkifydb
- The sparkifydb database contains lots of information about songs, artists albums and users. The data was originally in multiple .json files divided into song_data and log_data. By parsing this information the Sparkify startup is able to search their songs to find artists and songs by the Song Title, Artist Name, or Song Duration. This helps catalog their information and make it usable.

## PostGreSql 
- The Database Schema we used was a PostGreSQL Star Schema. This allows for simple queries, easy aggregations, and denormalized tables. The ETL pipeline allows for the json files to be easily parsed and inserted into the tables.

## How to Run the Script: 
1. Open test.ipynb & run Cells one at a time. 
2. After Cell 4 you are able to run any queries you would like. All the tables are made and values are inserted.

## Files: 
- sql_queries.py 
- etl_POSTGRESQL.py 
- etl_POSTGRESQL.ipynb 
- data folder - full of the .json data

## Example Queries: 
- Provide example queries and results for song play analysis. https://www.postgresqltutorial.com/postgresql-group-by/
- Select Count(user_id) from users Where level = paid; - this would tell us the amount of users that pay for the services
- Select artist_id count(songplays_id) from songplays group by artist_id - this would give you the number of plays from each artist

# Apache Cassandra 
- Create the same database by running the Songify_Cassandra_ Project.ipynb Juptyner Notebook. 

## Queries: 
- With NOSQL its always good to know the queries before you design the DB 
1. Give me the artist, song title and song's length in the music app history that was heard during sessionId = 338, and itemInSession = 4
2. Give me only the following: name of artist, song (sorted by itemInSession) and user (first and last name) for userid = 10, sessionid = 182
3. Give me every user name (first and last) in my music app history who listened to the song 'All Hands Against His Own'

## Files: 
- Songify_Cassandra_ Project.ipynb
- event_datafile_new.csv
