from stats import word_count, get_character_frequencies

def main():
    filepath = "books/frankenstein.txt"
    text = get_text(filepath)
    report = create_report(filepath, text)

    print(report)

def create_report(filepath, text):
    report = "============ BOOKBOT ============\n"
    report += f"Analyzing book found at {filepath}\n"
    report += "----------- Word Count ----------\n"
    report += f"Found {word_count(text)} total words\n"
    report += "--------- Character Count -------\n"
    character_frequencies = get_character_frequencies(text)
    for frequency in character_frequencies:
        report += f"{frequency['character']}: {frequency['count']}\n"
    report += "============= END ==============="
    return report

def get_text(filepath):
    with open(filepath) as f:
        contents = f.read()
    return contents

if __name__ == "__main__":
    main()
