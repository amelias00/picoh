import picoh
import time
import random

# Inicjalizacja Picoh
picoh.Init()
picoh.SetBaseColour(0, 255, 0)  # Ustawienie zielonego koloru podstawowego

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

    picoh.Say("Witaj w grze Fake News Challenge!")
    time.sleep(1)

    for news, is_true in news_data:
        picoh.Say("Uwaga! Oto wiadomość:")
        time.sleep(1)
        picoh.Say(news)
        time.sleep(1)

        # Pytanie do gracza
        picoh.Say("Czy to prawda? Odpowiedz tak lub nie.")

        answer = input("Czy to prawda? (tak/nie): ").strip().lower()

        # Sprawdzenie odpowiedzi
        if (answer == "tak" and is_true) or (answer == "nie" and not is_true):
            picoh.Say("Dobra odpowiedź!")
            picoh.SetMouth("happy")
            score += 1
        else:
            picoh.Say("Niestety, to błąd.")
            picoh.SetMouth("sad")

        time.sleep(1)

    # Podsumowanie gry
    picoh.Say(f"Koniec gry! Twój wynik to {score} na {len(news_data)}.")
    if score == len(news_data):
        picoh.Say("Jesteś mistrzem wykrywania fake newsów!")
    elif score > len(news_data) // 2:
        picoh.Say("Całkiem nieźle, ale jeszcze trochę nauki!")
    else:
        picoh.Say("Musisz być bardziej ostrożny w sieci!")

    picoh.SetMouth("neutral")

# Uruchomienie gry
play_game()

# Resetowanie Picoh
picoh.Close()
