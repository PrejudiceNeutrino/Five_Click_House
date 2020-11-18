# Five_Click_House.py
# Constructions workers hate him, learn how to make a house in just five clicks!

from graphics import *


def main():
    win = GraphWin('House', 1500, 800)
    win.setCoords(0, 0, 100, 100)

    p1 = win.getMouse()
    p2 = win.getMouse()

    frame = Rectangle(p1, p2)
    frame.draw(win)
    frame.setFill('grey')
    frame.setOutline('purple')
    frame.setWidth(4)

    houseBottomY = min(p1.getY(), p2.getY())
    houseTopY = max(p1.getY(), p2.getY())
    houseLeftX = min(p1.getX(), p2.getX())
    houseRighX = max(p1.getX(), p2.getX())

    p3 = win.getMouse()

    doorW = abs(p1.getX() - p2.getX()) * 0.2
    doorH = abs(p3.getY() - houseBottomY)
    doorP1 = Point(p3.getX() - doorW * 0.5, houseBottomY)
    doorP2 = Point(p3.getX() + doorW * 0.5, p3.getY())

    door = Rectangle(doorP1, doorP2)
    door.draw(win)
    door.setFill('red')
    door.setOutline('black')
    door.setWidth(4)

    p4 = win.getMouse()

    windowH = doorW * 0.5
    windowP1 = Point(p4.getX() - windowH * 0.5, p4.getY() - windowH * 0.5)
    windowP2 = Point(p4.getX() + windowH * 0.5, p4.getY() + windowH * 0.5)

    window = Rectangle(windowP1, windowP2)
    window.draw(win)
    window.setFill('green')
    window.setOutline('black')
    window.setWidth(4)

    # Window Bars
    bar_1 = Point(windowP1.getX(), windowP2.getY())
    bar_1v = Point(windowP2.getX(), windowP1.getY())
    bar = Line(bar_1, bar_1v)
    bar.draw(win)
    bar_2 = Line(windowP1, windowP2)
    bar_2.draw(win)
    bar.setWidth(4)
    bar_2.setWidth(4)
    bar.setFill('black')
    bar_2.setFill('black')

    p5 = win.getMouse()

    roofP1 = Point(houseLeftX, houseTopY)
    roofP2 = Point(houseRighX, houseTopY)
    roofP3 = p5

    roof = Polygon(roofP1, roofP2, roofP3)
    roof.draw(win)
    roof.setFill('purple')
    roof.setOutline('black')
    roof.setWidth(4)

    win.getMouse()

main()
