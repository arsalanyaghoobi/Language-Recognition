
Langauge = input("Enter the langauge you want to check if it is English ,Persian ,Japanese ,"
                 "Russian, Greek, Hebrew,German , or Nepali    ")
New_Language1=0
New_Langauge2=0

print("The Language Produced is   ", Langauge)
list_of_letters = list(Langauge)
Num_Letter_list_of_letters=len(list_of_letters)
print("Number of Letters in Language produced including Spaces is  ", Num_Letter_list_of_letters)
print(list_of_letters)



Eng_Alphabet= ["A","a","B","b","C","c","D","d","E","e","F","f","G","g","H","h","I","i","J","j","K","k","L","l",
               "M","m","N","n","O","o","P","p","Q","q","R","r","S","s","T","t","U","u",
               "V","v","W","w","X","x","Y","y","Z","z"]
Persi_Alphabet= ["آ","ا","ب","پ","ت","ث","ج","چ","ح","خ","د","ذ","ر","ز","ژ","س","ش",
                 "ص","ط","ظ","ع","غ","ف","ق","ک","گ","ل","م","ن","و","ه","ی"]
Japan_Alphabet= ["あ","い","う","え","お","か","き","く","け","こ","さ","し","す","せ","そ","た","ち","つ",
                "て","と","な","に","ぬ","ね","の","は","ひ","ふ","へ","ほ",
                "ま","み","む","め","も","や","ゆ","よ","ら","り","る","れ","ろ","わ","を","ん"]
Russian_Alphabet= ["А","а","Б","б","В","в","Г","г","Д","д","Е","е","Ё","ё","Ж","ж","З","з","И","и","Й","й","К","к","Л",
                  "л","М","м","Н","н","О","о","П","п","Р","р","С","с","Т","т","У","у"
                  ,"Ф","ф","Х","х","Ц","ц","Ч","ч","Ш","ш","Щ","щ","Ъ","ъ","Ы","ы","Ь","ь","Э","э","Ю","ю","Я","я"]
Greek_Alphabet= ["Α","α","Β","β","Γ","γ","Δ","δ","Ε","ε","Ζ","ζ","Η","η","Θ","θ","Ι","ι","Κ","κ","Λ","λ"
                 ,"Μ","μ","Ν","ν","Ξ","ξ","Ο","ο","Π","π","Ρ","ρ","Σ","σ","ς","Τ","τ","Υ","υ","Φ","φ",
                 "Χ","χ","Ψ","ψ","Ω","ω"]
Hebrew_Alphabet = ["ב","בּ","ג","ד","ה","ו","ז","ח","ט","י","כּ","כ","ךּ","ך","ל","מ","ם","נ"
                    ,"ן","ס","ע","פּ","פ","ף","צ","ץ","ק","ר","שׁ","א","שׂ","תּ","ת"]
German_Alphabet = ["ä","ö","ü","ß","A","a","B","b","C","c","D","d","E","e","F","f","G","g","H","h","I","i","J","j","K","k","L","l",
               "M","m","N","n","O","o","P","p","Q","q","R","r","S","s","T","t","U","u",
               "V","v","W","w","X","x","Y","y","Z","z"]
Nepalian_Alphabet = ["क","ख","ग","घ","ङ","च","छ","ज","झ","ञ","ट","ठ","ड","ढ","ण","त","थ","द","ध"
                     ,"न","प","फ","ब","भ","म","य","र","ल","व","श","ष","स"
                     ,"ह","क्ष","त्र","ज्ञ","अ","आ","इ","ई","उ","ऊ","ऋ","ए","ऐ","ओ","औ","अं","अः"]
Other_Alphabets = []





Number_Eng_Alph =len(Eng_Alphabet)/2
Number_Persia_Alph = len(Persi_Alphabet)
Number_Japan_Alph = len(Japan_Alphabet)
Number_Russian_Alph = len(Russian_Alphabet)/2-1
Number_Greece_Alph = (len(Greek_Alphabet)-1)/2
Number_Hebrew_Alph = (len(Hebrew_Alphabet))-11
Number_German_Alph = (len(German_Alphabet)/2)-2
Number_Nepali_Alph = (len(Nepalian_Alphabet))-3





E=0
P=0
J=0
R=0
G=0
H=0
Ger=0
N=0
Ger_Unique_List= ["ä","ö","ü","ß"]



for letters in list_of_letters:
    if letters in Eng_Alphabet:
        E = len(list_of_letters)
    else:
        if letters in Persi_Alphabet:
            P = len(list_of_letters)
        else:
             if letters in Nepalian_Alphabet:
                N = len(list_of_letters)
             else:
                 if letters in Japan_Alphabet:
                     J = len(list_of_letters)
                 else:
                     if letters in Russian_Alphabet:
                         R = len(list_of_letters)
                     else:
                         if letters in Greek_Alphabet:
                             G = len(list_of_letters)
                         else:
                             if letters in Hebrew_Alphabet:
                                 H = len(list_of_letters)
                             else:
                                 if letters in German_Alphabet:
                                     Ger = len(list_of_letters)
                                     break


if E>P and E>N and E>J and E>R and E>G and E>H and E>Ger:
    for letters in list_of_letters:
        if letters in Ger_Unique_List:
            print("Language is German, yappp")
            print("Number of German Alphabets is ", Number_German_Alph)
            break
        if not letters in Eng_Alphabet and Ger_Unique_List:
                print("Language is beyond my knowledge , you can check it online...")
        else:
            New_Language1 = input(" please add another and larger piece of language for identification  ")
            New_list_of_letters1 = list(New_Language1)
            for letters in New_list_of_letters1:
                if letters in Ger_Unique_List:
                    print("Language is German, YESSS")
                    print("Number of German Alphabets is ", Number_German_Alph)
                    break
                else:
                    New_Language2 = input("Sorry me; for the last time, to make sure that "
                                          "language is English, let me have "
                                          "another (big) portion of this language ")
                    New_list_of_letters2 = list(New_Language2)
                    for letters in New_list_of_letters2:
                        if letters in Ger_Unique_List:
                            print("Language is German, yapp")
                            print("Number of German Alphabets is ", Number_German_Alph)
                            break
                        else:
                            print("Language is English, Wooow ")
                            print("Number of English Alphabets is ", Number_Eng_Alph)
                            break
                            New_Language2 = True
                            New_Language1 = True
                if New_Language2: break
        if New_Language1: break


elif Ger==E and Ger>N and Ger>J and Ger>R and Ger>G and Ger>H:
    print("Language is German, Hoorah")
    print("Number of German Alphabets is ", Number_German_Alph)
elif Ger>E:
    print("Language is German, Mmmm")
    print("Number of German Alphabets is ", Number_German_Alph)
elif P>E and P>N and P>J and P>R and P>G and P>H and P>Ger:
    print("Language is Persian")
    print("Number of Persian Alphabets is ", Number_Persia_Alph)
elif J>P and J>E and J>N and J>R and J>G and J>H and J>Ger:
    print("Language is Japanese")
    print("Number of Japanese Alphabets is ", Number_Japan_Alph)
elif R>P and R>E and R>J and R>N and R>G and R>H and R>Ger:
    print("langage is Russian")
    print("Number of Russian Alphabet is ", Number_Russian_Alph)
elif G>P and G>E and G>J and G>N and G>R and G>H and G>Ger:
    print("Language is Greek")
    print("Number of Greece Alphabet is ", Number_Greece_Alph)
elif H>P and H>E and H>J and H>N and H>R and H>G and H>Ger:
    print("Language is Hebrew")
    print("Number of Hebrew Alphabets is ", Number_Hebrew_Alph)
elif N>P and N>E and N>J and N>H and N>R and N>G and N>Ger:
    print("Language is Nepali")
    print("Number of Alphabets in Nepali language is ", Number_Nepali_Alph)
else:
    print("Language is beyond my knowledge , you can check it online...")
