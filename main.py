from turtle import Screen
import turtle as t
import random

flork = t.Turtle()


def w_ileri():
    flork.forward(10)


def a_sol_dön():
    flork.left(15)


def d_sağ_dön():
    flork.right(15)


def s_geri_git():
    flork.back(10)


def c_sıfırla():
    flork.reset()

screen = Screen()
screen.listen()
screen.onkey(w_ileri, "w")
screen.onkey(a_sol_dön, "a")
screen.onkey(d_sağ_dön, "d")
screen.onkey(s_geri_git, "s")
screen.onkey(c_sıfırla, "c")
screen.exitonclick()

