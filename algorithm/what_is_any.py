def solution(spell, dic):
    spell = set(spell)
    for s in dic:
        if not spell - set(s):
            return 1
    return 2

if __name__ == "__main__":
    print(solution(["p", "o", "s"], ["sod", "eocd", "qixm", "adio", "soo"]))
    print(solution(["z", "d", "x"], ["def", "dww", "dzx", "loveaw"]))