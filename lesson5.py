

### Excercise Set 1 ###

def file_capitalize(in_file, out_file):
    with open(in_file, "r", newline="\n") as fni, open(out_file, "w") as fno:
        for lines in fni.readlines():
            lines = lines.replace(".", "").replace("!", "").replace("-", "").replace(",", "").strip().lower().capitalize()
            lines = lines.replace("'merica", "'Merica")
            fno.write(lines + "\n")

        fni.close()
        fno.close()


### Excercise Set 2 ###

def file_word_count(file_name):
    word_cnt = {}
    with open(file_name, "r") as fn:
        for lines in fn.readlines():
            lines = lines.replace(".", "").replace("!", "").replace("-", "").replace(",", "").strip().lower()
            for word in lines.split():
                if word not in word_cnt:
                    word_cnt[word] = 0
                word_cnt[word] += 1
        fn.close()
    print(word_cnt)


### Exercise Set 3 ### (extra credit)

def word_count_file(in_file, out_file):
    word_cnt = {}
    with open(in_file, "r") as fni, open(out_file, "w") as fno:
        for lines in fni.readlines():
            lines = lines.replace(".", "").replace("!", "").replace("-", "").replace(",", "").strip().lower()
            for word in lines.split():
                if word not in word_cnt:
                    word_cnt[word] = 0
                word_cnt[word] += 1
        for item, val in word_cnt.items():
            fno.write(str(item) + ": " + str(val) + "\n")

        fni.close()
        fno.close()
    

if __name__=='__main__':
    #file_capitalize("sonnet.txt", "sonnetout.txt")
    #file_word_count("sonnet.txt")
    #word_count_file("sonnet.txt", "wordcount.txt")