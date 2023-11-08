import QtQuick 2.15
import QtQuick.Controls 2.15

Rectangle{
    //color: "red"
    signal shiftClicked(state:int);
    signal input(key:string);
    signal close();
    signal enter();
    signal backspace();
    anchors.horizontalCenter: parent.horizontalCenter
    width: 1280
    height: 458
    color: "#1D1D1D"
    opacity: 0.75

    Grid {
        anchors.horizontalCenter: parent.horizontalCenter
        y:20
        rows: 5
        columns: 1
        spacing: 15
        Row{
            spacing: 15
            KKeyboardButton{
                radius: width
                width: 70
                height: 70
                text: "1"

                onClicked: {
                    parent.parent.parent.input(this.text)
                }
            }
            KKeyboardButton{
                width: 70
                height: 70
                text: "2"
                onClicked: {
                    parent.parent.parent.input(this.text)
                }
            }
            KKeyboardButton{
                width: 70
                height: 70
                text: "3"
                onClicked: {
                    parent.parent.parent.input(this.text)
                }
            }
            KKeyboardButton{
                width: 70
                height: 70
                text: "4"
                onClicked: {
                    parent.parent.parent.input(this.text)
                }
            }
            KKeyboardButton{
                width: 70
                height: 70
                text: "5"
                onClicked: {
                    parent.parent.parent.input(this.text)
                }
            }
            KKeyboardButton{
                width: 70
                height: 70
                text: "6"
                onClicked: {
                    parent.parent.parent.input(this.text)
                }
            }
            KKeyboardButton{
                width: 70
                height: 70
                text: "7"
                onClicked: {
                    parent.parent.parent.input(this.text)
                }
            }
            KKeyboardButton{
                width: 70
                height: 70
                text: "8"
                onClicked: {
                    parent.parent.parent.input(this.text)
                }
            }
            KKeyboardButton{
                width: 70
                height: 70
                text: "9"
                onClicked: {
                    parent.parent.parent.input(this.text)
                }
            }
            KKeyboardButton{
                width: 70
                height: 70
                text: "0"
                onClicked: {
                    parent.parent.parent.input(this.text)
                }
            }
            Image {
                source: "../Assets/AptinetKeyboard.png"
                width: 118
                height: 64
            }
        }
        Row{
            spacing: 15
            KKeyboardButton{
                width: 70
                height: 70
                text: "q"
                onClicked: {
                    parent.parent.parent.input(this.text)
                }
            }
            KKeyboardButton{
                width: 70
                height: 70
                text: "w"
                onClicked: {
                    parent.parent.parent.input(this.text)
                }
            }
            KKeyboardButton{
                width: 70
                height: 70
                text: "e"
                onClicked: {
                    parent.parent.parent.input(this.text)
                }
            }
            KKeyboardButton{
                width: 70
                height: 70
                text: "r"
                onClicked: {
                    parent.parent.parent.input(this.text)
                }
            }
            KKeyboardButton{
                width: 70
                height: 70
                text: "t"
                onClicked: {
                    parent.parent.parent.input(this.text)
                }
            }
            KKeyboardButton{
                width: 70
                height: 70
                text: "y"
                onClicked: {
                    parent.parent.parent.input(this.text)
                }
            }
            KKeyboardButton{
                width: 70
                height: 70
                text: "u"
                onClicked: {
                    parent.parent.parent.input(this.text)
                }
            }
            KKeyboardButton{
                width: 70
                height: 70
                text: "i"
                onClicked: {
                    parent.parent.parent.input(this.text)
                }
            }
            KKeyboardButton{
                width: 70
                height: 70
                text: "o"
                onClicked: {
                    parent.parent.parent.input(this.text)
                }
            }
            KKeyboardButton{
                width: 70
                height: 70
                text: "p"
                onClicked: {
                    parent.parent.parent.input(this.text)
                }
            }
            KKeyboardButton{
                width: 140
                height: 70
                text: "<--"
                color: "black"
                onClicked: {
                    parent.parent.parent.backspace()
                }
            }
        }
        Row{
            spacing: 15
            KKeyboardButton{
                width: 70
                height: 70
                text: "a"
                onClicked: {
                    parent.parent.parent.input(this.text)
                }
            }
            KKeyboardButton{
                width: 70
                height: 70
                text: "s"
                onClicked: {
                    parent.parent.parent.input(this.text)
                }
            }
            KKeyboardButton{
                width: 70
                height: 70
                text: "d"
                onClicked: {
                    parent.parent.parent.input(this.text)
                }
            }
            KKeyboardButton{
                width: 70
                height: 70
                text: "f"
                onClicked: {
                    parent.parent.parent.input(this.text)
                }
            }
            KKeyboardButton{
                width: 70
                height: 70
                text: "g"
                onClicked: {
                    parent.parent.parent.input(this.text)
                }
            }
            KKeyboardButton{
                width: 70
                height: 70
                text: "h"
                onClicked: {
                    parent.parent.parent.input(this.text)
                }
            }
            KKeyboardButton{
                width: 70
                height: 70
                text: "j"
                onClicked: {
                    parent.parent.parent.input(this.text)
                }
            }
            KKeyboardButton{
                width: 70
                height: 70
                text: "k"
                onClicked: {
                    parent.parent.parent.input(this.text)
                }
            }
            KKeyboardButton{
                width: 70
                height: 70
                text: "l"
                onClicked: {
                    parent.parent.parent.input(this.text)
                }
            }

            KKeyboardButton{
                width: 225
                height: 70
                text: "enter"
                color: "#F08C5A"
                onClicked: {
                    parent.parent.parent.enter()
                }
            }
        }
        Row{
            spacing: 15

            KKeyboardButton{
                width: 100
                height: 70
                text: "shift"
                onClicked: {
                    parent.parent.parent.shiftClicked(1)
                }
            }
            KKeyboardButton{
                width: 70
                height: 70
                text: "z"

                onClicked: {
                    parent.parent.parent.input(this.text)
                }
            }
            KKeyboardButton{
                width: 70
                height: 70
                text: "x"

                onClicked: {
                    parent.parent.parent.input(this.text)
                }
            }
            KKeyboardButton{
                width: 70
                height: 70
                text: "c"
                onClicked: {
                    parent.parent.parent.input(this.text)
                }
            }
            KKeyboardButton{
                width: 70
                height: 70
                text: "v"
                onClicked: {
                    parent.parent.parent.input(this.text)
                }
            }
            KKeyboardButton{
                width: 70
                height: 70
                text: "b"
                onClicked: {
                    parent.parent.parent.input(this.text)
                }
            }
            KKeyboardButton{
                width: 70
                height: 70
                text: "n"
                onClicked: {
                    parent.parent.parent.input(this.text)
                }
            }
            KKeyboardButton{
                width: 70
                height: 70
                text: "m"
                onClicked: {
                    parent.parent.parent.input(this.text)
                }
            }
            KKeyboardButton{
                width: 70
                height: 70
                text: ","
                onClicked: {
                    parent.parent.parent.input(this.text)
                }
            }
            KKeyboardButton{
                width: 70
                height: 70
                text: "."
                onClicked: {
                    parent.parent.parent.input(this.text)
                }
            }
            KKeyboardButton{
                width: 114
                height: 70
                text: "shift"
                onClicked: {
                    parent.parent.parent.shiftClicked(1)
                }
            }
        }
        Row{
            spacing: 15
            KKeyboardButton{
                width: 100
                height: 70
                text: "123?"
                onClicked: {
                    parent.parent.parent.shiftClicked(3);
                }
            }
            KKeyboardButton{
                width: 70
                height: 70
                text: "fn"
                onClicked: {
                    parent.parent.parent.shiftClicked(3)
                }
            }
            KKeyboardButton{
                width: 70
                height: 70
                text: "@"
                onClicked: {
                    parent.parent.parent.input(this.text)
                }
            }
            KKeyboardButton{
                width: 410
                height: 70
                text: ""
                onClicked: {
                    parent.parent.parent.input(" ")
                }
            }
            KKeyboardButton{
                width: 100
                height: 70
                text: ".com"
                onClicked: {
                    parent.parent.parent.input(" ")
                }
            }
            KKeyboardButton{
                width: 70
                height: 70
                text: "_"
                onClicked: {
                    parent.parent.parent.input("_")
                }
            }
            KKeyboardButton{
                width: 70
                height: 70
                text: "close"
                color: "black"
                onClicked: {
                    parent.parent.parent.close()
                }
            }
        }
    }
}
