import sys
input = sys.stdin.readline

class custom_set:
    def __init__(self):
        self.set = set()
    
    def show(self):
        print(self.set)

    def add(self, num: int):
        if not self.check(num):
            self.set.add(num)
    
    def remove(self, num: int):
        if self.check(num):
            self.set.remove(num)

    def check(self, num: int) -> int:
        if num in self.set:
            return 1
        else:
            return 0
    
    def toggle(self, num: int):
        if self.check(num):
            self.set.remove(num)
        else:
            self.set.add(num)
    
    def all(self):
        self.set = {i for i in range(1, 21)}
    
    def empty(self):
        self.set = set()



if __name__ == "__main__":
    my_set = custom_set()
    m = int(input())

    for _ in range(m):
        cmd = input().split()
        if cmd[0] == "add":
            my_set.add(int(cmd[1]))
        elif cmd[0] == "remove":
            my_set.remove(int(cmd[1]))
        elif cmd[0] == "check":
            print(my_set.check(int(cmd[1])))
        elif cmd[0] == "toggle":
            my_set.toggle(int(cmd[1]))
        elif cmd[0] == "all":
            my_set.all()
        elif cmd[0] == "empty":
            my_set.empty()
        else:
            print("wrong cmd")
        # my_set.show()