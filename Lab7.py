#    CS 2302 Data Structures
#    Professor Diego Aguirre
#    TA  Anindita Nath
#    Lab 7 option B
#    12/09/2018 by Edgar Escobedo 80502432

#The purpose of this lab is to create the method edit distance which would give as result the minumum amount of changes (between erasing a letter, adding a letter
#or swaping a letter) to change a string 1, to a string 2 or viceversa. In order to do so, I applied the idea of the matrix which we learned in class,this idea being
#of usig a matrix with the properties of having the number of rows equal to the length of the string 1 plus 1, and the number of the columns would be the length of the string 2
#plus 1 as well. The plus 1 being the space of am "empty" string. Then we would will the first column (converting the whole string 1 to an "empty" string
#and then the first row (converting the "empty" string 2 tp the string 1) or viceversa. Finally we will assign a number to each of the other empty matrix space
#holders, by first checking, if the 2 letters being check are equal, if they are, we pass the value in the diagonal, if they are not, we get the smallest value of the
#adjacent spaces. In the end we get the value at the last row and column and that would be the smallest amount of changes it took to transform it


def edit_distance(word_1, word_2):
    comp_table = {}
    rows = len(word_1) + 1
    columns = len(word_2) + 1

    for i in range(rows):
        comp_table[i, 0] = i                #setting values for first row and column
    for j in range(columns):
        comp_table[0, j] = j
    for i in range(1, rows):
        for j in range(1, columns):
            if word_1[i-1] == word_2[j-1]:      #If letters are the same, value equal to 0, diagonal value passed
                value = 0
            else:
                value = 1
            bottom_left = comp_table[i, j-1] + 1        #Checking for lowest value on adjacent spaces
            bottom_right = comp_table[i-1, j-1] + value
            upper_right = comp_table[i-1, j] + 1
            lowest_value = min(bottom_left, bottom_right, upper_right)
            comp_table[i , j] = lowest_value                #lowest value at the end of the rows and columns

    return comp_table[i,j]


#Regular file reader which will separate the words of the file and use them to check the amount of changes needed

file_name = input("Please select the name of the file you want to use\n")

with open(file_name+".txt") as f:
    passwords_list = f.read().splitlines()
counter = 0
while (counter != len(passwords_list)):
    list_x = passwords_list[counter]
    wrds = list_x.split(",")
    counter2 = 0
    show_line = []
    while (counter2 != len(wrds)):
        wrds[counter2] = wrds[counter2].replace(" ", "")
        if wrds[counter2] is not "":
            if counter2 == 0:
                x = wrds[counter2]
            else:
                y = wrds[counter2]
        counter2 += 1
    print("The two words in the line number "+str(counter + 1)+" needed "+str(edit_distance(x, y))+" changes in order to transform them")
    counter +=1

