import pandas as pd

books = pd.DataFrame({'book_id': ['b1','b2','b3'],
                      'title': ['Beautiful Coding','Pthon for web Development',
                      'Pythonic Thinking'],
                      'topic': ['programming','web','python']})
authors = pd.DataFrame({'author_id': ['jsn','tri','wsn'],
                        'author': ['Johnson','Treloni','willson']})
matching = pd.DataFrame({'author_id': ['jsn', 'jsn', 'tri', 'wsn'],
                         'book_id': ['b1', 'b2', 'b2', 'b3']})
#print(matching)
authorship = books.merge(matching, on='book_id').merge(authors, on='author_id')[
    ['title', 'topic', 'author']
]
print(authorship)