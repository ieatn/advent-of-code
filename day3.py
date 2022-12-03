ans = 0
# for each line in input file
for line in open('input.txt'):
    # x is the string on the line, just no extra spaces
    x = line.strip()
    # y is left half of string, z is right half
    y,z = x[:len(x)//2], x[len(x)//2:]
    # for each character in left half, check if this character is also in z
    for c in y:
        if c in z:
            # if this character is lowercase, use ord to get ascii num of c, add to ans + 1 for 0 based index
            if 'a' <= c <= 'z':
                ans += ord(c)-ord('a') + 1
            # if uppercase, add 26 for uppercase ascii value
            else:
                ans += ord(c)-ord('A') + 1 + 26
            # no duplicate characters
            break
print(ans)
