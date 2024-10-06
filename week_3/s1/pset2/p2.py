def remove_char(s, n): 
    # fixed_s = ""
    # for i in range(len(s)):    
    #     if i != n:
    #         fixed_s += s[i]
    # return fixed_s
    return s[:n] + s[n+1:]


def main():
    s = "Azziza"
    fixed_s = remove_char(s, 2)
    print(fixed_s)

main()
