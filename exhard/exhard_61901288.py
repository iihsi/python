"""
ファイル名の00000000を学籍番号に置き換えて提出すること

総合演習: リバーシを作ろう
"""


def initialize_board():
    """盤面を初期化して返す関数

    盤面を初期化して返す。
    盤面は10x10の2次元リストとし、ある(x,y)の位置のマスはlist[y][x]で表すものとする。
    このリストには、ゲームで使わないマスには-1を、石が置いていないマスは0を,
    白石が置いてあるマスは1を,黒石が置いてあるマスは2を入れるとする。
    初期化時は中央の8x8の部分以外は-1で埋めておき、
    (4, 4), (5, 5)のマスに1を、(4, 5), (5, 4)のマスに2を、
    残ったマスには0を埋めるようにする。
    
    -1,-1,-1,-1,-1,-1,-1,-1,-1,-1
    -1, 0, 0, 0, 0, 0, 0, 0, 0,-1
    -1, 0, 0, 0, 0, 0, 0, 0, 0,-1
    -1, 0, 0, 0, 0, 0, 0, 0, 0,-1
    -1, 0, 0, 0, 1, 2, 0, 0, 0,-1
    -1, 0, 0, 0, 2, 1, 0, 0, 0,-1
    -1, 0, 0, 0, 0, 0, 0, 0, 0,-1
    -1, 0, 0, 0, 0, 0, 0, 0, 0,-1
    -1, 0, 0, 0, 0, 0, 0, 0, 0,-1
    -1,-1,-1,-1,-1,-1,-1,-1,-1,-1

    Returns:
        list: 10x10の2次元リスト

    """
    mylist = [[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
              [-1, 0, 0, 0, 0, 0, 0, 0, 0,-1],
              [-1, 0, 0, 0, 0, 0, 0, 0, 0,-1],
              [-1, 0, 0, 0, 0, 0, 0, 0, 0,-1],
              [-1, 0, 0, 0, 1, 2, 0, 0, 0,-1],
              [-1, 0, 0, 0, 2, 1, 0, 0, 0,-1],
              [-1, 0, 0, 0, 0, 0, 0, 0, 0,-1],
              [-1, 0, 0, 0, 0, 0, 0, 0, 0,-1],
              [-1, 0, 0, 0, 0, 0, 0, 0, 0,-1],
              [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]]
    return mylist


def rival_player_num(player_num):
    """相手のプレイヤー番号を返す

    白が1, 黒が2として、現在のプレイヤー番号が1なら2を、2なら1を返す
    それ以外のプレイヤー番号が引数に与えられたら-1を返す

    Args:
        player_num (num): 現在のプレイヤー番号

    Returns:
        int: 相手のプレイヤー番号

    """
    if player_num == 1:
        return 2
    elif player_num == 2:
        return 1
    else:
        return -1

def count_reverse(board, player_num, x_put, y_put, x_direction, y_direction):
    """石を置いたときに特定の方向についてひっくり返せる数を返す

    (x_put, y_put)に石を置いたとき、(x_direction, y_direction)方向についてひっくり返せる数を返す
    ただしx_direction, y_directionは-1, 0, 1のどれかをとり、両方0が来ることはないものとする
    (ヒント: 置いた石からある方向に1マスずつ相手の石がある限り移動し続け、その先に自分の石があった場合にそこまでの相手の石をひっくり返せるものと考えると良い)

    Args:
        board: 盤面の2次元配列
        player_num: 石を置くプレイヤー番号
        x_put: 石を置くx座標
        y_put: 石を置くy座標
        x_direction: 調べたい方向のx座標
        y_direction: 調べたい方向のy座標

    Returns:
        int: ひっくり返せる石の数

    """
    count = 0
    for i in range(1, 9):
        x = x_put + x_direction*i
        y = y_put + y_direction*i
        if x <= 0 or x >= 9:
            return 0
        elif y <= 0 or y >= 9:
            return 0
        else:
            xy = board[y][x]
            if xy == 0 :
                return 0
            elif xy == -1:
                return 0
            elif xy == player_num:
                return count      
            elif xy == rival_player_num(player_num):
                count += 1 


def validate_reversible(board, player_num, x, y):
    """石を置いたときにひっくり返せるかどうかの確認

    player_numの石を(x,y)に置いたときに、ひっくり返せる石があるかどうか確認する
    ひっくり返せる石があればTrue, なければFalseを返す
    またx,yが1~8の間でない場合、および(x,y)の位置にすでに石がおいてある場合はFalseを返す
    ヒント: count_reverseを周囲8方向に対して行い、どれか1方向でもひっくり返せる数が1以上あればTrueを返すと良い

    Args:
        board: 盤面の2次元配列
        player_num: 石を置くプレイヤー番号
        x: 石を置くx座標
        y: 石を置くy座標

    Returns:
        bool: ひっくり返せる石があるかどうか

    """
    a = count_reverse(board, player_num, x, y, -1, -1)
    b = count_reverse(board, player_num, x, y, -1, 0)
    c = count_reverse(board, player_num, x, y, -1, 1)
    d = count_reverse(board, player_num, x, y, 0, -1) 
    e = count_reverse(board, player_num, x, y, 0, 1)
    f = count_reverse(board, player_num, x, y, 1, -1)
    g = count_reverse(board, player_num, x, y, 1, 0)
    h = count_reverse(board, player_num, x, y, 1, 1)
    if  a > 0:
        return True
    elif b > 0:
        return True
    elif c > 0:
        return True
    elif d > 0:
        return True
    elif e > 0:
        return True
    elif f > 0:
        return True
    elif g > 0:
        return True
    elif h > 0:
        return True    
    else:
        return False


def validate_reversible_all(board, player_num):
    """盤面上をすべてチェックして、石をひっくり返せる手があるかどうか確認する

    ヒント: validate_reversibleを全マス(x,yが1~8のところ)に対して行い、どれかひとつでもTrueならTrueを、ひとつもTrueでないならFalseを返せば良い

    Args:
        board: 盤面の2次元配列
        player_num: 石を置くプレイヤー番号

    Returns:
        bool: 盤面上すべてに対して、石をひっくり返せる手があればTrue、なければFalseを返す

    """
    count = 0
    for x in range(1, 9):
        for y in range(1, 9):
            if validate_reversible(board, player_num, x, y) == True:
                return True
            elif validate_reversible(board, player_num, x, y) == False:
                count += 1
                if count == 64:
                    return False 


def put_disc(board, player_num, x, y):
    """石を置いてひっくり返し、新しい盤面を返す

    player_numの石を(x,y)に石を置き、必要な石をすべてひっくり返した状態の新しい盤面を返す
    ヒント:
    - まずboardのコピーをとる(new_boardとする)
    - コピーしたnew_boardに対して、次にx,yの周囲8方向に対して、count_reverse()を実行してその返り値分だけx,yからのマスを塗り替える
    - 最後にnew_boardを返す

    Args:
        board: 盤面の2次元配列
        player_num: 石を置くプレイヤー番号
        x: 石を置くx座標
        y: 石を置くy座標

    Returns:
        list: 新しい盤面を表す2次元配列

    """
    new_board = board
    for a in range(1,7):
        if count_reverse(new_board, player_num, x, y, -1, -1) >= a:
            new_board[y-a][x-a] = player_num
        else:
            break
    
    for b in range(1,7):
        if count_reverse(new_board, player_num, x, y, -1, 0) >= b:
            new_board[y][x-b] = player_num
        else:
            break
    
    for c in range(1,7):
        if count_reverse(new_board, player_num, x, y, -1, 1) >= c:
            new_board[y+c][x-c] = player_num
        else:
            break
    
    for d in range(1,7):
        if count_reverse(new_board, player_num, x, y, 0, -1) >= d:
            new_board[y-d][x] = player_num
        else:
            break

    for e in range(1,7):
        if count_reverse(new_board, player_num, x, y, 0, 1) >= e:
            new_board[y+e][x] = player_num
        else:
            break
        
    for f in range(1,7):
        if count_reverse(new_board, player_num, x, y, 1, -1) >= f:
            new_board[y-f][x+f] = player_num
        else:
            break

    for g in range(1,7):
        if count_reverse(new_board, player_num, x, y, 1, 0) >= g:
            new_board[y][x+g] = player_num
        else:
            break
        
    for h in range(1,7):
        if count_reverse(new_board, player_num, x, y, 1, 1) >= h:
            new_board[y+h][x+h] = player_num
        else:
            break
            
    return new_board


def count_discs(board):
    """白と黒の石の数を数える

    盤面上の白と黒の石の数を数え、[白石の合計数、黒石の合計数]という形のリストを返す

    Args:
        board: 盤面の2次元配列

    Returns:
        list: [白石の合計数、黒石の合計数]という形のリスト

    """
    white = 0
    black = 0
    result = [white, black]
    for i in board:
        for j in i:
            if j == 1:
                white += 1
            elif j == 2:
                black += 1
    return result


def print_board(board):
    """盤面を表示する

    注意: この関数は学生のデバッグ用なので、それほど厳密でなくて良い
    石がない場所は'*', 白石は'O', 黒石は'X'とし、横方向にはマスとマスの間に半角スペースを置き、ゲームに使わないマスはそもそも何も表示しない
    例えば初期状態は以下のように表示される
    * * * * * * * *
    * * * * * * * *
    * * * * * * * *
    * * * O X * * *
    * * * X O * * *
    * * * * * * * *
    * * * * * * * *
    * * * * * * * *

    Args:
        board: 盤面の2次元配列

    Returns:
        
    """
    for i in range(10):
        for j in range(10):
            if board[i][j] == 0:
                board[i][j]= "* "
            elif board[i][j] == 1:
                board[i][j] = "O "
            elif board[i][j] == 2:
                board[i][j] = "X "
            else:
                board[i][j] = ""
    print(*board[0])
    print(*board[1])
    print(*board[2])
    print(*board[3])
    print(*board[4])
    print(*board[5])
    print(*board[6])
    print(*board[7])
    print(*board[8])
    print(*board[9])
            

def main():
    """ゲームの進行

    注意: この関数は学生のデバッグ用なので、それほど厳密でなくて良い
    ゲームを進行させる
    - まずinitialize_board()で初期化したboardを用意する
    - print_board()する
    - 現在のプレイヤーの状態を記憶する変数(player_num等)を用意
      - 先攻は黒なので、最初は2としておく
    - 何回パスが起きたかを記憶する変数(pass_count等)を用意し、0と初期化
    以下、無限ループ
    - プレイヤーが連続してパスした場合は勝負終了なので、count_discsの結果から勝敗を判定してループを抜ける
    - player_numにあわせて今がどっちの手番なのか表示する
    - 石を置く場所がない場合、その旨を表示してpass_countを増やし、即座に相手の番にする
    - 石を置く場所があった場合、pass_countを0に戻しておく
    - コンソールからX,Yの座標を入力し(2回に分けたりして良い)、石が置ける座標を打つまで無限ループする
    - 石が置ける座標が来たら、put_disc()の返り値の新しい盤面で現在の盤面を上書きし、print_board()する

    Returns:

    """
    board = initialize_board()
    print_board(board)
    player_num = 2
    pass_count = 0
    while True:
        if pass_count == 2:
            end = count_discs(board)
            if end[0] > end[1]:
                print("白の勝ちです")
                break
            elif end[0] < end[1]:
                print("黒の勝ちです")
                break
            elif end[0] == end[1]:
                print("引き分けです")
                break
        else:
            if player_num == 1:
                print("白の番です")
                if validate_reversible_all(board, player_num) == False:
                    print("置く場所がありません")
                    pass_count += 1
                    player_num = rival_player_num(player_num)
                elif validate_reversible_all(board, player_num) == True:
                    pass_count = 0
                    print("x座標は")
                    x = input()
                    print("y座標は")
                    y = input()
                    if validate_reversible(board, player_num, x, y) == False:
                        print("そこには置けません")
                    elif validate_reversible(board, player_num, x, y) == True:
                        board = put_disc(board, player_num, x, y)
                        print_board(board)
            elif player_num == 2:
                print("黒の番です")
                if validate_reversible_all(board, player_num) == False:
                    print("置く場所がありません")
                    pass_count += 1
                    player_num = rival_player_num(player_num)
                elif validate_reversible_all(board, player_num) == True:
                    pass_count = 0
                    print("x座標は")
                    x = input()
                    print("y座標は")
                    y = input()
                    if validate_reversible(board, player_num, x, y) == False:
                        print("そこには置けません")
                    elif validate_reversible(board, player_num, x, y) == True:
                        board = put_disc(board, player_num, x, y)
                        print_board(board)                       
                    
                
if __name__ == "__main__":
    main()
