import math
test_h = int(input("insert the height of the wall \n"))
test_w = int(input("insert the width of the wall \n"))
coverage = int(input("what is the coverage\n"))


def paint_calc(h, w, cove):

    area = ((test_h*test_w)/coverage)
    round_area = math.ceil(area)
    print(f"your paintable area is {round_area}")

paint_calc(h=test_h,w= test_w, cove= coverage)