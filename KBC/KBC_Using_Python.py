# KBC game using Python
'''Create a program capable of displaying questions to the user like KBC.
Use List data type to store the questions and their correct answers.
Display the final amount the person is taking home after playing the game.
'''


questions = [
    ["ISP stands for:", "1. Internet Survey Period", "2. Integrated Service Provider",
        "3. Internet Service Provider", "4. Internet Security Protocol", 3],

    ["Main circuit board in a computer is:", "1. Decoder",
        "2. Highlight", "3. Select", "4. Motherboard", 4],

    ["Internet Explorer is a:", "1. Any person browsing the net",
        "2. Web Browser", "3. Graphing Package", "4. News Reader", 2],

    ["Which company created the most used networking software in the 1980's",
        "1. Microsoft", "2. Sun", "3. IBM", "4. Novell", 2],

    ["In which decade was the Internet first implemented?",
        "1. 1940s", "2. 1950s", "3. 1960s", "4. 1980s", 3],

    ["'.TMP' extension refers usually to what kind of file?", "1. Compressed Archive file",
        "2. Image file", "3. Temporary file", "4. Audio file", 3],

    ["In what year was the '@' chosen for its use in e-mail addresses?",
        "1. 1976", "2. 1972", "3. 1980", "4. 1984", 2],

    ["What was the first ARPANET message?", "1. 'lo'", "2. 'hello world'",
        "3. 'mary had a little lamb'", "4. 'cyberspace, the final frontier'", 1],

    ["Where is the headquarters of Intel located?", "1. Redmond, Washington",
        "2. Tucson, Arizona", "3. Santa Clara California", "4. Richmond, Virginia", 3],

    ["Which one is the first fully supported 64-bit operating system",
        "1. Windows Vista", "2. Mac", "3. Linux", "4. Windows XP", 3],

    ["Computer Hard Disk was first introduced in 1956 by",
        "1. Dell", "2. Apple", "3. Microsoft", "4. IBM", 4],

    ["Which one of the followings is a programming language",
        "1. HTTP", "2. HTML", "3. HPML", "4. FTP", 2],

    ["Which protocol is used to received e-mail",
        "1. SMTP", "2. POP3", "3. HTTP", "4. FTP", 2],

    ["Which computer program converts assembly language to machine language",
        "1. Interpreter", "2. Compiler", "3. Assembler", "4. Comparator", 3],

    ["Which one is the latest one from PARAM SuperSries computers", "1. PARAM Yuva II", "2. PARAM 10000", "3. PARAM Padma", "4. PARAMnet", 1]]


levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000,
          160000, 320000, 640000, 1250000, 2500000, 5000000, 10000000]

prizeMoney = 0
padaoNumber = 0
padaoPrize = [0, 10000, 320000, 1000000]

print()
print()


for i in range(15):
    print(f"-------- Your Question for Rs. {levels[i]} --------".center(45))
    print()
    print(f"{questions[i][0]}")
    print()

    print("Options :")
    print(f"{questions[i][1]}")
    print(f"{questions[i][2]}")
    print(f"{questions[i][3]}")
    print(f"{questions[i][4]}")

    print()
    ans = int(input("Enter your Answer (1-4) : "))

    if ans == questions[i][5]:
        print()
        print("Correct Answer")
        prizeMoney = levels[i]
        print(f"You won Rs. {prizeMoney}")
        print()
        print()
    else:
        print()
        print("Wrong Answer")
        break

    if (i == 4 or i == 9 or i == 14):
        print(" *** Congratulations !!! ***".center(30))
        print(f"Aapne {padaoNumber+1} padao paar karliya hai")
        print(f"Check of Rs. {prizeMoney} handed to You")
        padaoNumber = padaoNumber+1
        print()
        print()

# For printing thw Final Prize Won
match padaoNumber:
    case 0:
        print(f"Prize Won = Rs. {padaoPrize[0]}")
    case 1:
        print(f"Prize Won = Rs. {padaoPrize[1]}")
    case 2:
        print(f"Prize Won = Rs. {padaoPrize[2]}")
    case 3:
        print(f"Prize Won = Rs. {padaoPrize[3]}")
