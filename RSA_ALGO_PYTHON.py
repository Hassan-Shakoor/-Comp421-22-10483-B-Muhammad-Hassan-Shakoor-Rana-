import rsa

print("__________________________________________")
print("Muhammad Hassan Shakoor Rana")
print("22-10483")
print("_________________________________________\n")


publicKey,privateKey = rsa.newkeys(512)

text=input("Enter something: ")

encrypted_text = rsa.encrypt(text.encode(),publicKey)

print("==============ORIGINAL STRING=================")
print(text)
print("\n")
print("==============encrypted string:===============")
print(encrypted_text)
print("\n")
decrypted_text= rsa.decrypt(encrypted_text, privateKey).decode()

print("==============DECRYPTED STRING:===============")
print(decrypted_text)
