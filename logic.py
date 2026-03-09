"""
This is the File for the logic of the programm
"""
from wonderwords import RandomWord
import random
mode = 'classic'
def random_word():
    """
    This is to choose a random word from the English dictionary
    :return:
    """
    rw = RandomWord()
    word = rw.word(word_max_length=10)
    return word

guessed_letters = [] # List of Letters that are typen
correct_letters = [] # List of letters that are correct
def check_for_input(pressed_key, word):  # This function appends input to the list "guessed_letters"
    """
    :param pressed_key: The pressed button (for example "a")
    :param word: The word that we have to guess correctly
    :return:
    """
    guessed_letters.append(pressed_key)
    print(pressed_key)
    for char in word:
        if char in guessed_letters:
            icon = f"[\u2714]"
            correct_letters.append(char)
        else:
            icon = f"[\u2718]"
        print(f"'{char}'{icon}")


def celebrities_word():
    celebrities = [
        # 🎵 Musik
        "Taylor Swift", "Billie Eilish", "Olivia Rodrigo", "Doja Cat", "Dua Lipa",
        "The Weeknd", "Bad Bunny", "Drake", "Post Malone", "Travis Scott",
        "Ariana Grande", "Harry Styles", "Ed Sheeran", "Beyoncé", "Rihanna",
        "Kendrick Lamar", "SZA", "Lil Nas X", "Jack Harlow", "Lizzo",
        "Sabrina Carpenter", "Gracie Abrams", "Chappell Roan", "Charli XCX", "Troye Sivan",
        "Rex Orange County", "Conan Gray", "Clairo", "Mitski", "Phoebe Bridgers",
        "Justin Bieber", "Shawn Mendes", "Camila Cabello", "Selena Gomez", "Miley Cyrus",
        "Nicki Minaj", "Cardi B", "Megan Thee Stallion", "Ice Spice", "GloRilla",
        "Peso Pluma", "Feid", "J Balvin", "Maluma", "Karol G",
        "Rosalía", "Anitta", "Becky G", "Nathy Peluso", "C. Tangana",
        "BTS", "BLACKPINK", "Stray Kids", "NewJeans", "aespa",
        "IU", "G-Dragon", "CL", "Sunmi", "Taeyang",
        "Coldplay", "Imagine Dragons", "Twenty One Pilots", "Panic! At The Disco", "Fall Out Boy",
        "Machine Gun Kelly", "Yungblud", "Willow Smith", "Jaden Smith", "Channel Tres",
        "Frank Ocean", "Tyler the Creator", "Childish Gambino", "Anderson Paak", "Bruno Mars",
        "John Legend", "Sam Smith", "Demi Lovato", "Halsey", "Lorde",
        "Zara Larsson", "Ava Max", "Anne-Marie", "Lewis Capaldi", "Niall Horan",
        "Liam Payne", "Louis Tomlinson", "Zayn Malik", "Normani", "Tinashe",

        # 🎬 Schauspieler / Film / TV
        "Zendaya", "Timothée Chalamet", "Tom Holland", "Sydney Sweeney", "Jacob Elordi",
        "Austin Butler", "Florence Pugh", "Anya Taylor-Joy", "Jenna Ortega", "Hunter Schafer",
        "Euphoria Cast", "Millie Bobby Brown", "Noah Schnapp", "Finn Wolfhard", "Sadie Sink",
        "Dwayne Johnson", "Ryan Reynolds", "Chris Evans", "Chris Hemsworth", "Robert Downey Jr.",
        "Scarlett Johansson", "Margot Robbie", "Emma Stone", "Jennifer Lawrence", "Natalie Portman",
        "Cate Blanchett", "Viola Davis", "Regina King", "Lupita Nyong'o", "Halle Bailey",
        "Pedro Pascal", "Oscar Isaac", "Idris Elba", "Michael B. Jordan", "Jonathan Majors",
        "Barry Keoghan", "Paul Mescal", "Andrew Garfield", "Ezra Miller", "Tom Hiddleston",
        "Saoirse Ronan", "Hailee Steinfeld", "Dove Cameron", "Joey King", "Maia Reficco",
        "Xochitl Gomez", "Isabela Merced", "Rachel Zegler", "Milly Alcock", "Emma D'Arcy",

        # 📱 Social Media / Content Creator
        "MrBeast", "PewDiePie", "KSI", "Logan Paul", "Jake Paul",
        "Addison Rae", "Charli D'Amelio", "Dixie D'Amelio", "Bella Poarch", "Avani Gregg",
        "Emma Chamberlain", "David Dobrik", "Liza Koshy", "James Charles", "NikkieTutorials",
        "Pokimane", "Valkyrae", "xQc", "Kai Cenat", "IShowSpeed",
        "Asmongold", "Ninja", "Tfue", "Shroud", "TimTheTatman",
        "Markiplier", "Jacksepticeye", "Lilly Singh", "Bretman Rock", "Tana Mongeau",
        "Trisha Paytas", "Shane Dawson", "Jeffree Star", "Colleen Ballinger", "Hannah Stocking",
        "Loren Gray", "Baby Ariel", "Zach King", "Brent Rivera", "Alan Chikin Chow",

        # ⚽ Sport
        "Lionel Messi", "Cristiano Ronaldo", "Kylian Mbappé", "Erling Haaland", "Vinicius Jr.",
        "Pedri", "Gavi", "Jude Bellingham", "Bukayo Saka", "Phil Foden",
        "Neymar Jr.", "Lamine Yamal", "Florian Wirtz", "Jamal Musiala", "Federico Valverde",
        "LeBron James", "Stephen Curry", "Kevin Durant", "Giannis Antetokounmpo", "Luka Dončić",
        "Victor Wembanyama", "Anthony Edwards", "Ja Morant", "Zion Williamson", "Paolo Banchero",
        "Serena Williams", "Naomi Osaka", "Coco Gauff", "Carlos Alcaraz", "Jannik Sinner",
        "Novak Djokovic", "Rafael Nadal", "Roger Federer", "Emma Raducanu", "Iga Świątek",
        "Simone Biles", "Sha'Carri Richardson", "Noah Lyles", "Mondo Duplantis", "Marcell Jacobs",
        "Patrick Mahomes", "Josh Allen", "Justin Jefferson", "Ja'Marr Chase", "Travis Kelce",
        "Shohei Ohtani", "Fernando Tatis Jr.", "Juan Soto", "Julio Rodriguez", "Wander Franco",
        "Max Verstappen", "Charles Leclerc", "Lando Norris", "George Russell", "Lewis Hamilton",
        "Jon Jones", "Israel Adesanya", "Conor McGregor", "Nate Diaz", "Alex Pereira",
        "Tyson Fury", "Anthony Joshua", "Canelo Álvarez", "Ryan Garcia", "Gervonta Davis",

        # 🏛️ Politik / Aktivismus
        "Greta Thunberg", "Malala Yousafzai", "Alexandria Ocasio-Cortez", "Jacinda Ardern", "Emmanuel Macron",
        "Justin Trudeau", "Barack Obama", "Michelle Obama", "Kamala Harris", "Joe Biden",
        "Donald Trump", "Elon Musk", "Bernie Sanders", "Pete Buttigieg", "Stacey Abrams",
        "Volodymyr Zelensky", "Narendra Modi", "Xi Jinping", "Olaf Scholz", "Giorgia Meloni",

        # 💼 Business / Tech
        "Jeff Bezos", "Mark Zuckerberg", "Bill Gates", "Tim Cook", "Sam Altman",
        "Sundar Pichai", "Jensen Huang", "Satya Nadella", "Jack Dorsey", "Evan Spiegel",

        # 🌍 Sonstige / Kultur
        "Kim Kardashian", "Kylie Jenner", "Kendall Jenner", "Khloé Kardashian", "Kourtney Kardashian",
        "Hailey Bieber", "Bella Hadid", "Gigi Hadid", "Dua Lipa", "Emily Ratajkowski",
        "Meghan Markle", "Prince Harry", "Kate Middleton", "Prince William", "King Charles",
        "Paris Hilton", "Lindsay Lohan", "Britney Spears", "Lady Gaga", "Katy Perry",
        "Nick Jonas", "Priyanka Chopra", "Deepika Padukone", "Shah Rukh Khan", "Ranveer Singh",
        "BamBam", "Lisa", "Jennie", "Rosé", "Jisoo", "Sophie Rain", "Lily Phillip",
        "Rizzler", "Johnny Sins", "Vitus", "Arun", "Riccardo"
    ]
    random_celebritie = random.choice(celebrities)
    return random_celebritie