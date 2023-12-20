def is_valid_move(move):
    if len(move) != 5:
        return False
    
    start = move[0:2]
    end = move[3:5]
    
    valid_chars = 'ABCDEFGH'
    valid_nums = '12345678'
    
    if start[0] not in valid_chars or end[0] not in valid_chars:
        return False
    if start[1] not in valid_nums or end[1] not in valid_nums:
        return False
    
    x_move = abs(ord(start[0]) - ord(end[0]))
    y_move = abs(int(start[1]) - int(end[1]))
    if (x_move, y_move) not in [(1, 2), (2, 1)]:
        return False
    
    return True

user_move = input("Введите ход конем (например, С7-D5): ")

if is_valid_move(user_move):
    print("Этот ход конем верный!")
else:
    print("Этот ход конем неверный или записан некорректно.")
