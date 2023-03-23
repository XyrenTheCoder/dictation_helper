from colorama import Fore

target = str(input("enter text: "))
string = str(input("> "))
out = []

for i in string:
    for a in target:
       if i != a:
           out.append(Fore.RED + i)
       else:
           out.append(i)

print(f"text: {target}")
print(f"your input: {''.join(out)}")


