def cipher(text, shift, key=None, decrypt=False): res = ""
for i, ch in enumerate(text) :
if ch. isalpha():
base = ord('A') if ch. isupper() else ord('a')
k = (ord(key[i % len(key)]) - base) % 26 if key else 0
s = (-shift - k) if decrypt else (shift + k)
res += chr((ord(ch) - base + s) % 26 + base)
elif ch.isdigit() :
s = -shift if decrypt else shift
res += chr((ord(ch) - ord('0') + s) % 10 + ord('0'))
else:res += ch
return res
#--- Main Program Loop ---while True:
choice = input("\nDo you want to Encrypt or Decrypt? (E/D) or Q to quit: "). strip(). upper()
if choice == 'Q':
print "Exiting program. ") 
  break
elif choice not in ('E', "D'):
print("Invalid choice. Please enter E, D, or Q.")
  continue
msg = input("Enter your message: ")
shift = int(input"Enter shift value: "))
key = input("Enter secret key (leave blank if none): ") or None
if choice == 'E':
result = cipher (msg, shift, key)
print("Encrypted: ", result)
else: result = cipher(msg, shift, key, decrypt=True)
print ("Decrynted " result)
