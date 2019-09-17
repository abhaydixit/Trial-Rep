import turtle

def drawSnowFlakes(depth, length):
    if depth == 0:
        return

    for i in range(6):
        turtle.forward(length)
        drawSnowFlakes(depth - 1, length/3)
        turtle.back(length)
        turtle.right(60)


def main():
    depth = int(input('Enter depth: '))
    drawSnowFlakes(depth, 100)
    input('Close the graphic window when done.')
    turtle.mainloop()

if __name__ == '__main__':
    main()