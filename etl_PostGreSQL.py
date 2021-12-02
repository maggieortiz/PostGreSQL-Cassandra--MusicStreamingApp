import os
import glob
import psycopg2
import pandas as pd
from sql_queries import *


def process_song_file(cur, filepath):
    """
  Description: This function can be used to read the file in the filepath (data/song_data)
  to get the song and artist info and used to populate the songs and artists fact tables.

  Arguments:
      cur: the cursor object. 
      filepath: log data file path. 

  Returns:
      None
    """
    # open song file
    df = pd.read_json(filepath, lines=True, orient='columns')

    # insert song record
    song_data = (df.values[0][7], df.values[0][8], df.values[0][0], df.values[0][9], df.values[0][5])
    cur.execute(song_table_insert, song_data)
    
    # insert artist record
    artist_data = artist_data = (df.values[0][0], df.values[0][4], df.values[0][2], df.values[0][1], df.values[0][3])
    cur.execute(artist_table_insert, artist_data)


def process_log_file(cur, filepath):
    """
  Description: This function can be used to read the file in the filepath (data/log_data)
  to get the user and time info and used to populate the users and time dim tables.

  Arguments:
      cur: the cursor object. 
      filepath: log data file path. 

  Returns:
      None
    """
    # open log file
    df = pd.read_json(filepath, lines=True, orient='columns')

    # filter by NextSong action
    df = df[df['page']=='NextSong']

    # convert timestamp column to datetime
    t =  pd.to_datetime(df['ts'], unit='ms')
    
    # insert time data records
    time_data =  list(zip(t.dt.strftime('%Y-%m-%d %I:%M:%S'), t.dt.hour, t.dt.day,t.dt.week, t.dt.month,t.dt.year, t.dt.weekday))
    column_labels =  ['start_time', 'hour', 'day', 'week', 'month', 'year', 'weekday']
    time_df = pd.DataFrame(time_data, columns = column_labels).astype(str)

    for i, row in time_df.iterrows():
        cur.execute(time_table_insert, list(row))

    # load user table
    user_df =  df[["userId", "firstName", "lastName", "gender", "level"]]

    # insert user records
    for i, row in user_df.iterrows():
        cur.execute(user_table_insert, row)

    # insert songplay records
    for index, row in df.iterrows():
        
        # get songid and artistid from song and artist tables
        cur.execute(song_select, (row.song, row.artist, row.length))
        results = cur.fetchone()
        
        if results:
            songid, artistid = results
        else:
            songid, artistid = None, None

        # insert songplay record
        # songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent
        
        # cant use index because of out of bounds error. So remake start_time from ts variable 
        start_time = pd.to_datetime(row.ts, unit='ms').strftime('%Y-%m-%d %I:%M:%S')
        songplay_data = (start_time,row.userId, row.level, songid, artistid, row.sessionId, row.location, row.userAgent)
        cur.execute(songplay_table_insert, songplay_data)


def process_data(cur, conn, filepath, func):
    # get all files matching extension from directory
    """
  Description: This function iterates over all the files to process the song_data and log_data

  Arguments:
      cur: the cursor object. 
      filepath: log data file path. 
      conn: connection object.
      func: process_song_file or process_log_file

  Returns:
      prints statment of file processed iteration
    """
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root,'*.json'))
        for f in files :
            all_files.append(os.path.abspath(f))

    # get total number of files found
    num_files = len(all_files)
    print('{} files found in {}'.format(num_files, filepath))

    # iterate over files and process
    for i, datafile in enumerate(all_files, 1):
        func(cur, datafile)
        conn.commit()
        print('{}/{} files processed.'.format(i, num_files))


def main():
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
    cur = conn.cursor()

    process_data(cur, conn, filepath='data/song_data', func=process_song_file)
    process_data(cur, conn, filepath='data/log_data', func=process_log_file)

    conn.close()


if __name__ == "__main__":
    main()