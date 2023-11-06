import QtQuick 2.15
import QtQuick.Window 2.12
import QtQuick.Controls 2.15
import QtGraphicalEffects 1.0


Popup {
    id: dataEntryPopup

    background: Rectangle {
        width: 652
       height: 72
       radius: 4
       color: "#4696FA"
       x:  542
       y: 223

       Text {
        text: "Please scan the Product QR Code"
        color: "white"
        font.family: "Archivo"
        font.pixelSize: 24
        width: 412
        height: 48
        x: 120
        y: 12
       }
    }
}