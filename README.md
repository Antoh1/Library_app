## Library Application

A flask Application for managing library services and Library users.
Administrator/Librarian is able to add various books to the library
basing on book name, book description and book category. Also admin marks 
the book unavailable if borrowed and vice versa. User is able to
view all the available books in the library, borrow the book, view all the
books he/she has borrowed, return a book to the library. 

#### Running the App

1. Clone the directory: ```git clone https://github.com/klintg/bc-12-Library_app.git```

2. Go to the app directory ```cd to Library_app directory```

3. Ensure to install and activate virtual enviroment for the app:
    * ``` . venv/bin/activate``` if on mac or linux
    * ``` venv\scripts\activate``` if on windows

4. Install requirements to install app dependencies: ```pip install -r requirements.txt```

5. Boot on the server: ```python run.py```

6. Access the app on your browser: ```localhost:5000```

