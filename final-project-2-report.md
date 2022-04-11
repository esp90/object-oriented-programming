# Esther's Media Recommendation Project v.1

## Introduction

This project uses data from the New York Times API to create lists of different media types for the user. These recommendation lists are created by the user who is asked to choose one of three options: read books, read articles, or watch a movie. The user also chooses how many items they want to see in the list. Based off of the user's choices, a group of functions is called, which allows specific data to be retrieved and added to a list that gets displayed. The list is presented as a table with one column.
<br>
<br>
The data retrieved for the list of books is from the NY Times Books API (for this project I use the data from the bestsellers list for hardcover fiction). The data for the list of articles is retrieved from the NY Times Most Popular API and the data here shows which articles have been viewed the most in the last 30 days. For the list of movies, I use the NY Times Movie Reviews API and specifically look at the movie reviews that are critics' picks.
<br>
<br>
For this project, I used Visual Studio Code as my code editor and used my laptop's Terminal window to run my code and view the results. I created a virtual environment for this project and installed the necessary packages in that environment.

---

## Code Walkthrough

My first block of code (see image below) consists of all the import statements for this project. The import statements are needed in order to use specific functions or methods that are based on the packages. The following are the different packages that I used for this project:
- **`requests`**: This module is used to request and obtain data from the web. This is important for this project because without this, we can't obtain data from the urls.
- **`random`**: This module has many methods that are related to randomization. For this project, I used `random.sample()` which creates a list of randomized elements (a sample) from an already existing list. This is a helpful method to use for my project because it prevents the same items from being included in the list as well as to change up the order of items so that the user doesn't always see the same items.
- **`textwrap`**: This module is used to wrap the text and prevent words from awkwardly breaking. I used `textwrap.fill()` to make sure that the text stays inside of its cell in the table that gets displayed. I used the `fill()` function rather than the `wrap()` function because the former returns the text as a string while the latter returns a list (which did not work well with my code). 
- **`time`**: This module has many functions that are related to time. I used `time.sleep()` for this project. The `sleep()` function delays the time it takes to print out something and is measured in seconds. I found this useful for my project because it helped to make things appear slower, which made it easier to see what was going on.
- **`tabulate`**: This module easily displays your data as a neat table. It also has many formats or styles. For this project, I used the `fancy-grid` format because it made everything look neat. I mainly used this module to make my list output look more neat and easier to read rather than as a table with multiple columns and rows of values.
- **`alive_progress`**: This module was used to create a live progress/loading bar. It's very customizable. You can manipulate the time that the bar loads and change the total number of items you want the bar to load to (I will explain this further in a later section). Using this module made it easier to create a progress bar and I used it to display a loading bar before a list gets displayed.
![import statements](https://i.imgur.com/WBDVcWZ.png "import statements")

My next block of code shows the various urls that I used for this project. The `apikey` variable (which is blank in this image due to privacy reasons) was created to shorten the urls. This key is necessary to access all of the data from the NY Times API and everyone gets their own unique key when they make an account for the [NY Times Developer website](https://developer.nytimes.com/).
![urls & api keys](https://i.imgur.com/duqjUpL.png "urls & api keys")

This block of code is a custom function that was created to extract data from a url. Here we see the `requests` module in action and after the request is made, the data is retrieved in the json format. The parameter for this function is a url. If the user chooses to read a book, then the url for the books data will be used. If the user chooses to read an article, the articles url will be used. And if the user chooses to watch a movie, then the movies url will be used.
![extract function](https://i.imgur.com/27SnJKF.png "extract function")

The next block of code shows the custom function that presents the finalized data as a neat table by using the `tabulate` module. There are 2 parameters for this function. The first one is needed to go through the finalized data and insert each item of the finalized data into each cell or block of the displayed table. Each item at each index of the finalized data gets added as a list (by using `append()`) to another list which is the one that is formatted into a table. So the table is basically a list that consists of other lists. The second parameter is for the header or title of the table. Depending on the user's choice, both parameters change accordingly.
![display function](https://i.imgur.com/3B2vXSV.png "display function")

This block of code is a custom function that was created to transform the data from the Books API. It goes through the data and obtains each book's title, author, short description, and the Amazon link. In this step the `textwrap` module is used and makes it so that each object is wrapped. The text goes to a new line when it reaches the width. These  wrapped objects are then consolidated into one variable called `book_info` and this is what gets displayed in each cell of the table. As the code goes through each item in the data, the `book_info` containing details of each book, is added to a list. When the iteration stops, the `random.sample()` function is used to create a new list of books that becomes randomized. As mentioned before, the function creates a sample list and the number of items in this list is determined by the `num_of_books` parameter. This represents the user input, and whatever number that the user inputs is the number of items that will be in the list that gets displayed.
![book function](https://i.imgur.com/UYzhjH5.png "book function")

This custom function works in the same way as the `book_function` that was previously explained. The only difference is that the data that gets transformed is from the Most Popular API. It goes through this data to obtain each article's title, abstract, and link to the NY Times article. 
![article function](https://i.imgur.com/ZkfCJdx.png "article function")

The same goes for this custom function, which goes through data from the Movie Reviews API to get each movie's title, short discription, rating, and link to the NY Times movie review. I noticed that some ratings were left blank so whenever there is a blank rating, the word `None` will be displayed instead of a blank.
![movie function](https://i.imgur.com/LM1yXMJ.png "movie function")

This function creates the live progress bar by using a combination of the `alive_progress` and `time` modules. The first image shows my code and the next image shows what the progress bar looks like in the Terminal window. Notice how the number to the left of the percentage is the same as the number that the user inputted. For this function, the user input is the parameter so the number of items that the progress bar has to load through is the same as the number of items that the user wants included in the list. In this example, the user wants 10 items so the progress bar starts at 1/10 and ends at 10/10 and the user is able to see everything in between! I used `time.sleep()` because without it the progess bar loaded very quickly and the user can't see the whole process. By using `time.sleep()` I was able to make each loading bar load at every second. This made it easier for the user to actually see the loading process. 
![progress bar function](https://i.imgur.com/d6A39RT.png "progress bar function")
![progress bar](https://i.imgur.com/Em3vnJr.png "progress bar screenshot")

This next block of code just shows a welcome message that briefly explains where the data for the recommendations is coming from. The user will take time to read this and whenever they are ready, they can press any key to move on. The next thing that gets displayed is the first question that the user will be asked which is if they want to read or watch a movie.
![welcome message](https://i.imgur.com/N4vboct.png "welcome message")

This block of code partially shows what happens when the user chooses if they want to read or watch a movie. First, whatever the user inputs becomes all lowercase (by using `.lower`) just in case the user doesn't put a capital letter A or B. The next portion of the code shows what happens when the user inputs A (chooses to read). They are asked another question, which is whether they want to get book recommendations or articles to read. If they choose books then they are asked how many books they want to see. Whatever number that the user inputs becomes the `num_of_books` which is used when calling the `book_function` and the `progress_bar` functions. Because the API data only shows 15 items for books, the maximum number that the user can input is 15. To crudely handle an error of when the user inputs a number that is higher than 15, an error message appears. But if the input number is 15 or lower, then the `progress_bar` function is called and a progress bar is displayed. Next, the `display`, `book_function`, and `extract` functions are called. When called together, these functions get data from the Books API and retrieve the necessary information which is displayed as a table-like list. In the `display()` function, we see the header of the table being set to `BOOK LIST`.
![choosing books](https://i.imgur.com/ZSz8GVY.png "books")

This block of code continues from the previous portion of code and shows what happens when the user choose to read articles. This part works similarly to the previous part of code with the `progress_bar` function and the simultaneous calling of the `display`, `article_function`, and `extract` functions. The header is set appropriately to `ARTICLE LIST`. The error handling also works in the same way but the maximum number here is 20. The last `else` statement is for in the beginning when the user doesn't input either A for book or B for article. If this situation occurs, an error message is displayed.
![choosing articles](https://i.imgur.com/13lfjHs.png "articles")

This portion of code shows what happens in the beginning when the user chooses to watch a movie or doesn't input A or B. Everything inside of the `elif` statement works the same as the previous two blocks of code and the header here is set to `MOVIE LIST`. Again an error message appears if the user doesn't choose either A for reading or B for watching a movie.
![choosing movies](https://i.imgur.com/TUaDzDe.png "movies")

---

## Summary of Results

The tool that I used after my loading process is the Terminal window. I displayed my finalized data as a table-like list as an output in Terminal. In each list, there is a header and each cell or block of the list contains information about the item. I thought that using `tabulate` to create a table of the presented data would make it easier to read rather than just printing a list of words. The lines help to separate each item in the list and overall makes the appearance very clean. Below are examples of lists for each type of media. Notice that each item is unique and never repeated due to the `random.sample()` function.

![book list](https://i.imgur.com/gbwPV0H.png "book list screenshot")
![article list](https://i.imgur.com/TXQYXg1.png "article list screenshot")
![movie list](https://i.imgur.com/PBSy6ce.png "movie list screenshot")

---

## Room for Improvements

I definitely know that I can improve my code. Originally my idea was to give the user the option to choose more than one media type (i.e. books and movies, books and articles, all 3, etc.), but I couldn't quite figure out how to execute that in the beginning. However, I definitely think that if I took the time to figure it out and experiment with my code, I could make this idea work. And if I was doing this project for realsies, I would try to find a way to make the links clickable rather than copy and paste. In the current version of this project, if the user copies the link from the list, theres a space between where the line in the link breaks, which is very inconvenient if they were trying to access that link. I also think that for the movies list, it would be cool to make it so that a YouTube link that shows the trailer for each movie is added to the list because personally I like to watch movie trailers rather than read reviews. However, I think that this might make the project very largescale. I also think that I can combine some lines of code into one custom function and maybe even see if I can just make one transformation function and add parameters for each media type.

---

## My Full Python Script

```python
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


apikey = # insert NY Times API key here
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

```
