class movie :
 
    def __init__(self, name, year, director, budget, stars):
        self.name = name
        self.year = year
        self.director = director
        self.budget = budget
        self.stars = stars

    def get_stars(self):
        print('=== 영화 {}의 주연 배우 목록 ======='.format(self.name))
        for star in self.stars:
            print(star)
#--------------------------------------------------------------------------

movies = []

movies.append(movie('Interstellar', 2014, 'Christoper Nolan', '$165,000,000',
                      ['Matthew McConaughey', 'Anne Hathaway', 'Jessica Chastain' ]))
movies.append(movie('Mad Max: Fury Road', 2015, 'George Miller', '$75,000,000',
                      ['Tom Hardy', 'Charlize Theron', 'Nicholas Hoult']))
movies.append(movie('Lagan', 2017, 'James Mangold', '$97,000,000',
                      ['Hugh Jackman', 'Patrick Stewart', 'Dafne Keen']))


for a in movies :
    print('=== 영화 {} 정보 ======='.format(a.name))
    print('영화 이름: ', a.name)
    print('개봉 년도: ', a.year)
    print('감독: ', a.director)
    print('예산: ', a.budget)
    print('주연: ', a.stars)
    print()

      
#---------------------------------------------------------------------------

Movie = movie('Interstellar', 2014, 'Christoper Nolan', '$165,000,000',
                      ['Matthew McConaughey', 'Anne Hathaway', 'Jessica Chastain'])
print(Movie.get_stars())
