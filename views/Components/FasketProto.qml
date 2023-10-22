import QtQuick 2.15
import QtQuick.Controls 2.15
import QtGraphicalEffects 1.15

Item{
    x:32
    y:40
    width: 120
    height: 35
    Image {
        id: img_logo
        source: "../../Assets/FASKET.svg"
    }
    ColorOverlay{
        anchors.fill: img_logo
        source:img_logo
        color:"#2979ff"
        transform:rotation
        antialiasing: false
        width: 600
        height: 600

        SequentialAnimation on color {
            loops: Animation.Infinite
            ColorAnimation { from: viewset.primaryColor; to: viewset.focusColor; duration: 1200 }
            ColorAnimation { from: viewset.focusColor; to: viewset.primaryColor; duration: 1200 }
        }

    }
    Label{
        text: "Designed by KAST"
        font.pixelSize: 10
        font.family: viewset.danaFuNumFont
        x:31
        y:40
        color: "#DADAE1"
        font.letterSpacing: 0.5
    }
}
