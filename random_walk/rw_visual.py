import matplotlib.pyplot as plt

from random_walk import RandomWalk

# 只要程序处于活动状态，就不断地模拟随机漫步
while True:
    # 创建一个RandomWalk实列，并将其包含的点都绘制出来
    rw = RandomWalk()
    rw.fill_walk()

    plt.figure(dpi=128, figsize=(8, 4))

    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=1)
    # 突出起点和终点
    plt.scatter(0, 0, c='green', edgecolors='none', s=10)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=10)
    plt.show()


