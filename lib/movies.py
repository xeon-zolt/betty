import omdb
import gi


def do_activate(self, args, argv):
	movie = omdb.title(' '.join(args).strip())
	print("Name : "+movie.title)
	print("Year of Releasing : "+movie.year)
	print("Movie or Series : "+movie.type)
	print("Genre : "+movie.genre)
	print("Cast : "+movie.actors)
	if (float(movie.imdb_rating) < 5.0):	
		print("I Won't Watch This Because its only "+movie.imdb_rating+" on imdb")
	else:
	print("Ok I will watch it because it got "+movie.imdb_rating+" on imdb")


