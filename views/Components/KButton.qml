import QtQuick 2.15
import QtGraphicalEffects 1.0
import QtQuick.Controls 2.15


Button {
    id: controlBt

    property bool ishover: true
    property int fontsize: 20
    property bool isBold: true
    property bool shadow: false
    property string btn_color:ishover? viewset.primaryColor:viewset.opacityColor
    property string btn_bordercolor: viewset.opacityColor
    property int btn_borderWidth: 1
    property string shadowcolor
    property int borderRadius : 50


    contentItem: Label {
        text: parent.text
        opacity: enabled ? 1.0 : 0.3
        horizontalAlignment: Text.AlignHCenter
        verticalAlignment: Text.AlignVCenter
        elide: Text.ElideRight
        color: "white"
        font.pixelSize: fontsize
        font.bold: isBold?true:false
        //font.weight: isBold? Font.Bold:Font.Normal
        //font.capitalization: Font.hintingPreference
        LayoutMirroring.enabled: true

    }

    background: Rectangle {
        id:primaryButton
        color: btn_color
        implicitWidth: 280
        implicitHeight: 40
        opacity: enabled ? 1 : 0.3
        border.color: btn_bordercolor
        border.width: btn_borderWidth
        radius: borderRadius
    }
    // onPressed:{
    //     if(ishover === true){
    //         clickanimation.start()
    //     }
    // }
    // onReleased:{
    //     if(ishover === true){
    //         releaseanimation.start()
    //     }
    // }
    DropShadow {
        id: rectShadow
        anchors.fill: source
        cached: true
        horizontalOffset: 0
        verticalOffset: 5
        radius: 16.0
        y: 5
        samples: 30
        color: "#50000000"
        smooth: true
        source: primaryButton
        visible: shadow?true:false

    }

    ParallelAnimation {
        id: clickanimation

        // Expand the button
        //        PropertyAnimation {
        //            target: controlBt
        //            property: "width"
        //            to: controlBt.width - 5
        //            duration: 100
        //            easing.type: Easing.Linear
        //        }

        PropertyAnimation {
            target: primaryButton
            property: "color"
            from: viewset.primaryColor
            to: viewset.focusColor
            duration: 600
        }
    }
    ParallelAnimation {
        id: releaseanimation

        // Expand the button
        //        PropertyAnimation {
        //            target: controlBt
        //            property: "width"
        //            to: controlBt.width + 5
        //            duration: 100
        //            easing.type: Easing.Linear
        //        }
        PropertyAnimation {
            target: primaryButton
            property: "color"
            from: viewset.focusColor
            to: viewset.primaryColor
            duration: 600
        }
    }
}



