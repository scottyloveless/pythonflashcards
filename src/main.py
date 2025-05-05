from datamodel import FlashCard

def main():
    name = input("Name: ")
    front = input("Front: ")
    back = input("Back: ")

    new_card = FlashCard(name, front, back)
    new_card.save_flashcard()
    return print(f"New card saved: {new_card.name}")

main()
