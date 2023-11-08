import QtQuick 2.15
import QtGraphicalEffects 1.0
import QtQuick.Controls 2.15

Item{
    property int battery_level: 50

    ProgressBar {
        id: targetProgressBar
        value: battery_level
        padding: 2
        from:0
        to:100


        background: Rectangle {
            implicitWidth: img_battery.width -2
            implicitHeight: img_battery.height
            color: "transparent"
            radius: 3
        }

        contentItem: Item {


            Rectangle {
                id:rect_porgress
                width: targetProgressBar.visualPosition * parent.width
                height: parent.height
                radius: 2
                color: "#17a81a"
            }
        }
        onValueChanged: {
            if(value < 30)
            {
                rect_porgress.color = "red"
            }
            else
            {
                rect_porgress.color = "#E1A44C"
            }
        }
    }

    Image {
        id: img_battery
        source: "../Assets/Battery.png"
        width: 36.67
        height: 23.33
    }
    Label{
        text:"%" + battery_level
        anchors.leftMargin: 5
        anchors.left: img_battery.right
        y:2.5
        // font.family: viewset.helveticaFont
        font.bold: true
        font.pixelSize: 16
        color: "white"

    }
}
