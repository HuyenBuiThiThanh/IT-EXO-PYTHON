# 20/11/2023
# var1 = 1
# var2 = 2
# # for i in[0,1,2,3]:
# #     print("i a pour vqleur", i)

# # for i in range(10):
# #     print(i)

# tom ="bonjour"
# mot = ""
# count_length=len(tom)
# for i in range (count_length):
#     last_char = tom[count_length - 1 -i]
#     mot = mot + last_char
# print(mot)


# # Calcul some des élément d'une liste

# array = [1, 2, 3, 4]
# total = 0
# nom_tableau = len(array)
# i = 0

# while i < nom_tableau:
#     total = total + array[i]
#     i = i + 1

# print(total)

# 21/11/2023
array1 = [10,25,23,64,59]
total =0
# for i in range(len(array1)):
#     print(array1[i])

# for i in array1:
#     print(i)

# for var in array1:
#     total += var
# print(total)

# for var in array1:
#     for var in array1:
#         print(var)
#         total = total + var
# print(total)

# array1= [10,25,23,64,59]
# total =0
# for var in range(len(array1)):
#     total = total + array1[var]
# print(total)

# Recherche du plus grand nombre dans ce tableau
# tableau =[3,58,11,21]

# valeur_max = 0
# for i in range(len(tableau)):
#     if tableau[i] >= valeur_max:
#         valeur_max = tableau[i]
# print(valeur_max)


# Fonction qui calcule la factorielle d'un nombre

# number = 5
# factorielle =1
# i=1
# while i <=  number:
#     factorielle=i * factorielle
#     i=i+1
# print(factorielle)


# number = 5
# result =1
# for i in range(number+1):
#     if i> 0:
#         result=result*i       
# print(result)


# number = 5
# result = number
# for i in range(number):
#     if i> 0:
#         result=result* (number -i) 
# print(result)

# # verifier un palindrome
# var = "radar"
# sortie = "true"


# def comparer1(var):
#     result = ""
#     length = len(var)
#     for i in range(length):
#         result = result + var[length - i - 1]
#     if var == result: 
#         print(True)
#     else:
#         print(False)
    
# comparer1("HUHUH")


# def  comparer2(var):
#     length = len(var) // 2
#     i = 0
#     while i <= length:
#         if var[i] == var [len(var) -i - 1]:
#             i = i + 1
#             if i == length:
#                 print(True)
#         else:
#             print(False)
#             break

# comparer2("HUHUHUHUH")


# entree = "bonjour"
# list_entree =  list(entree)


resul = "bonj"
retour ="ltotll"

def checkresul(resul,retour):
    if resul == retour:
         return True
    else:
        return False
    return 
checkresul(resul,retour) 
if checkresul(resul,retour):
    print(checkresul(resul,retour))




