# در این بخش کاربر جمله را وارد میکند و بررسی می شود ایا یک جمله وارد شده یا خیر
sentence = input("Input: ")
splite_sentence = sentence.strip() # چون ممکن بود کاربر ابتدا یک فاصله زده و بعدش فقط یک کلمه بزند پس از ابتدا و انتها فاصله ها حذف شد
if  " " not in splite_sentence:
    print("Warning!!!!!!! your sentence is not correct. you write just one word or if you write a sentence please use space between your word")

else:
    splite_sentence = sentence.split()

    
# دیکشنری که تعداد هر کلمه را نگه میدارد
repetition_of_word = {}

for word in splite_sentence:
    if word in repetition_of_word:
        repetition_of_word[word] +=1
    else:
        repetition_of_word [word] = 1
# print(repetition_of_word)

# کلمات منحصر به فرد را چاپ میکند
for  word , repetition in (repetition_of_word.items()):
    print(f"{word} : {repetition}")