#   Fernando Serrano, Instructor: Diego Aguirre, T.A.: Anindita Nath, 12/13/2018, CS 2302 DataStructures
#   This program is created to be able to determine the smallest amount of changes that need to be done
#   to two words in order to rewrite them to the same word. This is done with a matrix to store the value
#   of editing the letter and determines the value of the current change depending if the letters are similar;
#   storing the diagonal value in this location. The other change would be if the letters are different;
#   storing the min value of the locations preceding it and adding 1.


def edit_Distance(word1, word2):
    dis = []

    for i in range(len(word1) + 1):
        dis.append([0]*(len(word2) + 1))

    i = 1
    j = 1
    while i <= len(word1) or j <= len(word2):
        if i <= len(word1):
            dis[i][0] = i
            i += 1
        if j <= len(word2):
            dis[0][j] = j
            j += 1

    for i in range(1, len(dis)):
        for j in range(1, len(dis[i])):
            if word1[i - 1] == word2[j - 1]:
                dis[i][j] = dis[i - 1][j - 1]
            else:
                dis[i][j] = min(dis[i-1][j], dis[i][j-1], dis[i-1][j-1])+1

    print("word1 " + word1, "word2 " + word2)
    for i in range(len(dis)):
        for j in range(len(dis[i])):
            print(dis[i][j], end = " ")
        print()
    print()


# edit_Distance("crab", "ran")
