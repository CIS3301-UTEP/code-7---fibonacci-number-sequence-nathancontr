filename = 'my_first_file.txt'

file = open(filename,mode='a')

movies = ['scream', 'it', 'the nun', 'annabelle', 'jason']

for movie in movies:
    file.write(movie)
    file.write('\n')