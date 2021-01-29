def triangle(angle):
    if len(angle) == 3 and sum(angle) == 180 and 0 not in angle:
        if max(angle) > 90:
            print("둔각삼각형")
        elif max(angle) == 90:
            print("직각삼각형")
        else:
            print("예각삼각형")
    else:
        print("삼각형이 아닙니다")

triangle([30, 40 ,50, 60])

