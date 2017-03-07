import re

s = "(aasdf)[,\s]*(basdfa)"

text = """

asdfasdfkj  asadfasdf
asdf
asdf
as
df  a   b
 asdf  asdf asdf a sfd asf a,b

 asdfasdf
 as
 fasd
 f
 asdf             asdfas df asfd asd fas dfa sdf asdf
  asdfasdf  asdf asdf a,    b asdfasdf

asdf
asdfasdfasdf  asdfasdf   asdf as df asdf as dfa sdf asdf as dfa sdf af da fd asfd as dfas df asdf afd  a asdf asdf as dfasdf a
asdfasdfasdf  asdfasdf   asdf as df asdf as dfa sdf asdf as dfa sdf af da fd asfd as dfas df asdf afd  a asdf asdf as dfasdf a
asdfasdfasdf  asdfasdf   asdf as df asdf as dfa sdf asdf as dfa sdf af da fd asfd as dfas df asdf afd  a asdf asdf as dfasdf a
asdfasdfasdf  asdfasdf   asdf as df asdf as dfa sdf asdf as dfa sdf af da fd asfd as dfas df asdf afd  a asdf asdf as dfasdf a
asdfasdfasdf  asdfasdf   asdf as df asdf as dfa sdf asdf as dfa sdf af da fd asfd as dfas df asdf afd  a asdf asdf as dfasdf a
asdfasdfasdf  asdfasdf   asdf as df asdf as dfa sdf asdf as dfa sdf af da fd asfd as dfas df asdf afd  a asdf asdf as dfasdf a
asdfasdfasdf  asdfasdf   asdf as df asdf as dfa sdf asdf as dfa sdf af da fd asfd as dfas df asdf afd  a asdf asdf as dfasdf a
asdfasdfasdf  asdfasdf   asdf as df asdf as dfa sdf asdf as dfa sdf af da fd asfd as dfas df asdf afd  a asdf asdf as dfasdf a
asdfasdfasdf  asdfasdf   asdf as df asdf as dfa sdf asdf as dfa sdf af da fd asfd as dfas df asdf afd  a asdf asdf as dfasdf a
asdfasdfasdf  asdfasdf   asdf as df asdf as dfa sdf asdf as dfa sdf af da fd asfd as dfas df asdf afd  a asdf asdf as dfasdf a
asdfasdfasdf  asdfasdf   asdf as df asdf as dfa sdf asdf as dfa sdf af da fd asfd as dfas df asdf afd  a asdf asdf as dfasdf a
asdfasdfasdf  asdfasdf   asdf as df asdf as dfa sdf asdf as dfa sdf af da fd asfd as dfas df asdf afd  a asdf asdf as dfasdf a
df  a   b
 asdf  asdf asdf a sfd asf a,b

 asdfasdf
 as
 fasd
 f
 asdf             asdfas df asfd asd fas dfa sdf asdf
  asdfasdf  asdf asdf a,    b asdfasdf

asdf
asdfasdfasdf  asdfasdf   asdf as df asdf as dfa sdf asdf as dfa sdf af da fd asfd as dfas df asdf afd  a asdf asdf as dfasdf a
asdfasdfasdf  asdfasdf   asdf as df asdf as dfa sdf asdf as dfa sdf af da fd asfd as dfas df asdf afd  a asdf asdf as dfasdf a
asdfasdfasdf  asdfasdf   asdf as df asdf as dfa sdf asdf as dfa sdf af da fd asfd as dfas df asdf afd  a asdf asdf as dfasdf a
asdfasdfasdf  asdfasdf   asdf as df asdf as dfa sdf asdf as dfa sdf af da fd asfd as dfas df asdf afd  a asdf asdf as dfasdf a
asdfasdfasdf  asdfasdf   asdf as df asdf as dfa sdf asdf as dfa sdf af da fd asfd as dfas df asdf afd  a asdf asdf as dfasdf a
asdfasdfasdf  asdfasdf   asdf as df asdf as dfa sdf asdf as dfa sdf af da fd asfd as dfas df asdf afd  a asdf asdf as dfasdf a
asdfasdfasdf  asdfasdf   asdf as df asdf as dfa sdf asdf as dfa sdf af da fd asfd as dfas df asdf afd  a asdf asdf as dfasdf a
asdfasdfasdf  asdfasdf   asdf as df asdf as dfa sdf asdf as dfa sdf af da fd asfd as dfas df asdf afd  a asdf asdf as dfasdf a
asdfasdfasdf  asdfasdf   asdf as df asdf as dfa sdf asdf as dfa sdf af da fd asfd as dfas df asdf afd  a asdf asdf as dfasdf a
asdfasdfasdf  asdfasdf   asdf as df asdf as dfa sdf asdf as dfa sdf af da fd asfd as dfas df asdf afd  a asdf asdf as dfasdf a
asdfasdfasdf  asdfasdf   asdf as df asdf as dfa sdf asdf as dfa sdf af da fd asfd as dfas df asdf afd  a asdf asdf as dfasdf a
asdfasdfasdf  asdfasdf   asdf as df asdf as dfa sdf asdf as dfa sdf af da fd asfd as dfas df asdf afd  a asdf asdf as dfasdf a
df  a   b
 asdf  asdf asdf a sfd asf a,b

 asdfasdf
 as
 fasd
 f
 asdf             asdfas df asfd asd fas dfa sdf asdf
  asdfasdf  asdf asdf a,    b asdfasdf

asdf
asdfasdfasdf  asdfasdf   asdf as df asdf as dfa sdf asdf as dfa sdf af da fd asfd as dfas df asdf afd  a asdf asdf as dfasdf a
asdfasdfasdf  asdfasdf   asdf as df asdf as dfa sdf asdf as dfa sdf af da fd asfd as dfas df asdf afd  a asdf asdf as dfasdf a
asdfasdfasdf  asdfasdf   asdf as df asdf as dfa sdf asdf as dfa sdf af da fd asfd as dfas df asdf afd  a asdf asdf as dfasdf a
asdfasdfasdf  asdfasdf   asdf as df asdf as dfa sdf asdf as dfa sdf af da fd asfd as dfas df asdf afd  a asdf asdf as dfasdf a
asdfasdfasdf  asdfasdf   asdf as df asdf as dfa sdf asdf as dfa sdf af da fd asfd as dfas df asdf afd  a asdf asdf as dfasdf a
asdfasdfasdf  asdfasdf   asdf as df asdf as dfa sdf asdf as dfa sdf af da fd asfd as dfas df asdf afd  a asdf asdf as dfasdf a
asdfasdfasdf  asdfasdf   asdf as df asdf as dfa sdf asdf as dfa sdf af da fd asfd as dfas df asdf afd  a asdf asdf as dfasdf a
asdfasdfasdf  asdfasdf   asdf as df asdf as dfa sdf asdf as dfa sdf af da fd asfd as dfas df asdf afd  a asdf asdf as dfasdf a
asdfasdfasdf  asdfasdf   asdf as df asdf as dfa sdf asdf as dfa sdf af da fd asfd as dfas df asdf afd  a asdf asdf as dfasdf a
asdfasdfasdf  asdfasdf   asdf as df asdf as dfa sdf asdf as dfa sdf af da fd asfd as dfas df asdf afd  a asdf asdf as dfasdf a
asdfasdfasdf  asdfasdf   asdf as df asdf as dfa sdf asdf as dfa sdf af da fd asfd as dfas df asdf afd  a asdf asdf as dfasdf a
asdfasdfasdf  asdfasdf   asdf as df asdf as dfa sdf asdf as dfa sdf af da fd asfd as dfas df asdf afd  a asdf asdf as dfasdf a
df  a   b
 asdf  asdf asdf a sfd asf a,b

 asdfasdf
 as
 fasd
 f
 asdf             asdfas df asfd asd fas dfa sdf asdf
  asdfasdf  asdf asdf a,    b asdfasdf

asdf
asdfasdfasdf  asdfasdf   asdf as df asdf as dfa sdf asdf as dfa sdf af da fd asfd as dfas df asdf afd  a asdf asdf as dfasdf a
asdfasdfasdf  asdfasdf   asdf as df asdf as dfa sdf asdf as dfa sdf af da fd asfd as dfas df asdf afd  a asdf asdf as dfasdf a
asdfasdfasdf  asdfasdf   asdf as df asdf as dfa sdf asdf as dfa sdf af da fd asfd as dfas df asdf afd  a asdf asdf as dfasdf a
asdfasdfasdf  asdfasdf   asdf as df asdf as dfa sdf asdf as dfa sdf af da fd asfd as dfas df asdf afd  a asdf asdf as dfasdf a
asdfasdfasdf  asdfasdf   asdf as df asdf as dfa sdf asdf as dfa sdf af da fd asfd as dfas df asdf afd  a asdf asdf as dfasdf a
asdfasdfasdf  asdfasdf   asdf as df asdf as dfa sdf asdf as dfa sdf af da fd asfd as dfas df asdf afd  a asdf asdf as dfasdf a
asdfasdfasdf  asdfasdf   asdf as df asdf as dfa sdf asdf as dfa sdf af da fd asfd as dfas df asdf afd  a asdf asdf as dfasdf a
asdfasdfasdf  asdfasdf   asdf as df asdf as dfa sdf asdf as dfa sdf af da fd asfd as dfas df asdf afd  a asdf asdf as dfasdf a
asdfasdfasdf  asdfasdf   asdf as df asdf as dfa sdf asdf as dfa sdf af da fd asfd as dfas df asdf afd  a asdf asdf as dfasdf a
asdfasdfasdf  asdfasdf   asdf as df asdf as dfa sdf asdf as dfa sdf af da fd asfd as dfas df asdf afd  a asdf asdf as dfasdf a
asdfasdfasdf  asdfasdf   asdf as df asdf as dfa sdf asdf as dfa sdf af da fd asfd as dfas df asdf afd  a asdf asdf as dfasdf a
asdfasdfasdf  asdfasdf   asdf as df asdf as dfa sdf asdf as dfa sdf af da fd asfd as dfas df asdf afd  a asdf asdf as dfasdf a
df  a   b
 asdf  asdf asdf a sfd asf a,b

 asdfasdf
 as
 fasd
 f
 asdf             asdfas df asfd asd fas dfa sdf asdf
  asdfasdf  asdf asdf a,    b asdfasdf

asdf
asdfasdfasdf  asdfasdf   asdf as df asdf as dfa sdf asdf as dfa sdf af da fd asfd as dfas df asdf afd  a asdf asdf as dfasdf a
asdfasdfasdf  asdfasdf   asdf as df asdf as dfa sdf asdf as dfa sdf af da fd asfd as dfas df asdf afd  a asdf asdf as dfasdf a
asdfasdfasdf  asdfasdf   asdf as df asdf as dfa sdf asdf as dfa sdf af da fd asfd as dfas df asdf afd  a asdf asdf as dfasdf a
asdfasdfasdf  asdfasdf   asdf as df asdf as dfa sdf asdf as dfa sdf af da fd asfd as dfas df asdf afd  a asdf asdf as dfasdf a
asdfasdfasdf  asdfasdf   asdf as df asdf as dfa sdf asdf as dfa sdf af da fd asfd as dfas df asdf afd  a asdf asdf as dfasdf a
asdfasdfasdf  asdfasdf   asdf as df asdf as dfa sdf asdf as dfa sdf af da fd asfd as dfas df asdf afd  a asdf asdf as dfasdf a
asdfasdfasdf  asdfasdf   asdf as df asdf as dfa sdf asdf as dfa sdf af da fd asfd as dfas df asdf afd  a asdf asdf as dfasdf a
asdfasdfasdf  asdfasdf   asdf as df asdf as dfa sdf asdf as dfa sdf af da fd asfd as dfas df asdf afd  a asdf asdf as dfasdf a
asdfasdfasdf  asdfasdf   asdf as df asdf as dfa sdf asdf as dfa sdf af da fd asfd as dfas df asdf afd  a asdf asdf as dfasdf a
asdfasdfasdf  asdfasdf   asdf as df asdf as dfa sdf asdf as dfa sdf af da fd asfd as dfas df asdf afd  a asdf asdf as dfasdf a
asdfasdfasdf  asdfasdf   asdf as df asdf as dfa sdf asdf as dfa sdf af da fd asfd as dfas df asdf afd  a asdf asdf as dfasdf a
asdfasdfasdf  asdfasdf   asdf as df asdf as dfa sdf asdf as dfa sdf af da fd asfd as dfas df asdf afd  a asdf asdf as dfasdf a
df  a   b
 asdf  asdf asdf a sfd asf a,b

 asdfasdf
 as
 fasd
 f
 asdf             asdfas df asfd asd fas dfa sdf asdf
  asdfasdf  asdf asdf a,    b asdfasdf

asdf
asdfasdfasdf  asdfasdf   asdf as df asdf as dfa sdf asdf as dfa sdf af da fd asfd as dfas df asdf afd  a asdf asdf as dfasdf a
asdfasdfasdf  asdfasdf   asdf as df asdf as dfa sdf asdf as dfa sdf af da fd asfd as dfas df asdf afd  a asdf asdf as dfasdf a
asdfasdfasdf  asdfasdf   asdf as df asdf as dfa sdf asdf as dfa sdf af da fd asfd as dfas df asdf afd  a asdf asdf as dfasdf a
asdfasdfasdf  asdfasdf   asdf as df asdf as dfa sdf asdf as dfa sdf af da fd asfd as dfas df asdf afd  a asdf asdf as dfasdf a
asdfasdfasdf  asdfasdf   asdf as df asdf as dfa sdf asdf as dfa sdf af da fd asfd as dfas df asdf afd  a asdf asdf as dfasdf a
asdfasdfasdf  asdfasdf   asdf as df asdf as dfa sdf asdf as dfa sdf af da fd asfd as dfas df asdf afd  a asdf asdf as dfasdf a
asdfasdfasdf  asdfasdf   asdf as df asdf as dfa sdf asdf as dfa sdf af da fd asfd as dfas df asdf afd  a asdf asdf as dfasdf a
asdfasdfasdf  asdfasdf   asdf as df asdf as dfa sdf asdf as dfa sdf af da fd asfd as dfas df asdf afd  a asdf asdf as dfasdf a
asdfasdfasdf  asdfasdf   asdf as df asdf as dfa sdf asdf as dfa sdf af da fd asfd as dfas df asdf afd  a asdf asdf as dfasdf a
asdfasdfasdf  asdfasdf   asdf as df asdf as dfa sdf asdf as dfa sdf af da fd asfd as dfas df asdf afd  a asdf asdf as dfasdf a
asdfasdfasdf  asdfasdf   asdf as df asdf as dfa sdf asdf as dfa sdf af da fd asfd as dfas df asdf afd  a asdf asdf as dfasdf a
asdfasdfasdf  asdfasdf   asdf as df asdf as dfa sdf asdf as dfa sdf af da fd asfd as dfas df asdf afd  a asdf asdf as dfasdf a
df  a   b
 asdf  asdf asdf a sfd asf a,b

 asdfasdf
 as
 fasd
 f
 asdf             asdfas df asfd asd fas dfa sdf asdf
  asdfasdf  asdf asdf a,    b asdfasdf

asdf
asdfasdfasdf  asdfasdf   asdf as df asdf as dfa sdf asdf as dfa sdf af da fd asfd as dfas df asdf afd  a asdf asdf as dfasdf a
asdfasdfasdf  asdfasdf   asdf as df asdf as dfa sdf asdf as dfa sdf af da fd asfd as dfas df asdf afd  a asdf asdf as dfasdf a
asdfasdfasdf  asdfasdf   asdf as df asdf as dfa sdf asdf as dfa sdf af da fd asfd as dfas df asdf afd  a asdf asdf as dfasdf a
asdfasdfasdf  asdfasdf   asdf as df asdf as dfa sdf asdf as dfa sdf af da fd asfd as dfas df asdf afd  a asdf asdf as dfasdf a
asdfasdfasdf  asdfasdf   asdf as df asdf as dfa sdf asdf as dfa sdf af da fd asfd as dfas df asdf afd  a asdf asdf as dfasdf a
asdfasdfasdf  asdfasdf   asdf as df asdf as dfa sdf asdf as dfa sdf af da fd asfd as dfas df asdf afd  a asdf asdf as dfasdf a
asdfasdfasdf  asdfasdf   asdf as df asdf as dfa sdf asdf as dfa sdf af da fd asfd as dfas df asdf afd  a asdf asdf as dfasdf a
asdfasdfasdf  asdfasdf   asdf as df asdf as dfa sdf asdf as dfa sdf af da fd asfd as dfas df asdf afd  a asdf asdf as dfasdf a
asdfasdfasdf  asdfasdf   asdf as df asdf as dfa sdf asdf as dfa sdf af da fd asfd as dfas df asdf afd  a asdf asdf as dfasdf a
asdfasdfasdf  asdfasdf   asdf as df asdf as dfa sdf asdf as dfa sdf af da fd asfd as dfas df asdf afd  a asdf asdf as dfasdf a
asdfasdfasdf  asdfasdf   asdf as df asdf as dfa sdf asdf as dfa sdf af da fd asfd as dfas df asdf afd  a asdf asdf as dfasdf a
asdfasdfasdf  asdfasdf   asdf as df asdf as dfa sdf asdf as dfa sdf af da fd asfd as dfas df asdf afd  a asdf asdf as dfasdf a
df  a   b
 asdf  asdf asdf a sfd asf a,b

 asdfasdf
 as
 fasd
 f
 asdf             asdfas df asfd asd fas dfa sdf asdf
  asdfasdf  asdf asdf a,    b asdfasdf

asdf
asdfasdfasdf  asdfasdf   asdf as df asdf as dfa sdf asdf as dfa sdf af da fd asfd as dfas df asdf afd  a asdf asdf as dfasdf a
asdfasdfasdf  asdfasdf   asdf as df asdf as dfa sdf asdf as dfa sdf af da fd asfd as dfas df asdf afd  a asdf asdf as dfasdf a
asdfasdfasdf  asdfasdf   asdf as df asdf as dfa sdf asdf as dfa sdf af da fd asfd as dfas df asdf afd  a asdf asdf as dfasdf a
asdfasdfasdf  asdfasdf   asdf as df asdf as dfa sdf asdf as dfa sdf af da fd asfd as dfas df asdf afd  a asdf asdf as dfasdf a
asdfasdfasdf  asdfasdf   asdf as df asdf as dfa sdf asdf as dfa sdf af da fd asfd as dfas df asdf afd  a asdf asdf as dfasdf a
asdfasdfasdf  asdfasdf   asdf as df asdf as dfa sdf asdf as dfa sdf af da fd asfd as dfas df asdf afd  a asdf asdf as dfasdf a
asdfasdfasdf  asdfasdf   asdf as df asdf as dfa sdf asdf as dfa sdf af da fd asfd as dfas df asdf afd  a asdf asdf as dfasdf a
asdfasdfasdf  asdfasdf   asdf as df asdf as dfa sdf asdf as dfa sdf af da fd asfd as dfas df asdf afd  a asdf asdf as dfasdf a
asdfasdfasdf  asdfasdf   asdf as df asdf as dfa sdf asdf as dfa sdf af da fd asfd as dfas df asdf afd  a asdf asdf as dfasdf a
asdfasdfasdf  asdfasdf   asdf as df asdf as dfa sdf asdf as dfa sdf af da fd asfd as dfas df asdf afd  a asdf asdf as dfasdf a
asdfasdfasdf  asdfasdf   asdf as df asdf as dfa sdf asdf as dfa sdf af da fd asfd as dfas df asdf afd  a asdf asdf as dfasdf a
asdfasdfasdf  asdfasdf   asdf as df asdf as dfa sdf asdf as dfa sdf af da fd asfd as dfas df asdf afd  a asdf asdf as dfasdf a
df  a   b
 asdf  asdf asdf a sfd asf a,b

 asdfasdf
 as
 fasd
 f
 asdf             asdfas df asfd asd fas dfa sdf asdf
  asdfasdf  asdf asdf a,    b asdfasdf

asdf
asdfasdfasdf  asdfasdf   asdf as df asdf as dfa sdf asdf as dfa sdf af da fd asfd as dfas df asdf afd  a asdf asdf as dfasdf a
asdfasdfasdf  asdfasdf   asdf as df asdf as dfa sdf asdf as dfa sdf af da fd asfd as dfas df asdf afd  a asdf asdf as dfasdf a
asdfasdfasdf  asdfasdf   asdf as df asdf as dfa sdf asdf as dfa sdf af da fd asfd as dfas df asdf afd  a asdf asdf as dfasdf a
asdfasdfasdf  asdfasdf   asdf as df asdf as dfa sdf asdf as dfa sdf af da fd asfd as dfas df asdf afd  a asdf asdf as dfasdf a
asdfasdfasdf  asdfasdf   asdf as df asdf as dfa sdf asdf as dfa sdf af da fd asfd as dfas df asdf afd  a asdf asdf as dfasdf a
asdfasdfasdf  asdfasdf   asdf as df asdf as dfa sdf asdf as dfa sdf af da fd asfd as dfas df asdf afd  a asdf asdf as dfasdf a
asdfasdfasdf  asdfasdf   asdf as df asdf as dfa sdf asdf as dfa sdf af da fd asfd as dfas df asdf afd  a asdf asdf as dfasdf a
asdfasdfasdf  asdfasdf   asdf as df asdf as dfa sdf asdf as dfa sdf af da fd asfd as dfas df asdf afd  a asdf asdf as dfasdf a
asdfasdfasdf  asdfasdf   asdf as df asdf as dfa sdf asdf as dfa sdf af da fd asfd as dfas df asdf afd  a asdf asdf as dfasdf a
asdfasdfasdf  asdfasdf   asdf as df asdf as dfa sdf asdf as dfa sdf af da fd asfd as dfas df asdf afd  a asdf asdf as dfasdf a
asdfasdfasdf  asdfasdf   asdf as df asdf as dfa sdf asdf as dfa sdf af da fd asfd as dfas df asdf afd  a asdf asdf as dfasdf a
asdfasdfasdf  asdfasdf   asdf as df asdf as dfa sdf asdf as dfa sdf af da fd asfd as dfas df asdf afd  a asdf asdf as dfasdf a
df  a   b
 asdf  asdf asdf a sfd asf a,b

 asdfasdf
 as
 fasd
 f
 asdf             asdfas df asfd asd fas dfa sdf asdf
  asdfasdf  asdf asdf a,    b asdfasdf

asdf
asdfasdfasdf  asdfasdf   asdf as df asdf as dfa sdf asdf as dfa sdf af da fd asfd as dfas df asdf afd  a asdf asdf as dfasdf a
asdfasdfasdf  asdfasdf   asdf as df asdf as dfa sdf asdf as dfa sdf af da fd asfd as dfas df asdf afd  a asdf asdf as dfasdf a
asdfasdfasdf  asdfasdf   asdf as df asdf as dfa sdf asdf as dfa sdf af da fd asfd as dfas df asdf afd  a asdf asdf as dfasdf a
asdfasdfasdf  asdfasdf   asdf as df asdf as dfa sdf asdf as dfa sdf af da fd asfd as dfas df asdf afd  a asdf asdf as dfasdf a
asdfasdfasdf  asdfasdf   asdf as df asdf as dfa sdf asdf as dfa sdf af da fd asfd as dfas df asdf afd  a asdf asdf as dfasdf a
asdfasdfasdf  asdfasdf   asdf as df asdf as dfa sdf asdf as dfa sdf af da fd asfd as dfas df asdf afd  a asdf asdf as dfasdf a
asdfasdfasdf  asdfasdf   asdf as df asdf as dfa sdf asdf as dfa sdf af da fd asfd as dfas df asdf afd  a asdf asdf as dfasdf a
asdfasdfasdf  asdfasdf   asdf as df asdf as dfa sdf asdf as dfa sdf af da fd asfd as dfas df asdf afd  a asdf asdf as dfasdf a
asdfasdfasdf  asdfasdf   asdf as df asdf as dfa sdf asdf as dfa sdf af da fd asfd as dfas df asdf afd  a asdf asdf as dfasdf a
asdfasdfasdf  asdfasdf   asdf as df asdf as dfa sdf asdf as dfa sdf af da fd asfd as dfas df asdf afd  a asdf asdf as dfasdf a
asdfasdfasdf  asdfasdf   asdf as df asdf as dfa sdf asdf as dfa sdf af da fd asfd as dfas df asdf afd  a asdf asdf as dfasdf a
asdfasdfasdf  asdfasdf   asdf as df asdf as dfa sdf asdf as dfa sdf af da fd asfd as dfas df asdf afd  a asdf asdf as dfasdf a


"""
s2="'"
for i in range(1,200) :
    s2 += "|" + s +str(i)


s2 = s2[1:]
import time
start = time.time()
for i in range(1,200) :
    p = re.compile(s, flags=re.IGNORECASE)

    p.findall(text)

print("elapsed ", time.time() - start)