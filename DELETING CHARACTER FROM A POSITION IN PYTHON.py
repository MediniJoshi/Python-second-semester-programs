String1 =input("")
print("Initial String: ")
print(String1)
a=len(String1) 
# Deleting a character
# of the String
print("Enter the position at which you want to delete the character")
n=int(input(""))
if n<=a:
   String2 = String1[0:n-1] + String1[n:]
   print("\nDeleting character at 2nd Index: ")
   print(String2)
