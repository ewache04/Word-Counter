'''
Author name: Jeremiah E. Ochepo
Code description: Exception and handling errors (Word Counter)
Last Updated Date: 9/29/19
'''


def word_count(file_path):
    try:
        with open(file_path, 'r') as file_object:
            file_content = file_object.read()
    except FileNotFoundError:
        msg = f"Sorry, the file {file_path} does not exist."
        print(msg)
    else:
        # Count approximate number of words in the file.
        words_list = file_content.split()
        num_words = len(words_list)
        print(f"The file has approximately {num_words} words.")


if __name__ == "__main__":
    # Example usage
    file_path = 'text.txt'
    word_count(file_path)
