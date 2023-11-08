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
    width: 308
    height: 375
    radius: 4
    //anchors.verticalCenter: parent.verticalCenter
    //anchors.horizontalCenter: parent.horizontalCenter

    property TextInput inputtext



    KNumberButton{
        x:32
        y:34
        text: "1"
        onClicked: inputtext.text += "1"
    }

    KNumberButton{
        x:124
        y:34
        text: "2"
        onClicked: inputtext.text += "2"
    }
    KNumberButton{
        x:216
        y:34
        text: "3"
        onClicked: inputtext.text += "3"
    }
    KNumberButton{
        x:32
        y:116
        text: "4"
        onClicked: inputtext.text += "4"
    }
    KNumberButton{
        x:124
        y:116
        text: "5"
        onClicked: inputtext.text += "5"
    }
    KNumberButton{
        x:216
        y:116
        text: "6"
        onClicked: inputtext.text += "6"
    }
    KNumberButton{
        x:32
        y:199
        text: "7"
        onClicked: inputtext.text += "7"

    }
    KNumberButton{
        x:124
        y:199
        text: "8"
        onClicked: inputtext.text += "8"

    }
    KNumberButton{
        x:216
        y:199
        text: "9"
        onClicked: inputtext.text += "9"

    }
    KNumberButton{
        x:32
        y:280
        text: "#"

    }
    KNumberButton{
        x:124
        y:280
        text: "0"
        onClicked: inputtext.text += "0"

    }
    KNumberButton{
        x:216
        y:280
        font.pixelSize: 16
        text: "<--"
        onClicked:{
            inputtext.text = inputtext.text.slice(0,-1)
        }
    }
}
