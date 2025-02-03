def count_words(text):
    words = text.split()
    return len(words)    

def count_chars(text):
    r = {}
    l = text.lower()
    for c in l:
        if not c in r:
            r[c] = 1
        else:
            r[c] = r[c] + 1
    
    return r

def main():
    wordCount = 0
    charCount = { }

    with open("books/frankenstein.txt") as f:
        for file_contents in f:
            wordCount += count_words(file_contents)
            chars = count_chars(file_contents)
            for c in chars:
                if not c in charCount:
                    charCount[c] = chars[c]
                else:
                    charCount[c] = charCount[c] + chars[c]
            
            # print(file_contents.strip())
        
    
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{wordCount} words found in the document")
    print()
    for c in charCount:
        if c in 'abcdefghijklmnopqstuvwxyz':
            print(f"The '{c}' character was found {charCount[c]} times")
    print("--- End report ---")

main()
