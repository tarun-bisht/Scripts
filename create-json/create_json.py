def create_json(a,b):
    try:
        json_list=list(zip(a,b))
        json=[]
        for j in json_list:
            jstr=str("\""+j[0]+"\""+" : "+"\""+str(j[1])+"\"")
            json.append(jstr)
        name=input("Enter json file name to create or override:: ")+'.json'
        json_string=""
        with open(name,'w',encoding='utf-8') as file:
            json_string+="{\n"
            for j in range(len(json)):
                if j <len(json)-1:
                    json_string+="\t"+json[j]+",\n"
                else:
                    json_string+="\t"+json[j]+"\n"
            json_string+="}"
            file.write(json_string)
        print("JSON CREATION SUCCESS")
    except Exception as e:
        print(f'Something went wrong:: Error: {e}')
def file_open(path):
    try:
        import codecs
        f=[]
        with codecs.open(path,'r',encoding='utf-8') as file:
            f=file.read().strip().split('\r\n')
        return f
    except Exception as e:
        print(f'Something went wrong:: Error: {e}')
def main():
    try:
        path=input("Enter File Path (will be used as key of json):: ")
        f_1=file_open(path)
        path=input("Enter File Path (will be used as value of json):: ")
        f_2=file_open(path)
        if not f_1==None and not f_2==None:
            create_json(f_1,f_2)
    except Exception as e:
        print(f'Something went wrong:: Error: {e}')
if __name__=="__main__":
    main()
