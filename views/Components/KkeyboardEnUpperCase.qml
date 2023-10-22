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
        y:20

        rows: 5
        columns: 1
        spacing: 8
        Row{
            spacing: 8
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
            spacing: 8
            KKeyboardButton{
                width: 70
                height: 70
                text: "Q"
                onClicked: {
                    parent.parent.parent.input(this.text)
                }
            }
            KKeyboardButton{
                width: 70
                height: 70
                text: "W"
                onClicked: {
                    parent.parent.parent.input(this.text)
                }
            }
            KKeyboardButton{
                width: 70
                height: 70
                text: "E"
                onClicked: {
                    parent.parent.parent.input(this.text)
                }
            }
            KKeyboardButton{
                width: 70
                height: 70
                text: "R"
                onClicked: {
                    parent.parent.parent.input(this.text)
                }
            }
            KKeyboardButton{
                width: 70
                height: 70
                text: "T"
                onClicked: {
                    parent.parent.parent.input(this.text)
                }
            }
            KKeyboardButton{
                width: 70
                height: 70
                text: "Y"
                onClicked: {
                    parent.parent.parent.input(this.text)
                }
            }
            KKeyboardButton{
                width: 70
                height: 70
                text: "U"
                onClicked: {
                    parent.parent.parent.input(this.text)
                }
            }
            KKeyboardButton{
                width: 70
                height: 70
                text: "I"
                onClicked: {
                    parent.parent.parent.input(this.text)
                }
            }
            KKeyboardButton{
                width: 70
                height: 70
                text: "O"
                onClicked: {
                    parent.parent.parent.input(this.text)
                }
            }
            KKeyboardButton{
                width: 70
                height: 70
                text: "P"
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
            spacing: 8
            KKeyboardButton{
                width: 70
                height: 70
                text: "A"
                onClicked: {
                    parent.parent.parent.input(this.text)
                }
            }
            KKeyboardButton{
                width: 70
                height: 70
                text: "S"
                onClicked: {
                    parent.parent.parent.input(this.text)
                }
            }
            KKeyboardButton{
                width: 70
                height: 70
                text: "D"
                onClicked: {
                    parent.parent.parent.input(this.text)
                }
            }
            KKeyboardButton{
                width: 70
                height: 70
                text: "F"
                onClicked: {
                    parent.parent.parent.input(this.text)
                }
            }
            KKeyboardButton{
                width: 70
                height: 70
                text: "G"
                onClicked: {
                    parent.parent.parent.input(this.text)
                }
            }
            KKeyboardButton{
                width: 70
                height: 70
                text: "H"
                onClicked: {
                    parent.parent.parent.input(this.text)
                }
            }
            KKeyboardButton{
                width: 70
                height: 70
                text: "J"
                onClicked: {
                    parent.parent.parent.input(this.text)
                }
            }
            KKeyboardButton{
                width: 70
                height: 70
                text: "K"
                onClicked: {
                    parent.parent.parent.input(this.text)
                }
            }
            KKeyboardButton{
                width: 70
                height: 70
                text: "L"
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
                text: "'"
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
            spacing: 8

            KKeyboardButton{
                width: 114
                text: "shift"
                checked: true
                onClicked: {
                    parent.parent.parent.shiftClicked(2);
                }
            }
            KKeyboardButton{
                width: 70
                height: 70
                text: "Z"
                onClicked: {
                    parent.parent.parent.input(this.text)
                }
            }
            KKeyboardButton{
                width: 70
                height: 70
                text: "X"
                onClicked: {
                    parent.parent.parent.input(this.text)
                }
            }
            KKeyboardButton{
                width: 70
                height: 70
                text: "C"
                onClicked: {
                    parent.parent.parent.input(this.text)
                }
            }
            KKeyboardButton{
                width: 70
                height: 70
                text: "V"
                onClicked: {
                    parent.parent.parent.input(this.text)
                }
            }
            KKeyboardButton{
                width: 70
                height: 70
                text: "B"
                onClicked: {
                    parent.parent.parent.input(this.text)
                }
            }
            KKeyboardButton{
                width: 70
                height: 70
                text: "N"
                onClicked: {
                    parent.parent.parent.input(this.text)
                }
            }
            KKeyboardButton{
                width: 70
                height: 70
                text: "M"
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
                width: 70
                height: 70
                text: "/"
                onClicked: {
                    parent.parent.parent.input(this.text)
                }
            }
            KKeyboardButton{
                width: 114
                text: "shift"
                checked: true
                onClicked: {
                    parent.parent.parent.shiftClicked(2);
                }
            }
        }
        Row{
            spacing: 8
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
                    parent.parent.parent.shiftClicked(3);
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
                    parent.parent.parent.shiftClicked(3);
                }
            }
            KKeyboardButton{
                width: 114
                text: "close"

                onClicked: {
                    parent.parent.parent.close()
                }
            }
        }
    }
}
