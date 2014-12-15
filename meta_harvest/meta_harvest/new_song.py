#coding=utf-8
import random
import csv
import MySQLdb
import sys
from mydb import Tiedb
from mydb import Meta
import re


mydb = Tiedb()
meta = Meta()
    # for row in mydb.get_random_rows(100, "%gmail.com"):
        # print row
    # sys.exit(0)
    #print mydb.get_song_info("青花瓷","周杰伦")[0],mydb.get_song_info("青花瓷","周杰伦")[1],mydb.get_song_info("青花瓷","周杰伦")[2]
csvfile = file('meta_new_song.csv', 'rb')
reader = csv.reader(csvfile)
index=0
index_error=0
index_full=0
for lrow in list(reader):
    index=index+1
    print '处理前:',lrow[0].decode('gbk'),index
    song_raw=lrow[0].decode('gbk').encode('UTF-8')
    song=re.sub('\(.*?\)|\[.*?]|{.*?}|（.*?）','',song_raw)#去括号
    artist_raw=lrow[1].decode('gbk').encode('UTF-8')
    artist=re.sub('\(.*?\)|\[.*?]|{.*?}|（.*?）','',artist_raw)#去括号
    try:        
        #print '处理后：',song,artist
        #song_info=mydb.get_artist_xiami(song)
        #artist=song_info[0]
        #print '处理后：',song,artist  
        song_info=mydb.get_song_info_163music(song,artist)
        album_id=song_info[0]
        album=song_info[1]
        musicUrl=song_info[2]
        lyricid=song_info[3]

        meta.update_songinfo(song,artist,album_id,album,musicUrl,lyricid)
        index_full=index_full+1
        print index_full

    except Exception, e:
        index_error=index_error+1
        print e,index_error
        

