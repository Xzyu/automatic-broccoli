import queue
class hasher:
    def __init__(self):
        pass

    def hashIt(self, password):
        q = queue.Queue()
        hashednum = 1
        y = 0
        for x in range(0, len(password)):
            q.put((ord(password[x]) - 96))
        while not q.empty():
            hashednum = hashednum * q.get() + (ord(password[y-1]) * 25) #change to change number
            y = y + 1
        return hashednum
