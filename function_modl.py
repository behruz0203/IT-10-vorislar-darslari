def darajaga_oshirish(a,b):
    """a sonining b ichi darajasini hisoblash funksiyasi"""
    print(f"{a} ** {b} = {a**b}")

def salomber(ism):
    """kiritilgan isimga qo'shimcha matn yozib chiqalish funksiyasi"""
    print(f"Assalomu alaykum {ism.title()} ishlar, o'qishlar yaxshimi?")

def  ishorani_aniqlash(son):
    """a sonining sonni musbat, manfiy yoki nolga teng ekanini aniqlovchi funksiya"""
    if son > 0:
        print("Siz kiritgan son MUSBAT")

    elif son < 0:
        print("Siz kiritgan son MANFIY")

    else:
        print("Siz kiritgan son NOLGA TENG")

# def mashina_taklif_qilish(narx):
#     """Mijozni puliga qarab unga yetadigan mashinalar taklif qilish funksiyasi"""
# print("""sizda qancha miqdorda pul bor(som) bor sizni pulingizga mos mashina tanlab beraman""")
# ism = input("isimingizni kiriting: ")
# miqdor = int(input("summani kiriting: :"))
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





# def orta_arifmetik(*sonlar):
#     """Siz kiritgan sonlarning o'rta alifmetikini hisoblash funksiyasi"""

# def orta_geometrk(*sonlar):
#     """siz kiritgan sonlarning o'rta geometrikini hisoblash funksiyasi"""


# darajaga_oshirish(5,3)
# salomber("behruzbek")
# ishorani_aniqlash(-5)
# mashina_taklif_qilish(40)