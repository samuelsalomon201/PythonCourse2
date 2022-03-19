NSFW = open("E:\samuel\Content(18+).txt")
print(NSFW)
print(NSFW.read())
print(len(NSFW.read()))

print(NSFW.seek(0))
print(len(NSFW.read()))

print(NSFW.close())

NSFW = open("E:\samuel\Content(18+).txt", "r+")
print(NSFW.truncate())

NSFW.close()
NSFW = open("E:\samuel\Content(18+).txt", "r+")
NSFW.truncate(10)
NSFW.close()
NSFW = open("E:\samuel\Content(18+).txt")
print(len(NSFW.read()))
NSFW.close()
