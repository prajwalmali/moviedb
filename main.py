# Repo Owner :- https://github.com/prajwalmali/prajwalmali
# ALL-IN-ONE link :- https://linktr.ee/prajwalmali

import sqlite3  # Interfacing database using sqlite library

def db_connection():
    #"Connecting database"
    connect=sqlite3.connect("movie.sqlite",isolation_level=None)
    return connect

db=db_connection()
cursor=db_connection().cursor()

def create_table(db):
    list_table=cursor.execute("""SELECT * FROM sqlite_master WHERE type='table' and name="movie" ; """).fetchall()
    if list_table==[]:
        cursor.execute("""CREATE TABLE IF NOT EXISTS movie(movie VARCHAR(25),actor VARCHAR(30), actress VARCHAR(30), director VARCHAR(25),year VARCHAR(5));""")
        print('Movie table created')
        #cursor.execute("""INSERT INTO movie (movie,actor,actress,director,year) VALUES ('Iron man', 'Robert dowry jr','Gwyneth paltrow','Jon favreav',2008);""")
        db.commit()

    else:
                print('Movie table already exist in the database and connected successfully')

def check_connections():
    if db_connection() is not None:
        print("Database connected successfully")
        create_table(db_connection())
    else:
            print("I can't cannot create the database connection.")


def insert_data(db):
    movie_name=input("Enter Movie name : ")
    actor=input("Enter movie's Actor name: ")
    actress=input("Enter movie's actress name: ")
    director=input("Enter movie's director name: ")
    year=input("Enter movie released year : ")
    cmd=("""INSERT INTO movie (movie,actor,actress,director,year) VALUES (?,?,?,?,?);""")
    val=(movie_name,actor,actress,director,year)
    cursor.execute(cmd,val)
    db.commit()
    print("\nData Inserted successfully...")


def remove_data(db):
    cursor.execute("""DELETE FROM movie;""").fetchall()
    db.commit()
    print("All the data' deleted successfully ...")

movie_=[]
actor_=[]
actress_=[]
director_=[]
year_=[]


def insert_sample_data():
    cursor.execute("""INSERT INTO movie (movie,actor,actress,director,year) VALUES ('Iron man', 'Robert dowry jr','Gwyneth paltrow','Jon favreav','2008'),
                   ('Sherlock Holmes','Robert dowry jr','Rachel MC adams','Guy richie','2009'),
                   ('Captain america','Chris evans','Harley atwel','Joe johnson','2011'),
                   ('Fantastic four', 'Chris evans', 'Jesica alba','Tim story','2005'),
                   ('Thor','Chris Hamsworth','Natalie portman','Kanneth Branagh','2011'),
                   ('Extraction','Chris Hamsworth', 'Golshifteh Farahani', 'Sam hargrave','2020');""")
    db.commit()
    print("Inbuilt data inserted Successfully to database...")
def select_actor():
    hero=str(input("Enter Actor Name : "))
    view=cursor.execute("""SELECT movie FROM movie WHERE actor=(?);""",(hero,)).fetchall()
    db.commit()
    for i in view:
        print(i,end='')
    
def select_actress():
    heroine=str(input("Enter Actress Name : "))
    view=cursor.execute("""SELECT movie FROM movie WHERE actress=(?);""",(heroine,)).fetchall()
    db.commit()
    print(view)

def select_director():
    director_of_the_movie=str(input("Enter movie director name : "))
    view=cursor.execute("""SELECT movie FROM movie WHERE director=(?);""",(director_of_the_movie,)).fetchall()
    db.commit()
    for i in view:
        print(i,end='')
        
def select_year():
    realease_year=str(input("Enter Movie released year : "))
    view=cursor.execute("""SELECT movie FROM movie WHERE year=(?);""",(realease_year,)).fetchall()
    db.commit()
    for i in view:
        print(i,end='')

def view_database():
    movie_=[]
    actor_=[]
    actress_=[]
    director_=[]
    year_=[]

    data=cursor.execute("""SELECT * FROM movie; """).fetchall()
    for row in data:

        #print "ID = ", row[0]
        #print "NAME = ", row[1]
        #print "ADDRESS = ", row[2]
        #print "SALARY = ", row[3], "\n"

        movie_.append(row[0])
        actor_.append(row[1])
        actress_.append(row[2])
        director_.append(row[3])
        year_.append(row[4])
        
    print("Movie = ", movie_ )
    print("Actor = ", actor_)
    print("Actress  = ",actress_)
    print("Director  = ", director_)
    print("Year  = ", year_, "\n")




while(1):
    print(" ____________________________________")
    print("|                             OPTIONS                               |")
    print("|    1. Check Movie database connection     |")
    print("|    2. Insert data into the movie table          |")
    print("|    3. Delete data into the movie table         |")
    print("|    4. Insert sample movie data                      |")
    print("|    5. View data in the movie table                |")
    print("|    6. Select movie by actor                             |")
    print("|    7. Select movie by actress                          |")
    print("|    8. Select movie by Director                        |")
    print("|    9. Select movie by Year                               |")
    print("|                   Enter ('Q') to quit                          |")
    print("|___________________________________|")
    selection=input("\nSelect a option : ")
    print('-----------------------------------------------------------')
    if selection=='1':
        check_connections()
        print('-----------------------------------------------------------')
    elif selection=='2':
        db
        insert_data(db)
        db.commit()
        print('-----------------------------------------------------------')
    elif selection=='3':
        db
        remove_data(db)
        db.commit()
        print('-----------------------------------------------------------')
    elif selection=='4':
        db
        insert_sample_data()
        db.commit()
        print('-----------------------------------------------------------')
    elif selection=='5':
        view_database()
        print('-----------------------------------------------------------')
    elif selection=='6':
        db
        select_actor()
        print('-----------------------------------------------------------')
    elif selection=='7':
        db
        select_actress()
        print('-----------------------------------------------------------')
    elif selection=='8':
        db
        select_director()
        print('-----------------------------------------------------------')
    elif selection=='9':
        db
        select_year()
        print('-----------------------------------------------------------')
    elif selection=='Q' or selection=='q' :
        print('Script Ended...')
        quit()

    else:
        print("Enter valid option..!")







    
