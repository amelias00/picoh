import time
import random

# Lista wiadomości (prawdziwe i fałszywe)
news_data = [
    ("Naukowcy potwierdzili, że Ziemia jest płaska.", False),
    ("Badania wykazały, że mycie rąk zmniejsza ryzyko infekcji.", True),
    ("Kot w Nowym Jorku zdał egzamin na prawo jazdy.", False),
    ("NASA potwierdziła istnienie wody na Marsie.", True),
    ("Pijąc wodę z cytryną, możesz wyleczyć wszystkie choroby.", False),
]

def play_game():
    score = 0  # Liczba poprawnych odpowiedzi
    random.shuffle(news_data)  # Losowe mieszanie wiadomości

    print("\n=== Fake News Challenge ===")
    print("Odpowiadaj 'tak' lub 'nie' na poniższe wiadomości.\n")
    time.sleep(1)

    for news, is_true in news_data:
        print("\nUwaga! Oto wiadomość:")
        time.sleep(1)
        print(f"» {news}")
        time.sleep(1)

        answer = input("Czy to prawda? (tak/nie): ").strip().lower()

        # Sprawdzenie odpowiedzi
        if (answer == "tak" and is_true) or (answer == "nie" and not is_true):
            print("Dobra odpowiedź!")
            score += 1
        else:
            print("Niestety, to błąd.")

        time.sleep(1)

    # Podsumowanie gry
    print("\n=== Koniec gry! ===")
    print(f"Twój wynik: {score} na {len(news_data)}.")

    if score == len(news_data):
        print("Jesteś mistrzem wykrywania fake newsów!")
    elif score > len(news_data) // 2:
        print("Całkiem nieźle, ale jeszcze trochę nauki!")
    else:
        print("Musisz być bardziej ostrożny w sieci!")

# Uruchomienie gry
play_game()

