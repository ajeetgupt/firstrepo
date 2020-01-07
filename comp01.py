test_cases=int(input())
for t in range(test_cases):
    c= int(input())
    dic={}
    list_of_key=[]
    while c>0:
        inputs = list(map(str,input().split()))
        if inputs[0]=='top':
            list_of_tuple=sorted(dic.items(), key=lambda x: x[1], reverse=True)
            list_of_tuple=dict(list_of_tuple)
            first_key=list(list_of_tuple.keys())[0]
            maxval=list_of_tuple[first_key]
#             print(maxval)
            for k in list_of_tuple.keys():
                if list_of_tuple[k]==maxval:
                    list_of_key.append(k)
                else:
                    break                    
            ss=sorted(list_of_key)
            listToStr = ' '.join([str(elem) for elem in ss])
            print(listToStr)
            list_of_key.clear()
        else:
            p=inputs[0]
            u=int(inputs[1])
            if p in dic:
                dic[p]+=u
            else:
                dic[p]=u
#             print(dic)
        c-=1       