result = ""
display = f"[{result}]"

while True:
    userInput = input("input: ").strip(" ")
    # calculate result
    if userInput == "=":
        try:
            result = result.rstrip()
            e = eval(result)
            print(f"[{result} = {e}]")
            result = ""
            continue
        except Exception:
            print("Syntax Error")
            result = ""
            continue

    # delete prev input
    if userInput.lower() == "del":
        result = result[:-3]
        display = f"[{result}]"
        print(display)
        if display == "[]":
            continue
        result += " "

    # random ahh input
    else:
        result += userInput
        display = f"[{result}]"
        print(display)
        result += " "

