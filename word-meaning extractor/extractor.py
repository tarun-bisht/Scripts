import sys
import os
def file_open(path):
    try:
        data=[]
        with open(path,'r',encoding='utf-8') as file:
            data=file.read().strip().split('\n')
        return data
    except Exception as e:
        print(f'Something went wrong:: Error: {e}')
def create_files(data,file1_name,file2_name):
    n=len(data)
    print("DATA LENGTH: ",n)
    words=[data[i] for i in range(0,n,2)]
    meanings=[data[i] for i in range(1,n,2)]
    print("NUMBER OF WORDS: ",len(words))
    print("NUMBER OF MEANINGS: ",len(meanings))
    try:
        with open(f'{file1_name}.txt','w',encoding='utf-8') as file:
            for i in words:
                file.write(i+"\n")
        print("::WORDS FILE CREATED::")
        with open(f'{file2_name}.txt','w',encoding='utf-8') as file:
            for i in meanings:
                file.write(i+"\n")
        print("::MEANINGS FILE CREATED::")
    except Exception as e:
        print(f'Something went wrong CANNOT CREATE FILES:: Error: {e}')
        print("\t::::WORDS::::")
        for i in words:
            print(i)
        print("\t--------------------------------------------------------------")
        print("\t::::MEANINGS::::")
        for i in meanings:
            print(i)
def upper(data,file_name):
    n=len(data)
    print("DATA LENGTH: ",n)
    try:
        with open(f'{file_name}.txt','w',encoding='utf-8') as file:
            for i in data:
                file.write(i.upper()+"\n")
        print("::FILE CREATED::")
    except Exception as e:
        print(f'Something went wrong CANNOT CREATE FILES:: Error: {e}')
        print("::::FILE::::")
        print("\t--------------------------------------------------------------")
        for i in data:
            print(i.upper())
def lower(data,file_name):
    n=len(data)
    print("DATA LENGTH: ",n)
    try:
        with open(f'{file_name}.txt','w',encoding='utf-8') as file:
            for i in data:
                file.write(i.lower()+"\n")
        print("::FILE CREATED::")
    except Exception as e:
        print(f'Something went wrong CANNOT CREATE FILES:: Error: {e}')
        print("\t::::FILE::::")
        print("\t--------------------------------------------------------------")
        for i in data:
            print(i.lower())
def sort_words(data,file_name):
    n=len(data)
    print("DATA LENGTH: ",n)
    data=insertion_sort(data)
    try:
        with open(f'{file_name}.txt','w',encoding='utf-8') as file:
            for i in data:
                file.write(i+"\n")
        print("::FILE CREATED::")
        for i in data:
            print(f"{i} : {len(i)}")
    except Exception as e:
        print(f'Something went wrong CANNOT CREATE FILES:: Error: {e}')
        print("\t::::FILE::::")
        print("\t--------------------------------------------------------------")
        for i in data:
            print(i)
def sort_words_meanings(words,meanings,file1_name,file2_name):
    words,meanings=word_sort_map_meaning(words,meanings)
    try:
        with open(f'{file1_name}.txt','w',encoding='utf-8') as file:
            for i in words:
                file.write(i+"\n")
        print("::WORDS FILE CREATED::")
        with open(f'{file2_name}.txt','w',encoding='utf-8') as file:
            for i in meanings:
                file.write(i+"\n")
        print("::MEANINGS FILE CREATED::")
    except Exception as e:
        print(f'Something went wrong CANNOT CREATE FILES:: Error: {e}')
        print("\t::::WORDS::::")
        for i in words:
            print(i)
        print("\t--------------------------------------------------------------")
        print("\t::::MEANINGS::::")
        for i in meanings:
            print(i)
def word_sort_map_meaning(words,meanings):
    n=len(words)
    for i in range(1,n):
        key=len(words[i])
        str_key=words[i]
        str_meaning=meanings[i]
        j=i-1
        while j>=0 and len(words[j])>key:
            words[j+1]=words[j]
            meanings[j+1]=meanings[j]
            j=j-1
        words[j+1]=str_key
        meanings[j+1]=str_meaning
    return (words,meanings)
def insertion_sort(data):
    n=len(data)
    for i in range(1,n):
        key=len(data[i])
        str_key=data[i]
        j=i-1
        while j>=0 and len(data[j])>key:
            data[j+1]=data[j]
            j=j-1
        data[j+1]=str_key
    return data
def main():
    terms=sys.argv
    path=function=new_file=""
    if len(terms)<2:
        path=os.getcwd()
        filename=input("Enter File Name::=> ")
        path=os.path.join(path,filename)
    elif len(terms)==2:
        path=terms[1]
        filename=input("Enter File Name::=> ")
        path=os.path.join(path,filename)
    elif len(terms)>=3:
        path=terms[1]
        filename=terms[2]
        path=os.path.join(path,filename)
        try:
            function=terms[4]
        except IndexError:
            function=""
        try:
            new_file=terms[5]
        except IndexError:
            new_file=input("Enter File Name to create: ")
    try:
        data=file_open(path)
        if not data == None:
            if function=="new":
                try:
                    file2_name=terms[6]
                except IndexError:
                    file2_name=input("Enter Meaning File Name to create: ")
                create_files(data,new_file,file2_name)
            elif function=="upper":
                upper(data,new_file)
            elif function=="lower":
                lower(data,new_file)
            elif function=="sort":
                sort_words(data,new_file)
            elif function=="sort_words_meanings":
                try:
                    file2_name=terms[6]
                except IndexError:
                    file2_name=input("Enter Meaning File Name to create: ")
                path1=input("Enter Word File Path::=> ")
                path2=input("Enter Meaning File Path::=> ")
                words=file_open(path1)
                meanings=file_open(path2)
                sort_words_meanings(words,meanings,new_file,file2_name)
            else:
                print("Define Functionality: ")
                print('''
                1=> Press 1 to create word meaning file from a file
                2=> Press 2 to upper the text in file
                3=> Press 3 to lower the text in file
                4=> Press 4 to Sort Words according to Length
                5=> Press 5 to sort and map Words and Meanings''')
                choice=input("Enter your Choice: ")
                if choice=='1':
                    try:
                        file2_name=terms[6]
                    except IndexError:
                        file2_name=input("Enter Meaning File Name to create: ")
                    create_files(data,new_file,file2_name)
                elif choice=='2':
                    upper(data,new_file)
                elif choice=='3':
                    lower(data,new_file)
                elif choice=='4':
                    sort_words(data,new_file)
                elif choice=='5':
                    try:
                        file2_name=terms[6]
                    except IndexError:
                        file2_name=input("Enter Meaning File Name to create: ")
                    path1=input("Enter Word File Path::=> ")
                    path2=input("Enter Meaning File Path::=> ")
                    words=file_open(path1)
                    meanings=file_open(path2)
                    sort_words_meanings(words,meanings,new_file,file2_name)
                else:
                    print("No Functionality Defined")
    except Exception as e:
        print(f"ERROR:: Something went wrong:: {e}")
if __name__=="__main__":
    main()
