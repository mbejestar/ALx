book = Book.objects.get(title="1984") book.title = "Nineteen Eighty-Four" book.save()

OUTPUT # Verify with Book.objects.get(id=1).title -> "Nineteen Eighty-Four"
