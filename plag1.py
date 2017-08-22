from difflib import SequenceMatcher
with open('1.txt') as file_1,open('2.txt') as file_2:
    file1_data = file_1.read()
    file2_data = file_2.read()
    similarity_ratio = SequenceMatcher(None,file1_data,file2_data)
    print (similarity_ratio.ratio()*100)