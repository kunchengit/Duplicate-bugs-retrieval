# This is the most original file to extract features from bugs. Not used in the final system.

import MySQLdb
import numpy
import pandas
from nltk.corpus import stopwords
from bs4 import BeautifulSoup
#LCAL_DATABASE_HOST = "10.117.8.41"
#LOCAL_DATABASE_PORT = 3306
#LOCAL_DATABASE_USER = "root"
#LOCAL_DATABASE_PW = "vmware"
#LOCAL_DATABASE_DATABASE = "bugdata"
conn = MySQLdb.connect(host='10.117.8.41', port=3306, user='root', passwd='vmware', db='bugdata')
cur =conn.cursor()
sql = '''select * from longdescs where bug_id=7'''
df = pandas.io.sql.read_sql(sql, conn)

def discription_to_words( raw_description ):
    # Function to convert a raw bug discription to a string of words
    # 1. Remove markers
    discription_text = BeautifulSoup(raw_description).get_text() 
    #
    # 2. Remove non-letters        
    #letters_only = re.sub("[^a-zA-Z]", " ", review_text) 
    #
    # 3. Convert to lower case, split into individual words
    words = discription_text.lower().split()                             
    #
    # 4. In Python, searching a set is much faster than searching
    #   a list, so convert the stop words to a set
    stops = set(stopwords.words("english"))                  
    # 
    # 5. Remove stop words
    meaningful_words = [w for w in words if not w in stops]   
    #
    # 6. Join the words back into one string separated by space, 
    # and return the result.
    return( " ".join( meaningful_words ))

for i in range(df.size):
    #words = discription_to_words(df.ix[i,'thetext'])
    #print words
    print df.ix[i,'thetext']

