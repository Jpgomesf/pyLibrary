import os
import json
from openai import OpenAI
from app.models.book import Book

class RecommendationService:
    client = OpenAI(
        api_key=os.environ.get("OPENAI_API_KEY"),
    )

    @staticmethod
    def get_recommendations_from_llm(prompt: str):
        response = RecommendationService.client.chat.completions.create(
            model="gpt-3.5-turbo",
            response_format={ "type": "json_object" },
            messages=[
                {"role": "system", "content": "You are a helpful librarian designed to output JSON. You should recommend a maximum of 3 books."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=350
        )

        print(response.choices[0].message.content)
        content = response.choices[0].message.content
        if content is None:
            raise ValueError("Received None content which cannot be processed.")
        recommendations = json.loads(content)
        return recommendations

    @staticmethod
    def get_available_books(recommended_books):
        print(f"Type of recommended_books: {type(recommended_books)}")
        if isinstance(recommended_books, list) and recommended_books:
            print(f"Type of first element: {type(recommended_books[0])}")
            print(f"First element: {recommended_books[0]}")
        else:
            print("recommended_books is not a list or is empty")

        book_titles = [book['title'] for book in recommended_books]

        found_books = Book.query.filter(Book.title.in_(book_titles)).all()

        found_books_dict = {book.title: book for book in found_books}

        available_books = []
        for book in recommended_books:
            title = book['title']
            if title in found_books_dict:
                db_book = found_books_dict[title]
                available_books.append({
                    'id': db_book.id,
                    'title': db_book.title,
                    'author': db_book.author,
                    'published_date': db_book.published_date,
                    'genre': db_book.genre.name,
                    'genre_id': db_book.genre_id,
                    'description': book.get('summary', ''),
                    'rating': book.get('rating', '')
                })

        unavailable_books = [book for book in recommended_books if book['title'] not in found_books_dict]

        return available_books, unavailable_books
