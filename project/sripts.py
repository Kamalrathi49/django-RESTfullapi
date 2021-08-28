from myapp.models import Post

posts = [{
  "name": "Cricket World Cup: The Indian Challenge",
  "author": "Ashis Ray",
  "rating": -1
}, {
  "name": "	My Journey",
  "author": "Dr. A.P.J. Abdul Kalam",
  "rating": 1
}, {
  "name": "Making of New India",
  "author": "Dr. Bibek Debroy",
  "rating": -1
}, {
  "name": "Whispers of Time",
  "author": "Dr. Krishna Saksena",
  "rating": 1
}, {
  "name": "A Revenue Stamp",
  "author": "Amrita Pritam",
  "rating": 0
}]

for item in posts:
    post = Post.objects.create(
        book_name=item['name'],
        author=item['author'],
        rating=item['rating']
    )
    post.save()