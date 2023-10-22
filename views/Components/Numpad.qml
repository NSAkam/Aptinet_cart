import QtQuick 2.15
import QtQuick.Window 2.12
import QtQuick.Controls 2.15
import QtGraphicalEffects 1.0
import "../Utiles"

Rectangle {

    ViewSettings
    {
        id:viewset
    }

    id:numpad
    width: 244
    height: 308
    radius: 4
    anchors.verticalCenter: parent.verticalCenter
    anchors.horizontalCenter: parent.horizontalCenter

    property TextInput inputtext



    KNumberButton{
        x:0
        y:0
        text: "1"
        onClicked: inputtext.text += "1"
    }

    KNumberButton{
        x:82
        y:0
        text: "2"
        onClicked: inputtext.text += "2"
    }
    KNumberButton{
        x:164
        y:0
        text: "3"
        onClicked: inputtext.text += "3"
    }
    KNumberButton{
        x:0
        y:62
        text: "4"
        onClicked: inputtext.text += "4"
    }
    KNumberButton{
        x:82
        y:62
        text: "5"
        onClicked: inputtext.text += "5"
    }
    KNumberButton{
        x:164
        y:62
        text: "6"
        onClicked: inputtext.text += "6"
    }
    KNumberButton{
        x:0
        y:124
        text: "7"
        onClicked: inputtext.text += "7"

    }
    KNumberButton{
        x:82
        y:124
        text: "8"
        onClicked: inputtext.text += "8"

    }
    KNumberButton{
        x:164
        y:124
        text: "9"
        onClicked: inputtext.text += "9"

    }
    KNumberButton{
        x:0
        y:186
        text: "-"

    }
    KNumberButton{
        x:82
        y:186
        text: "0"
        onClicked: inputtext.text += "0"

    }
    KNumberButton{
        x:164
        y:186
        font.pixelSize: 16
        text: "حذف"
        onClicked:{
            inputtext.text = inputtext.text.slice(0,-1)
        }
    }
}
