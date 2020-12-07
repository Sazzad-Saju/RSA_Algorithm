#  input_key.txt contains prime p, q and e. To generate
#  big prime numbers go: https://bigprimes.org/
#  or, get some in Key_set.txt file....

while True:
    try:
        myfile = open("input_key.txt", "r+")
        break
    except IOError:
        input("Could not open file! Press Enter to retry.")

with open('input_key.txt','r') as f:
    p = f.readline()
    p = int(p[:-1])
    q = f.readline()
    q = int(q[:-1])
    n = p*q
    e = int(f.readline())
with open('public_key','w') as f:
    f.write(str(n))
    f.write('\n')
    f.write(str(e))
with open('private_key','w') as f:
    f.write(str(p))
    f.write('\n')
    f.write(str(q))

if(p != "" and q  != "" and e != ""):
    print("Key has been created!")