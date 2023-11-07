#!/bin/python3
input = input("Type a word: ")

match input:
    case "Hello":
        print("Hi :)")
        pass
    case "Help":
        print("What do you need?")
    case "Exit":
        print("Ok bye")
    case _:
        print("Invalid word!")
