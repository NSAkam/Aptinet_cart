import QtQuick 2.15
import QtGraphicalEffects 1.15
import "../Utiles" as Util
import "../Components"

GridView {
    width: 826
    height: 568
//    spacing: 16 /*22*/
//    flickableDirection: Flickable.HorizontalFlick
//    orientation: ListView.Horizontal
    cellWidth: 150
    cellHeight: 150
    focus: true

    model: 10
    delegate:
        Item {
        width: 150
        height: 150
//        x: 32
//        y: 40
//        spacing: 22
        Rectangle {
            width: 100
            height: 100
            id: mainrect
//            anchors.fill: parent
//            width: 190
//            height: 249
            color: "white"
            x: 0
            y: 54

            DropShadow {
                anchors.fill: mainrect
                cached: true
                horizontalOffset: 0
                verticalOffset: 8
                radius: 16.0
                y: 5
                samples: 30
                color: "#0000000A"
                smooth: true
                source: mainrect
                visible: shadow?true:false

        }

    }
    }







}
