print("""sizda qancha miqdorda pul bor(som) bor sizni pulingizga mos mashina tanlab beraman""")
ism = input("isimingizni kiriting: ")
miqdor = int(input("summani kiriting: :"))
# if miqdor <= 20:
#     print(f"{ism.title()} siz bu pulga TIKO, JIGULI, DAEWOO, NEXIA, MATIZ kabi mashinalarni sotib olishingiz mumkin")
# elif miqdor > 20 and miqdor <= 40:
#     print(f"{ism.title()} siz bu pulga TIKO, JIGULI, DAEWOO, NEXIA, MATIZ, DAMAS kabi mashinalarni sotib olishingiz mumkin")
# elif miqdor > 40:
#     print(f"{ism.title()} siz bu pulga  NEXIA 2, MATIZ, DAMAS kabi mashinalarni sotib olishingiz mumkin")

# elif miqdor > 70:
#     print(f"{ism.title()} siz bu pulga  NEXIA 2, MATIZ, DAMAS, SPARK, kabi mashinalarni sotib olishingiz mumkin")
# elif miqdor > 150:
#     print(f"{ism.title()} siz bu pulga  NEXIA 2, MATIZ, DAMAS NEXIA 3, QOBALT, JENTRA kabi mashinalarni sotib olishingiz mumkin")


# # While sikl operaatori
# son = 1
# while son <= 10:
#     print(f"(son)-sikl : Behruzbek ...")
#     son += 1


# son = 1
# while son <=20:
#     print(f"Behruzbekga yoqadigan sonlar {son }")
#     son += 1
#     if son == 17:
#         break


print("ENG YAQIN 5 TA DO'STINGIZNI ISMINI KIRITING")
ism = input("Ismingizni nima? ")
son = 1
mevalar =[]


while son <= 5:
    savol = f"{ism.title()} {son} - eng yaqi dostingiz kim ? "
    ism1 = input(savol)
    print(ism1)
    son +=1
