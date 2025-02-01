def count_words(text):
    words = text.split()
    return len(words)    

def main():
    wordCount = 0

    with open("books/frankenstein.txt") as f:
        for file_contents in f:
            wordCount += count_words(file_contents)
            print(file_contents.strip())
        
    print(wordCount)

main()
