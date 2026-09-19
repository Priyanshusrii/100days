def caes(text,shift,mode):
    if mode.lower()=="encrypt":
        result=""
        for t in text:
                if t==" ":
                   result+=" "
                   continue     
                
                tt=ord(t)
                tt-=ord("a")
                tt+=shift
                tt%=26
                tt+=ord("a")
                res=chr(tt)
                result+=res
                

        return result
    elif mode.lower()=="decrypt":
        result=""
        for t in text:
              if t==" ":
                   result+=" "
                   continue
              tt=ord(t)
              tt-=ord("a")
              tt-=shift
              tt%=26
              tt+=ord("a")
              res=chr(tt)
              result+=res
        return result
    else:
         return

while True:
    text=input("Enter text or exit\n")
    if text.lower()=="exit":
             break
    shift=int(input("Enter shift\n"))
    mode=input("Select mode encrypt/decrypt\n")
    result=caes(text,shift,mode)
    print(result )
   

    