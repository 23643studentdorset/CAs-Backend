from time import timezone
import requests
import json

from CAs.polls.models import Movie


class Movie:
    def __init__(self, title, score):
        self.title = title
        self.score = score

    def __str__(self):
        return "Title:" + self.title + " Score:" + self.score


# req = requests.get('https://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc&api_key'
#                    '=04c35731a5ee918f014970082a0088b1&page=1')
# json_data = json.loads(req.text)
c = 0
movies = []
# total_pages = json_data['total_pages']
# print(total_pages)


for i in range(1, 501):
    req = requests.get(
        'https://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc&api_key=04c35731a5ee918f014970082a0088b1'
        '&page=' + str(i))
    json_data = json.loads(req.text)
    page = json_data['page']
    print(page)
    for element in json_data['results']:
        movie = Movie(element['title'], element['vote_average'])
        print(movie.title)
        movies.append(movie)
counter = 5
for target_movie in movies:
    counter += 1
    q = Movie(question_text=str(target_movie.title), pub_date=timezone.now())
    q.save()
    retrieved_movie = Movie.objects.get(pk=counter)
    for i in range(1, 11):
        retrieved_movie.choice_set.create(choice_text=str(i), votes=0)
