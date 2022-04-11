"""
The goal of my project is to create a list of recommendations for different
types of media that the user can read or watch depending on their preferences.
The user will be asked a series of questions that will help customize the list.
This project will use the Books API (specifically the NY Times bestseller list
for "hardcover-fiction"), the Movie Reviews API (reviews that are critics'
picks), and the Most Popular API (most viewed articles in the last 30 days) to
retrieve the data. After the data is retrieved, the code will pick out specific
objects from the data to use. Depending on what the user wants on their list of
recommendations, the code will iterate through all of these objects and
randomly choose different movies, books, or articles based on the number of
recommendations the user wants on their list. The final list containing details
of each recommendation will be displayed in the terminal as a table.
"""

import requests
import random
import textwrap
import time
from tabulate import tabulate
from alive_progress import alive_bar
head = {"USER-AGENT": "ESTHER PARK'S MEDIA RECOMMENDATION PROJECT V.1"}


apikey = "Cs89y7YzP8ln3KNNkkbYcQdW6lZ5fzfF"
book_url = f"https://api.nytimes.com/svc/books/v3/lists/current/hardcover-fiction.json?api-key={apikey}"
movie_url = f"https://api.nytimes.com/svc/movies/v2/reviews/picks.json?api-key={apikey}"
article_url = f"https://api.nytimes.com/svc/mostpopular/v2/viewed/30.json?api-key={apikey}"


def extract(url):
    """Extracts data in the json format from the NY Times API using one of the
    3 urls listed above. The url used depends on what function is called. For
    example, when calling book_function, book_url is used"""
    rawdata = requests.get(url, headers=head).json()
    return rawdata["results"]


def display(final_data, table_header):
    """Displays the transformed data into a neat table-like list using
    tabulate. The header will be the title of the list and will depend on
    which function is called."""
    # each item in this list will have its own "cell" in the final table
    final_list = []
    for final_index in final_data:
        # each item at each index of final_data will be its own list and
        # added to boxed_list
        final_list.append([f"{final_index}"])
    # tabulate() turns a list into a nice table
    print(
        tabulate(final_list, headers=[table_header], tablefmt="fancy_grid"))


def book_function(data_from_book_url, num_of_books):
    """Retrieves the title, author, description, and the amazon link of
    each book listed in the data; puts all of these into book_list; the
    items in this list will be randomized and generates a list based on
    num_of_books (the user input)"""
    data_index = 0
    book_list = []
    for item in data_from_book_url["books"]:
        title = data_from_book_url["books"][data_index]["title"]
        author = data_from_book_url["books"][data_index]["author"]
        desc = data_from_book_url["books"][data_index]["description"]
        amazon_link = (
            data_from_book_url["books"][data_index]["amazon_product_url"])
        # the next 4 lines use textwrap.fill() to wrap the text
        # (so the words will be inside the table)
        wrapped_title = textwrap.fill(title, width=60)
        wrapped_author = textwrap.fill(author, width=60)
        wrapped_desc = textwrap.fill(desc, width=60)
        wrapped_link = textwrap.fill(amazon_link, width=50)
        # each book and its details will be stored in this variable, which
        # gets added to book_list
        book_info = (
            f"{wrapped_title} by {wrapped_author}\n\n{wrapped_desc}"
            f"\n\nBuy the book here:\n{wrapped_link}")
        book_list.append(book_info)
        data_index += 1
    # random.sample() generates a new list of books from book_list;
    # the number of books is determined by num_of_books; the same book
    # is never repeated in this new list and every list item is unique
    randomized_book_list = random.sample(book_list, num_of_books)
    return(randomized_book_list)


def article_function(data_from_articles_url, num_of_articles):
    """Retrieves the title, abstract, and link of each article listed in
    the data; puts all of these into article_list; the items in this list
    will be randomized and generates a list based on num_of_articles (the
    user input)"""
    data_index = 0
    article_list = []
    for item in data_from_articles_url:
        title = data_from_articles_url[data_index]["title"]
        abstract = data_from_articles_url[data_index]["abstract"]
        article_link = data_from_articles_url[data_index]["url"]
        # the next 3 lines use textwrap.fill() to wrap the text
        wrapped_title = textwrap.fill(title, width=60)
        wrapped_abstract = textwrap.fill(abstract, width=60)
        wrapped_link = textwrap.fill(article_link, width=40)
        # each article and its details will be stored in this variable,
        # which gets added to article_list
        article_info = (
            f"{wrapped_title}\n\n{wrapped_abstract}\n"
            f"\nRead more:\n{wrapped_link}\n")
        article_list.append(article_info)
        data_index += 1
    # random.sample() generates a new list of articles from
    # article_list and # of articles is determined by num_of_articles
    randomized_article_list = (
        random.sample(article_list, num_of_articles))
    return(randomized_article_list)


def movie_function(data_from_movies_url, num_of_movies):
    """Retrieves the title, abstract, and link of each movie listed in
    the data; puts all of these into movie_list; the items in this list
    will be randomized and generates a list based on num_of_movies (the
    user input)"""
    data_index = 0
    movie_list = []
    for item in data_from_movies_url:
        title = data_from_movies_url[data_index]["display_title"]
        desc = data_from_movies_url[data_index]["summary_short"]
        rating = data_from_movies_url[data_index]["mpaa_rating"]
        # if there is a blank for the rating, just print out None
        if rating == "":
            rating = "None"
        review_link = data_from_movies_url[data_index]["link"]["url"]
        # the next 3 lines use textwrap.fill() to wrap the text
        wrapped_title = textwrap.fill(title, width=60)
        wrapped_desc = textwrap.fill(desc, width=60)
        wrapped_link = textwrap.fill(review_link, width=50)
        # each movie and its details will be stored in this variable,
        # which gets added to movie_list
        movie_info = (
            f"{wrapped_title}\n\n{wrapped_desc}\n\nMovie rating: {rating}"
            f"\n\nRead the movie review:\n{wrapped_link}\n")
        movie_list.append(movie_info)
        data_index += 1
    # random.sample() generates a new list of movies from
    # movie_list and # of movies is determined by num_of_movies
    randomized_movie_list = random.sample(movie_list, num_of_movies)
    return(randomized_movie_list)


# "interactive" portion of the code - asks the user a series of questions
# to see what kind of list should be created
def progress_bar(user_input_num):
    """Creates a live progress bar using the alive_progress library; will
    be used to show the user the progess of generating the list"""
    # user_input_num here is the total that gets shown in the progress bar
    # ex: if the user inputs 5, the bar will show ??/5 until it reaches 5/5
    with alive_bar(user_input_num) as bar:
        for index in range(user_input_num):
            # time.sleep() delays the time of the loading bar
            time.sleep(1)
            # bar() makes the loading bar move forward
            bar()


# delaying the time it takes to print the message below
time.sleep(1)
print("\nHello there! Are you looking for something to do?\n"
        "If you are, then you've come to the right place!\n"
        "I'll give you some recommendations of things to read or watch "
        "based on the NY Times:\n"
        "- bestsellers list for hardcover fiction\n"
        "- most popular articles from the last 30 days\n"
        "- movie reviews that are critics' picks!\n")
print(input("Press any key to get started!"))
print("Do you want to read or watch a movie?\n"
        "Your choices:\n    A - read\n    B - watch a movie")
# lower() makes the user input lowercase
choice = input("Choose a letter and type your choice here: ").lower()
if choice == "a":
    print("\nWould you like to read some books or articles?\n"
            "You choices:\n    A - books\n    B - articles")
    reading_choice = input(
        "Choose a letter and type your choice here: ").lower()
    if reading_choice == "a":
        print("\nHow many book recommendations do you want? (max = 15)")
        # int() turns the user input (which is a string) into an integer
        num_of_books = int(input("Type number here: "))
        # the max number of books in the book_url data is 15
        if num_of_books <= 15:
            print("\nFinding some good books for you to read...")
            # calling the progress_bar function to display a live progress bar
            progress_bar(num_of_books)
            print("\nAll done! Enjoy reading :)")
            # displays list after 1 second
            time.sleep(1)
            # calling the extract, book_function, and display functions;
            # setting the header of this list as BOOK LIST
            display(
                book_function(extract(book_url), num_of_books), "BOOK LIST")
        else:
            # error handling - in case user types more than max num
            print(
                "\nOops! You can only view up to 15! "
                "Please choose a number between 1 and 15!\n")
    elif reading_choice == "b":
        print("\nHow many article recommendations do you want? (max = 20)")
        num_of_articles = int(input("Type number here: "))
        # the max number of articles in the article_url is 20
        if num_of_articles <= 20:
            print("\nFinding some interesting articles for you to read...")
            progress_bar(num_of_articles)
            print("\nAll done! Enjoy reading :)")
            time.sleep(1)
            # calling the extract, article_function, and display functions;
            # setting the header of this list as ARTICLE LIST
            display(
                article_function(
                    extract(article_url), num_of_articles), "ARTICLE LIST")
        else:
            # error handling - in case user types more than max num
            print(
                "\nOops! You can only view up to 20! "
                "Please choose a number between 1 and 20!\n")
    else:
        # error handling - just in case user types something that is not a or b
        print("\nOops! Please type the letter A or B to move on!\n")
elif choice == "b":
    print("\nHow many movies movie recommendations do you want? (max = 20)")
    num_of_movies = int(input("Type number here: "))
    # the max number of movies in the movie_article is 20
    if num_of_movies <= 20:
        print("\nFinding some interesting movies for you to watch...")
        progress_bar(num_of_movies)
        print("All done! Enjoy watching :)")
        time.sleep(1)
        # calling the extract, movie_function, and display functions;
        # setting the header of this list as MOVIE LIST
        display(
            movie_function(extract(movie_url), num_of_movies), "MOVIE LIST")
    else:
        # error handling - just in case user types something that is not a or b
        print(
            "\nOops! You can only view up to 20! "
            "Please choose a number between 1 and 20!\n")
else:
    # error handling - just in case user types something that is not a or b
    print("\nOops! Please type the letter A or B to move on!\n")
