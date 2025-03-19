# Problem: Movie Collection Management

# 1. Create a list called movies with the following movie titles: "Inception", "The Matrix", "Interstellar", "The Godfather", "Toy Story".

# 2. Print the entire list of movies.

# 3. Calculate and print the total number of movies in the collection.

# 4. Check if "Avatar" is in the collection and print the result.

# 5. Add "Avatar" and "Titanic" to the collection.

# 6. Remove the third movie from the collection.

# 7. Sort the list of movies in alphabetical order and print the sorted list.

movies = ["Inception", "The Matrix", "Interstellar", "The Godfather", "Toy Story"]
print("Movies:", movies)

print("Number of movies:", len(movies))

if "Avatar" in movies:
    print("I do have the movie Avatar")
else:
    print("I do not have Avatar")

movies.append("Avatar")
movies.append("Titanic")

del movies[2]

movies.sort()
print("Movies in alphabetical order:", movies)
