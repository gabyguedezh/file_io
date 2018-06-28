f = open("newfile.txt", "a")
lines= ['Hello','World','Welcome','To','File IO']
text = "\n".join(lines)
# f.write("Hello\n")
f.writelines(text)
f.close()