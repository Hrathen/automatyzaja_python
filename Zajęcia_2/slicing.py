#Za pomocą string slicing wytnij ze zdań słowo “love”
#a. Love hurts
#b. I love you
#c. All you need is love!
#(użyj ujemnych indeksów)


txt1 = "Love hurts"
txt_new = txt1[0:5]
print(txt_new)

txt2 = "I love you"
txt_new2 = txt2[2:6]
print(txt_new2)

txt3 = "All you need is love!"
txt_new3 = txt3[-5:-1]
print(txt_new3)