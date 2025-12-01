import sys

print("Version =", sys.version)
print("Path =", sys.path)
print("Maxsize=", sys.maxsize)
sys.stdout.write("Hello World\n")

num1 = int(sys.argv[1])
num2 = int(sys.argv[2])

print("Sum = ", num1 + num2)

age = 20
if age < 18:
    print("Not Allowed")
    sys.exit()

print("Welcome Inside")

ages = int(sys.argv[3])
if ages < 18:
    print("Not Vote")
    sys.exit()
else:
    print("Vote")

