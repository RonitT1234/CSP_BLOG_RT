import random

#ChatGPT was used throughout the test in certain print statements to make the words sound more formal.

comments = []

def add_comment(movie, comment_text, rating, pin):
    comments.append({"movie": movie, "comment_text": comment_text, "rating": rating, "likes": 0, "pin": pin})

# the following sample comments were created with the assitance of ChatGPT.
add_comment("The Shawshank Redemption", "Classic movie, a powerful story of hope and friendship.", 5, str(random.randint(1000, 9999)))
add_comment("The Godfather", "Timeless movie, a gripping tale of family and power.", 5, str(random.randint(1000, 9999)))
add_comment("The Dark Knight", "Iconic movie, Heath Ledger's Joker is unforgettable.", 5, str(random.randint(1000, 9999)))
add_comment("Forrest Gump", "Heartwarming movie, Tom Hanks delivers an incredible performance.", 4, str(random.randint(1000, 9999)))
add_comment("The Matrix", "Groundbreaking movie, redefined action and sci-fi genres.", 4, str(random.randint(1000, 9999)))
add_comment("Pulp Fiction", "Quentin Tarantino at his best, a must-watch for film enthusiasts.", 4, str(random.randint(1000, 9999)))
add_comment("The Silence of the Lambs", "Thrilling movie, Anthony Hopkins' portrayal of Hannibal Lecter is chilling.", 4, str(random.randint(1000, 9999)))
add_comment("Schindler's List", "Emotional movie, Steven Spielberg's masterpiece.", 5, str(random.randint(1000, 9999)))
add_comment("Inception", "Mind-bending movie, Christopher Nolan's vision is incredible.", 4, str(random.randint(1000, 9999)))
add_comment("Titanic", "Epic movie, a tragic love story that captured the world.", 4, str(random.randint(1000, 9999)))
add_comment("The Lion King", "Timeless classic, a beautifully animated film with a powerful message.", 5, str(random.randint(1000, 9999)))
add_comment("The Shawshank Redemption", "Classic movie, a powerful story of hope and friendship.", 5, str(random.randint(1000, 9999)))
add_comment("The Godfather", "Timeless movie, a gripping tale of family and power.", 5, str(random.randint(1000, 9999)))
add_comment("The Dark Knight", "Iconic movie, Heath Ledger's Joker is unforgettable.", 5, str(random.randint(1000, 9999)))
add_comment("Forrest Gump", "Heartwarming movie, Tom Hanks delivers an incredible performance.", 4, str(random.randint(1000, 9999)))
add_comment("The Matrix", "Groundbreaking movie, redefined action and sci-fi genres.", 4, str(random.randint(1000, 9999)))
add_comment("Pulp Fiction", "Quentin Tarantino at his best, a must-watch for film enthusiasts.", 4, str(random.randint(1000, 9999)))
add_comment("The Silence of the Lambs", "Thrilling movie, Anthony Hopkins' portrayal of Hannibal Lecter is chilling.", 4, str(random.randint(1000, 9999)))
add_comment("Schindler's List", "Emotional movie, Steven Spielberg's masterpiece.", 5, str(random.randint(1000, 9999)))
add_comment("Inception", "Mind-bending movie, Christopher Nolan's vision is incredible.", 4, str(random.randint(1000, 9999)))
add_comment("Titanic", "Epic movie, a tragic love story that captured the world.", 4, str(random.randint(1000, 9999)))


def edit_comment(movie, new_comment_text, new_rating, pin):
    for comment in comments:
        if comment["movie"] == movie and comment["pin"] == pin:
            comment["comment_text"] = new_comment_text
            comment["rating"] = new_rating
            print(f"\nComment on movie '{movie}' has been updated.\n")
            return
    print("\nEither the comment does not exist or the provided PIN is incorrect.\n")

def like_comment(movie):
    for comment in comments:
        if comment['movie'] == movie:
            comment['likes'] += 1
            print(f"\nComment '{comment['comment_text']}' on movie '{movie}' has been liked. Total likes: {comment['likes']}\n")
            return
    print(f"\nComment on movie '{movie}' not found.\n")

def get_random_comments(num_comments):
    for comment in random.sample(comments, min(num_comments, len(comments))):
        print(f"\nmovie: {comment['movie']}")
        print(f"comment: {comment['comment_text']}")
        print(f"Rating: {comment['rating']} out of 5")
        print(f"Likes: {comment['likes']}\n")

def print_comments_by_rating(desired_rating):
    matching_comments = []
    for comment in comments:
        if comment['rating'] == desired_rating:
            matching_comments.append(comment)
    for comment in matching_comments:
        print(f"\nmovie: {comment['movie']}")
        print(f"comment: {comment['comment_text']}")
        print(f"Rating: {comment['rating']} out of 5")
        print(f"Likes: {comment['likes']}\n")

def get_most_liked_comments(num_comments):
    #ChatGPT also helped fix the following line:
    sorted_comments = sorted(comments, key=lambda x: x['likes'], reverse=True)
    for comment in sorted_comments[:num_comments]:
        print(f"\nmovie: {comment['movie']}")
        print(f"comment: {comment['comment_text']}")
        print(f"Rating: {comment['rating']} out of 5")
        print(f"Likes: {comment['likes']}\n")

#ChatGPT also provided a template for the get_comment_statistics below:
def get_comment_statistics():
    total_comments = len(comments)
    total_likes = sum(comment['likes'] for comment in comments)
    average_rating = sum(comment['rating'] for comment in comments) / total_comments if total_comments > 0 else 0
    print(f"\nTotal comments: {total_comments}")
    print(f"Total likes: {total_likes}")
    print(f"Average rating: {average_rating:.2f} out of 5\n")

while True:
    print("1. Add a comment")
    print("2. Edit a comment")
    print("3. Like a comment")
    print("4. Get random comments")
    print("5. Print comments by rating")
    print("6. Get comments with the most likes")
    print("7. Get comment statistics")
    print("8. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        movie = input("Enter the movie name: ")
        comment_text = input("Enter your comment: ")
        rating = int(input("Enter the rating (1-5): "))
        pin = str(random.randint(1000, 9999))
        add_comment(movie, comment_text, rating, pin)
        print("Your comment has been added!\n")
        print(f"Your PIN is: {pin}\n")
    elif choice == "2":
        movie = input("Enter the movie name: ")
        pin = input("Enter your PIN: ")
        new_comment_text = input("Enter the new comment text: ")
        new_rating = int(input("Enter the new rating (1-5): "))
        edit_comment(movie, new_comment_text, new_rating, pin)
    elif choice == "3":
        movie = input("Enter the movie name: ")
        like_comment(movie)
    elif choice == "4":
        num_comments = int(input("Enter the number of random comments you want to see: "))
        get_random_comments(num_comments)
    elif choice == "5":
        desired_rating = int(input("Enter the rating (1-5) of comments you want to filter by: "))
        print_comments_by_rating(desired_rating)
    elif choice == "6":
        num_comments = int(input("Enter the number of comments you want to see with the most likes: "))
        get_most_liked_comments(num_comments)
    elif choice == "7":
        get_comment_statistics()
    elif choice == "8":
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Please try again.\n")