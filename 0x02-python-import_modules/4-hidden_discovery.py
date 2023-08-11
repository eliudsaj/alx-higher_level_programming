#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    all_dir = dir(hidden_4)
    for i in range(0, len(all_dir)):
        if not (len(all_dir) > 2 and all_dir[i][0] == '_' and all_dir[i][1] == '_'):
            print(all_dir[i])
