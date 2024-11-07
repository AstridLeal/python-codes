books={
    "Life of Pi": "Adventure Fiction",
    "The Three Musketeers": "Historical Adventure",
    "Watchmen": "Comics",
    "Bird Box": "Horror",
    "Harry Potter": "Fantasy Fiction",
    "Good Omens": "Comedy"
}

book=input()

if book in books:
    print(books[book])
else:
    print("Not found")