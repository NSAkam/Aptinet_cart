import QtQuick 2.15
import QtQuick.Controls 2.15

Rectangle{
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
        y:80
        rows: 5
        columns: 1
        spacing: 2
        Row{
            spacing: 2
            KKeyboardButton{

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
            KKeyboardButton{
                width: 70
                height: 70
                text: "-"
                onClicked: {
                    parent.parent.parent.input(this.text)
                }
            }
            KKeyboardButton{
                width: 70
                height: 70
                text: "="
                onClicked: {
                    parent.parent.parent.input(this.text)
                }
            }
            KKeyboardButton{
                width: 114
                text: "<--"
                onClicked: {
                    parent.parent.parent.backspace()
                }
            }
        }
        Row{
            spacing: 2
            KKeyboardButton{
                width: 70
                height: 70
                text: "@"
                onClicked: {
                    parent.parent.parent.input(this.text)
                }
            }
            KKeyboardButton{
                width: 70
                height: 70
                text: "#"
                onClicked: {
                    parent.parent.parent.input(this.text)
                }
            }
            KKeyboardButton{
                width: 70
                height: 70
                text: "$"
                onClicked: {
                    parent.parent.parent.input(this.text)
                }
            }
            KKeyboardButton{
                width: 70
                height: 70
                text: "%"
                onClicked: {
                    parent.parent.parent.input(this.text)
                }
            }
            KKeyboardButton{
                width: 70
                height: 70
                text: "^"
                onClicked: {
                    parent.parent.parent.input(this.text)
                }
            }
            KKeyboardButton{
                width: 70
                height: 70
                text: "&"
                onClicked: {
                    parent.parent.parent.input(this.text)
                }
            }
            KKeyboardButton{
                width: 70
                height: 70
                text: "\&"
                onClicked: {
                    parent.parent.parent.input(this.text)
                }
            }
            KKeyboardButton{
                width: 70
                height: 70
                text: "*"
                onClicked: {
                    parent.parent.parent.input(this.text)
                }
            }
            KKeyboardButton{
                width: 70
                height: 70
                text: "("
                onClicked: {
                    parent.parent.parent.input(this.text)
                }
            }
            KKeyboardButton{
                width: 70
                height: 70
                text: ")"
                onClicked: {
                    parent.parent.parent.input(this.text)
                }
            }
            KKeyboardButton{
                width: 70
                height: 70
                text: "["
                onClicked: {
                    parent.parent.parent.input(this.text)
                }
            }
            KKeyboardButton{
                width: 70
                height: 70
                text: "]"
                onClicked: {
                    parent.parent.parent.input(this.text)
                }
            }
            KKeyboardButton{
                width: 114
                text: "\\"
                onClicked: {
                    parent.parent.parent.input(this.text)
                }
            }
        }
        Row{
            spacing: 2
            KKeyboardButton{
                width: 70
                height: 70
                text: "!"
                onClicked: {
                    parent.parent.parent.input(this.text)
                }
            }
            KKeyboardButton{
                width: 70
                height: 70
                text: "\""
                onClicked: {
                    parent.parent.parent.input(this.text)
                }
            }
            KKeyboardButton{
                width: 70
                height: 70
                text: "<"
                onClicked: {
                    parent.parent.parent.input(this.text)
                }
            }
            KKeyboardButton{
                width: 70
                height: 70
                text: ">"
                onClicked: {
                    parent.parent.parent.input(this.text)
                }
            }
            KKeyboardButton{
                width: 70
                height: 70
                text: ":"
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
                width: 70
                height: 70
                text: "?"
                onClicked: {
                    parent.parent.parent.input(this.text)
                }
            }
            KKeyboardButton{
                width: 70
                height: 70
                text: ";"
                onClicked: {
                    parent.parent.parent.input(this.text)
                }
            }
            KKeyboardButton{
                width: 70
                height: 70
                text: "ddd"
                opacity: 0
            }
            KKeyboardButton{
                width: 70
                height: 70
                text: "ddd"
                opacity: 0
            }
            KKeyboardButton{
                width: 70
                height: 70
                text: "'"
                opacity: 0
                onClicked: {
                    parent.parent.parent.input(this.text)
                }
            }
            KKeyboardButton{
                width: 172
                text: "enter"
                color: viewset.primaryColor
                onClicked: {
                    parent.parent.parent.enter()
                }
            }
        }

        Row{
            spacing: 2
            KKeyboardButton{
                width: 114
                text: "123 ..."
                onClicked: {
                    parent.parent.parent.shiftClicked(3);
                }
            }
            KKeyboardButton{
                width: 70
                height: 70
                text: "fn"
                onClicked: {
                    parent.parent.parent.shiftClicked(2);
                }
            }
            KKeyboardButton{
                width: 462
                text: "space"
                onClicked: {
                    parent.parent.parent.input(" ")
                }
            }
            KKeyboardButton{
                width: 70
                height: 70
                text: "fn"

                onClicked: {
                    parent.parent.parent.shiftClicked(2)
                }
            }
            KKeyboardButton{
                width: 114
                text: "close"
                onClicked: {
                    parent.parent.parent.close();
                }
            }
        }
    }
}
