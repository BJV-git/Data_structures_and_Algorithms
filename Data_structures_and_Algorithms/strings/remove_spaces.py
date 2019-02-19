# normal observations
# can use two pointers to move and then exchange

def remove_string(s):
    output=''
    space=False
    ls = len(s)

    for i in range(ls):
        if not s[i].isspace():
            if space:
                if s[i] in (',','.','?'):
                    pass
                else:
                    output+=s[i] # means we are adding the character

            space = False
            output+=s[i]

        elif s[i-1].isspace(): # i-1 as we set the flag to true, when we face the space second time
            space= True

    return output
print(remove_string('geek    .'))