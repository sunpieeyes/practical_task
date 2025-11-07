def compress_string(strk) :
    result = []
    current_char = strk[0]
    count = 1

    for i in range(1,len(strk)):
        if strk[i] == current_char:
            count += 1
        else:
            result.append(current_char + str(count))
            current_char = strk[i]
            count = 1
    result.append(current_char + str(count))

    return "".join(result)

text_str = "hhheeelllllllloooo wwworlddddd"
result = compress_string(text_str)
print(result)