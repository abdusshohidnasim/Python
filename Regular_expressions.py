import re

pattern = r"colour"
if re.search(pattern, "The colour of the sky is blue"):
    print("Match found")
else: 
    print("Match not found")


if re.match(pattern, "colour of the sky is blue"):
    print("Match found")
else: 
    print("Match not found")

li = re.findall(pattern, "The colour of the sky is blue and the colour of the grass is green")
print(li)

# more scarch funtion 
pat = r"Naiem"
text = "My name is Naiem and Naiem is a good boy and Naiem is a student."
moreobj = re.search(pat, text)
if moreobj:
    print(moreobj.start())
    print(moreobj.end())
    print(moreobj.span())


# Search And Replace
repless = r"Naiem"
repl = "Nasim"
newtext = re.sub(repless, repl, text,count=8)
print(newtext)

# Meta Characters
print("____________________________________\"Meta Characters\"____________________________________")

ma = r"^Na..m$" # ^ this simibme name is tope simble. and thiks simble is working is frist a match korta hoba $ ar ai chinno ar aga hola oi latter ta sasa thakta hoba 
if re.match(ma, "Naiem"):
    print("Match found")
else: 
    print("Match not found")

print("____________________________________\"Meta Characters astic simple\"____________________________________")
# * this simble name astic simple  
# * thik simble minig is 0 or more . mining is thks text fount and not fount print true 
n = r"a*"
m = r"(ab)*"
if re.match(n,"colors"):
    print("match")
else:
    print("Not match")

#  + thik simble minig is 1 or more , mining minimum 1 valu requerd in stiging moro and more valu dont match 
plass = r"a+"
if re.match(plass,"colors"):
    print("Match a")
else:
    print("not match a +")

doubleolass = r"a+b"
# ar mining hoilo ja a ar  pora obossoi b thakta hoba

if re.match(plass,"abcolors"):
    print("Match ab")
else:
    print("not match ab+")

doubleolass = r"a+b"

# ? ar mininig holo ja 0 or 1 thakaba parba 
exp = r"isc(-)?reem"
if re.match(exp,"iscreem"):
    print("Match iscreem")
else:
    print("not match iscreem")

doubleolass = r"a+b"

print("____________________________________\"Meta Characters carle bracked \"____________________________________")

carli = r"a{1,3}"
exp = r"isc(-)?reem"
if re.match(carli,"aisacareem"):
    print("Match carli")
else:
    print("not match carli")

print("____________________________________\"Meta Characters therd bracked \"____________________________________")

therdbracked1 = r"[aeiou]"
if re.match(therdbracked1, "asdkji"):
    print("match aeiou")
else: 
    print("Not match")

therdbracked2 = r"[A-Z]"
if re.match(therdbracked2, "asdkji"):
    print("match A to Z")
else: 
    print("Not match A to Z")


therdbracked3 = r"[0-9][A-Z]"
if re.match(therdbracked3, "0asdkji"):
    print("match A to Z")
else: 
    print("Not match A to Z")

therdbracked4 = r"[0-9][a-z][A-Z]"
if re.match(therdbracked4, "0aZasdkji"):
    print("match A to Z")
else: 
    print("Not match A to Z")

