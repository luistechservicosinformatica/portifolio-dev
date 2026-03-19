# Blog API

A modern blog system built with Flask, featuring both a web interface and a REST API.

---

## Features

### Web Interface
- Create posts
- Edit posts
- Delete posts
- Simple and clean UI
- Animated posts

---

### REST API
- List all posts
- Create post
- Update post
- Delete post
- JSON response

---

## Technologies

- Python
- Flask
- Flask SQLAlchemy
- SQLite
- HTML, CSS, JavaScript

---

## How to Run

```bash
git clone https://github.com/luistechservicosinformatica/portifolio-dev/backend/python/flask-blog-api.git
cd flask-blog-api
pip install -r requirements.txt
python run.py
```
								
Access
	```http://127.0.0.1:500```

									---
## API Endpoints
# Get all posts
```GET /api/posts```

Waited response:
```json
[
  {
    "id": 1,
    "title": "First Post",
    "content": "Hello world",
    "author": "Luis"
  }
]
```

# Create post
```POST /api/post```

Body:

```json
{
	"title": "My Post",
  	"content": "This is my content",
  	"author": "Luis"
}
```

Waited response:
```json
{
	"success":true
}
```

# Update post
```PUT /api/post/<id>```

Body:

```json
{
	"title": "Updated Title",
  	"content": "Updated content",
  	"author": "Luis"
}
```

Waited response:
```json
{
	"success":true
}
```


# Delete post
```Delete /api/post/<id>```

Waited response:
```json
{
	"success":true
}
```

---

## Project Structure
```bash
flask-blog-api
│
├── app
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   └── config.py
│
├── templates
    ├── index.html
    ├── edit.html
├── static
    ├── css
        ├── styles.css
    ├── js
        ├── main.js
├── requirements.txt
├── README.md
└── run.py
```

---

## Future Improvements
- Authentication (login/register)
- JWT security
- Password hashing
- Rate limiting
- Better frontend UI
- Pagination

---

## License
This project is free for use for all. I just made for educational purposes.

---

## Author
Luís Fernando Reis
Computer Science Student
Cybersecurity & Backend Development