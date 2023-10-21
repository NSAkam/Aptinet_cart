import QtQuick 2.12
import QtQuick.Window 2.12
import QtQuick.Controls 2.12
import QMLLanguageManager.binding 1.0

Window {
    width: 640
    height: 480
    visible: true
    title: qsTr("Multi Language")
    id: root

    QMLLanguageManager {
        id: languageManager
    }

    Component.onCompleted: {
        languageManager.change_language("en");
    }

    Rectangle{
        id: myrect
        width: root.width
        height: root.height
        anchors.fill: root
        color: "pink"
    }

    MyText{
        text_property: languageManager.read_how 
        x_location: 400
        y_location: 50
    }

    MyText{
        text_property: languageManager.read_why 
        x_location: 400
        y_location: 150
    }

    MyText{
        text_property: languageManager.read_where 
        x_location: 400
        y_location: 250
    }

    Button{
        id: enbutton
        text: "en"
        font.italic: true
        font.pixelSize: 20
        x: 400
        y: 350
        onClicked: {
            languageManager.change_language("en")
        }

    }

    Button{
        id: fabutton
        text: "fa"
        font.italic: true
        font.pixelSize: 20
        x: 100
        y: 350
        onClicked: {
            languageManager.change_language("fa")
        }

    }



}

