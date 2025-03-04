from datetime import datetime
import random
# print("sveiki visi!")
# print(5+7+4+16)
#
# vardas = "Petras"
# pavarde = "Petraitis"
# birth_date = 1990
# b_date = 1784
# info_msg = "Prašome įvesti vardą."
#
# print(vardas + " " + pavarde)
# print("Vartotojo vardas yra " + vardas + " " + pavarde +
#       ". Jis yra gimęs " + str(birth_date) + " metais." )

# print(5 + 18)
# print("5" + "18")
#
# print("labas rytas")
#
# rekordas = 412
# print("2025-02-25 11:44 rekordas yra: " + str(rekordas))
#
# rekordas = 418
# print("2025-02-25 11:46 rekordas yra: " + str(rekordas))
#
# birth_year = 1990
# current_year = 2025
#
# print("Vartotojui yra " + str(current_year - birth_year) + " metai." )
# print(str(current_year - birth_year) + " metai yra vartotojo amžius" )


# print(datetime.now())

# ========================================================================

# if 5 > 3:
#     print("5 > 3")
#     print(":)")
# else:
#     print("5 !> 3")


# pazymys = 8
#
# if pazymys == 10:
#     print("auksciausias ivertinimas")
# else:
#     print("yra kur tobuleti")


# pazymys = 3
#
# if pazymys == 10:
#     print("auksciausias ivertinimas")
# elif pazymys >= 8: # else if (kitu atveju jeigu salyga patenkinama)
#     print('labai gerai')
# elif pazymys >= 7:
#     print("neblogai")
# elif pazymys >= 4:
#     print("teigiamas")
# # else:
# #     print("reikes perlaikyti egzamina")
# elif pazymys <= 3:
#     print("reikes perlaikyti egzamina")
#
#
#
# print("zemiau salyginio sakinio")
#
#
# pazymys = 8
#
# if pazymys < 9 and pazymys > 7:
#     print("greiciausiai yra 8")
# if 7 < pazymys < 9: #daugiau uz 7 bet maziau uz 9
#     print("greiciausiai yra 8")

print("hi")




pazymys = 10

if pazymys == 10:
    print("auksciausias ivertinimas")

if 10 > pazymys >= 8: # else if (kitu atveju jeigu salyga patenkinama)
    print('labai gerai')

if 8 > pazymys >= 7:
    print("neblogai")

if 7 > pazymys >= 4:
    print("teigiamas")

if pazymys <= 3:
    print("reikes perlaikyti egzamina")


temperatura = -5
krituliai = "nera"
vejas = 5

if temperatura <= 0:
    if krituliai == "sninga":
        print("sedesiu namie")
    else:
        print("apsirengsiu siltai ir eisiu pasivaikscioti")
else:
    if krituliai != "lija":
        print("eisiu pabegiot")
    else:
        print("isitaysisiu patogiai lovoj ir klausysiuos lietaus :)")

print(random.randint(0,4))

atsitiktinis_sk1 = random.randint(0,4)
atsitiktinis_sk2 = random.randint(0,4)

print("atsitiktines reiksmes yra " + str(atsitiktinis_sk1) + " , " + str(atsitiktinis_sk2))


starWars = "Star Wars: Episode " + (" " * random.randint(1, 9)) + str(random.randint(1, 7)) + " - A New Hope"
print(starWars)

var = "labas vakaras :)"

var = "labas vakaras :)"

var = "labas vakaras :)"

var = "labas vakaras :)"
print("hihihi")
