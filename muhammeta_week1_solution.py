TEAM 1. HAFTA 1. 

#soru1_cevabi:

movies = []
for movie in range(3):
    movie = input(f'Enter your {movie + 1}. favorite movie:  ').title()
    movies.append(movie)
print(f'Your favorite movies are: {', '.join(movies)}')
print('You entered first: ', movies[0])
print('You entered last: ', movies[2])
print('The number of movies: ', len(movies))


#soru2_cevabi:

birth_year = int(input("Enter your birth year: "))
age = 2025 - birth_year
if age > 18:
    print(f'Your age is {age}. You are an adult.')
else:
    print(f'Your age is {age}. You are not adult.')


#soru3_cevabi:

cumle = input("Bir cumle giriniz:")
karakter_sayisi= len(cumle.replace(" ",""))
print("Karakter sayisi:",karakter_sayisi)

kelime_sayisi = cumle.strip()
print("Kelime sayisi:",len(kelime_sayisi.split()))

essiz_kelimeler = set(kelime_sayisi.split())
print("Essiz kelimerler:",essiz_kelimeler)

liste1= cumle.split()
liste2=[]

#1. yontem
for i in liste1:
    liste2.append(len(i))
liste2.sort()

uzunluk = (liste2[-1])

for i in liste1:
    if len(i)>= uzunluk:
        print("En uzun kelime:",i)
""""#2. yontem

uzunluk2 = max(liste1,key=len)
print("En uzun kelime:" , uzunluk2)"""


#soru4_cevabi:

products = {"apple": 3, "banana": 5, "bread": 2, "milk": 4}
print("Products and prices are: " , products)
print("Please choose 3 products:")
p1 = input("Product 1 : ")
p2 = input("Product 2 : ")
p3 = input("Product 3 : ")
if p1 and p2 and p3 in products.keys():
   print("Your basket: ", p1, p2, p3,sep="-")
   total = products[p1] + products[p2] + products[p3]
   print("Total price: ", total ," ", end = "Tl")
else:
    print("*******WARNING!******* \n"
          "One or more product doesn't exist")


#soru5_cevabi:

ogrenciler = {}
ogr_sayi = 3
#ogrenci bilgileri al
for i in range(ogr_sayi):
    isim = input(f"{i+1}.ogrenci ismi: ")
    notlari = []
    for j in range(3):
        notu = int(input(f"{isim} isimli ogrencinin {j+1}.notunu gir: "))
        notlari.append(notu)
    ogrenciler[isim] = notlari
print("\nOgrenci ortalamalari: ")
#Ogrenci ortalamalari hesapla
ortalamalar = {}
for isim, notlari in ogrenciler.items():
    ort = sum(notlari) / len(notlari)
    ortalamalar[isim] = ort
    print(f"{isim}: {ort}")
#En yuksek ortalamali ogrenci
yuksek_ogr = max(ortalamalar, key=ortalamalar.get)
yuksek_ort = ortalamalar[yuksek_ogr]
print(f"\nYuksek ortalama: {yuksek_ogr} ({yuksek_ort})")


#soru6_cevabi:

# Initial library dictionary
library = {
    "python101": "Available",
    "datascience": "Available",
    "algorithms": "Available"
}

# Track borrowed books in a set
borrowed_books = set()

while True:
    print("\n--- Library Menu ---")
    print("1 - Add Book")
    print("2 - Borrow Book")
    print("3 - Return Book")
    print("4 - View All Books")
    print("5 - Exit")

    choice = input("Choose an option (1-5): ")

    # 1 - Add Book
    if choice == "1":
        new_book = input("Enter book name to add: ").strip().lower()
        if new_book in library:
            print(f"'{new_book.title()}' already exists in the library.")
        else:
            library[new_book] = "Available"
            print(f"'{new_book.title()}' has been added to the library.")

    # 2 - Borrow Book
    elif choice == "2":
        book = input("Enter book name to borrow: ").strip().lower()
        if book not in library:
            print(f"'{book.title()}' does not exist in the library.")
        elif library[book] == "Borrowed":
            print(f"'{book.title()}' is already borrowed.")
        else:
            library[book] = "Borrowed"
            borrowed_books.add(book)
            print(f"You borrowed '{book.title()}'.")

    # 3 - Return Book
    elif choice == "3":
        book = input("Enter book name to return: ").strip().lower()
        if book not in borrowed_books:
            print(f"'{book.title()}' was not borrowed.")
        else:
            library[book] = "Available"
            borrowed_books.remove(book)
            print(f"'{book.title()}' has been returned.")

    # 4 - View All Books
    elif choice == "4":
        print("\n--- Library Collection ---")
        for book, status in library.items():
            print(f"{book.title()} - {status}")
        print("\n--- Statistics ---")
        print(f"Total books: {len(library)}")
        print(f"Available books: {list(library.values()).count('Available')}")
        print(f"Borrowed books: {list(library.values()).count('Borrowed')}")

    # 5 - Exit
    elif choice == "5":
        print("Exiting library system. Goodbye!")
        break

    else:
        print("Invalid choice. Please select between 1 and 5.")
