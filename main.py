from sqlalchemy import create_engine, MetaData, VARCHAR, Integer, Table, Column, ForeignKey, UniqueConstraint, select
from sqlalchemy.dialects.postgresql import insert
import random

#  Create the postgresql database engine of the database "x_bookkeeping".
engine = create_engine('postgresql://postgres:YOUR_PASSWORD@localhost/x_bookkeeping')
metadata = MetaData()
# metadata.reflect(engine)
# metadata.drop_all(engine)
# metadata.clear()

# Create books table
books = Table("books", metadata,
              Column('id', Integer, unique=True, primary_key=True, autoincrement=True, nullable=False),
              Column('title', VARCHAR(150), nullable=False),
              Column('number_of_pages', Integer, nullable=False),
              UniqueConstraint('title', 'number_of_pages')
              )
# Create authors table
authors = Table("authors", metadata,
                Column('id', Integer, unique=True, primary_key=True, autoincrement=True, nullable=False),
                Column('first_name', VARCHAR(50), nullable=False),
                Column('last_name', VARCHAR(50), nullable=False),
                UniqueConstraint('first_name', 'last_name')
                )
# Create author_books table
author_books = Table("author_books", metadata,
                     Column('id', Integer, unique=True, primary_key=True, autoincrement=True, nullable=False),
                     Column('author_id', Integer, ForeignKey('authors.id', ondelete='CASCADE'), nullable=False),
                     Column('book_id', Integer, ForeignKey('books.id', ondelete='CASCADE'), unique=True, nullable=False),
                     UniqueConstraint('author_id', 'book_id'),
                     )
# Effects the CREATE operations above.
metadata.create_all(engine)

data = [{'book_id': 1, 'title': 'The Mystery', 'number_of_pages': 300, 'author_id': 1, 'first_name': 'John',
         'last_name': 'Doe'},
        {'book_id': 2, 'title': 'Journey to the Stars', 'number_of_pages': 250, 'author_id': 2, 'first_name': 'Jane',
         'last_name': 'Smith'},
        {'book_id': 3, 'title': 'Beyond the Horizon', 'number_of_pages': 400, 'author_id': 3, 'first_name': 'Michael',
         'last_name': 'Johnson'},
        {'book_id': 4, 'title': 'Secrets Unveiled', 'number_of_pages': 320, 'author_id': 4, 'first_name': 'Sarah',
         'last_name': 'Williams'},
        {'book_id': 5, 'title': 'Echoes of Time', 'number_of_pages': 280, 'author_id': 5, 'first_name': 'Robert',
         'last_name': 'Davis'},
        {'book_id': 6, 'title': 'Whispers in the Wind', 'number_of_pages': 200, 'author_id': 6, 'first_name': 'Emily',
         'last_name': 'Taylor'},
        {'book_id': 7, 'title': 'The Silent Observer', 'number_of_pages': 350, 'author_id': 7,
         'first_name': 'Christopher', 'last_name': 'Brown'},
        {'book_id': 8, 'title': 'Enchanted Gardens', 'number_of_pages': 180, 'author_id': 8, 'first_name': 'Olivia',
         'last_name': 'Anderson'},
        {'book_id': 9, 'title': 'Shattered Dreams', 'number_of_pages': 300, 'author_id': 9, 'first_name': 'Daniel',
         'last_name': 'Wilson'},
        {'book_id': 10, 'title': 'Lost in Translation', 'number_of_pages': 240, 'author_id': 10,
         'first_name': 'Sophia', 'last_name': 'Miller'},
        {'book_id': 11, 'title': 'Midnight Serenade', 'number_of_pages': 280, 'author_id': 1, 'first_name': 'John',
         'last_name': 'Doe'},
        {'book_id': 12, 'title': 'Captivating Moments', 'number_of_pages': 320, 'author_id': 2, 'first_name': 'Jane',
         'last_name': 'Smith'},
        {'book_id': 13, 'title': 'Shadows of the Past', 'number_of_pages': 400, 'author_id': 3,
         'first_name': 'Michael', 'last_name': 'Johnson'},
        {'book_id': 14, 'title': 'The Forgotten Realm', 'number_of_pages': 260, 'author_id': 4, 'first_name': 'Sarah',
         'last_name': 'Williams'},
        {'book_id': 15, 'title': 'Symphony of Shadows', 'number_of_pages': 300, 'author_id': 5, 'first_name': 'Robert',
         'last_name': 'Davis'},
        {'book_id': 16, 'title': "A Garden's Tale", 'number_of_pages': 220, 'author_id': 6, 'first_name': 'Emily',
         'last_name': 'Taylor'},
        {'book_id': 17, 'title': 'The Art of Silence', 'number_of_pages': 380, 'author_id': 7,
         'first_name': 'Christopher', 'last_name': 'Brown'},
        {'book_id': 18, 'title': 'Colors of the Sky', 'number_of_pages': 200, 'author_id': 8, 'first_name': 'Olivia',
         'last_name': 'Anderson'},
        {'book_id': 19, 'title': 'Broken Reflections', 'number_of_pages': 320, 'author_id': 9, 'first_name': 'Daniel',
         'last_name': 'Wilson'},
        {'book_id': 20, 'title': 'Echoes of Eternity', 'number_of_pages': 240, 'author_id': 10, 'first_name': 'Sophia',
         'last_name': 'Miller'},
        {'book_id': 21, 'title': 'The Hidden Truth', 'number_of_pages': 300, 'author_id': 1, 'first_name': 'John',
         'last_name': 'Doe'},
        {'book_id': 22, 'title': 'Serendipity', 'number_of_pages': 250, 'author_id': 2, 'first_name': 'Jane',
         'last_name': 'Smith'},
        {'book_id': 23, 'title': "The Alchemist's Legacy", 'number_of_pages': 400, 'author_id': 3,
         'first_name': 'Michael', 'last_name': 'Johnson'},
        {'book_id': 24, 'title': 'Veil of Illusions', 'number_of_pages': 320, 'author_id': 4, 'first_name': 'Sarah',
         'last_name': 'Williams'},
        {'book_id': 25, 'title': 'Eternal Odyssey', 'number_of_pages': 280, 'author_id': 5, 'first_name': 'Robert',
         'last_name': 'Davis'},
        {'book_id': 26, 'title': 'Echoes of Eternity', 'number_of_pages': 240, 'author_id': 10, 'first_name': 'Sophia',
         'last_name': 'Miller'},
        {'book_id': 27, 'title': 'The Hidden Truth', 'number_of_pages': 300, 'author_id': 1, 'first_name': 'Michael',
         'last_name': 'Johnson'},
        {'book_id': 28, 'title': 'Serendipity', 'number_of_pages': 250, 'author_id': 2, 'first_name': 'Jane',
         'last_name': 'Smith'},
        {'book_id': 29, 'title': "The Alchemist's Legacy", 'number_of_pages': 400, 'author_id': 3,
         'first_name': 'Michael', 'last_name': 'Johnson'},
        {'book_id': 30, 'title': 'Veil of Illusions', 'number_of_pages': 320, 'author_id': 4, 'first_name': 'Jane',
         'last_name': 'Smith'},
        {'book_id': 31, 'title': 'Eternal Odyssey', 'number_of_pages': 280, 'author_id': 5, 'first_name': 'Robert',
         'last_name': 'Davis'}]

random.shuffle(data)  # Used just to obtain/test different datasets case scenarios

books_insert_stmt = insert(books).values(
    [{'id': entry['book_id'], 'title': entry['title'], 'number_of_pages': entry['number_of_pages']} for entry in
     data]).on_conflict_do_nothing()
authors_insert_stmt = insert(authors).values(
    [{'id': entry['author_id'], 'first_name': entry['first_name'], 'last_name': entry['last_name']} for entry in
     data]).on_conflict_do_nothing()

#  Connect to the database and perform the INSERT (data) operations executing rollback if any constraint
#  exception is encountered.
with engine.connect() as conn:
    with conn.begin():
        conn.execute(books_insert_stmt)
        conn.execute(authors_insert_stmt)
    for entry in data:
        try:
            conn.execute(insert(author_books).values([
                {'author_id': select(authors.c.id).where((authors.c.first_name == entry['first_name']) & (
                        authors.c.last_name == entry['last_name'])), 'book_id': select(books.c.id).where(
                    (books.c.title == entry['title']) & (books.c.number_of_pages == entry['number_of_pages']))}]))
        except Exception as e:
            print(e)
            conn.rollback()
            # max_id = conn.execute(select(author_books.c.id).order_by(author_books.c.id.desc()).limit(1)).scalar()
            # conn.execute(sqlalchemy.text(f'ALTER SEQUENCE author_books_id_seq RESTART WITH {max_id+1}'))
        else:
            conn.commit()

    # Query the database and select all records in the authors table, then order by ID.
    authors_table_data = [row for row in conn.execute(select(authors).order_by(authors.c.id))]
    print(len(authors_table_data), '\n', authors_table_data)

    # Query the database and select all records in the books table, then order by ID.
    books_table_data = [row for row in conn.execute(select(books).order_by(books.c.id))]
    print(len(books_table_data), '\n', books_table_data)

    # Query the database and select all records in the author_books table, then order by author_books ID.
    author_books_table_data = [row for row in conn.execute(select(author_books).order_by(author_books.c.id))]
    print(len(author_books_table_data), '\n', author_books_table_data)
