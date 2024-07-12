import os
from openai import OpenAI
from app.models.book import Book

class RecommendationService:
    client = OpenAI(
        api_key=os.environ.get("OPENAI_API_KEY"),
    )

    @staticmethod
    def get_recommendations_from_llm(prompt):
        response = RecommendationService.client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model="gpt-3.5-turbo",
            max_tokens=150
        )

        recommendations = response.choices[0].message.content
        return recommendations

    @staticmethod
    def get_available_books(recommended_books):
        available_books = []
        unavailable_books = []

        for book_title in recommended_books:
            book = Book.query.filter(Book.title.ilike(f'%{book_title}%')).first()
            if book:
                available_books.append({
                    'id': book.id,
                    'title': book.title,
                    'author': book.author,
                    'published_date': book.published_date,
                    'genre': book.genre.name,
                    'genre_id': book.genre_id
                })
            else:
                unavailable_books.append(book_title)

        return available_books, unavailable_books
