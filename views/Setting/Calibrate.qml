import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15
import QtGraphicalEffects 1.12
import QtQuick.Window 2.14
import "../Utiles"
import "../Components"
import "../Setting"
import KAST.Logic 1.0




Item {
    id: root
    visible: true
    width: 1280
    height: 800

    property int weightedCount: 0


    property Logic obj_LogicCalibrate

    ViewSettings{
        id:viewset
    }

    Image {
        id: q
        source: "../../Assets/AuthenticationBackground.png"
        anchors.fill: parent
    }

    Text {
        text: obj_LogicCalibrate.lang.txt_Poor
        x:270
        y:132
        font.pixelSize: 16
        color: "gray"
    }
    Text {
        text: obj_LogicCalibrate.lang.txt_Infficient
        x:352
        y:132
        font.pixelSize: 16
        color: "gray"
    }
    Text {
        text: obj_LogicCalibrate.lang.txt_Adequate
        x:454
        y:132
        font.pixelSize: 16
        color: "gray"
    }
    Text {
        text: obj_LogicCalibrate.lang.txt_Good
        x:597
        y:132
        font.pixelSize: 16
        color: "gray"
    }
    Text {
        text: obj_LogicCalibrate.lang.txt_Great
        x:707
        y:132
        font.pixelSize: 16
        color: "gray"
    }
    Text {
        text: obj_LogicCalibrate.lang.txt_Excellent
        x:791
        y:132
        font.pixelSize: 16
        color: "gray"
    }
    Text {
        text: obj_LogicCalibrate.lang.txt_Perfect
        x:917
        y:132
        font.pixelSize: 16
        color: "gray"
    }
    Text {
        text: obj_LogicCalibrate.lang.txt_Fantastic
        x:1005
        y:132
        font.pixelSize: 16
        color: "gray"
    }
    ProgressBar {
        id:progressBar
        value: 0.125 * weightedCount
        width: 880
        height: 16
        x:196
        y:162

        background: Rectangle {
            anchors.fill: progressBar
            color: "white"
            radius: 10
            border.width: 0
            border.color: "white"
        }
        contentItem:
            Item {
            implicitWidth: 200
            implicitHeight: 4
            Rectangle {
                anchors.left: progressBar.left
                anchors.bottom: progressBar.bottom
                height: progressBar.height
                width: progressBar.width * (progressBar.value)
                color: "#4696FA"
                radius: 10

            }

        }
    }

    Rectangle{
        x:196
        y:226
        width: 384
        height: 70
        Rectangle{
            anchors.left: parent.left
            width: 128
            height: parent.height
            color: "#F08C5A"

            Text {
                id:txt_Unit
                text: qsTr("gr")
                anchors.verticalCenter: parent.verticalCenter
                anchors.horizontalCenter: parent.horizontalCenter
                font.pixelSize: 24
                color: "white"
            }
        }
        Text {
            text: obj_LogicCalibrate.lang.txt_Change_Unit
            x:160
            anchors.verticalCenter: parent.verticalCenter
            font.pixelSize: 20
        }
        Image {
            source: "../../Assets/menu.png"
            anchors.verticalCenter: parent.verticalCenter
            x:344

        }
        MouseArea{
            anchors.fill:parent
            onClicked: {
                if(txt_Unit.text === "gr"){
                    txt_Unit.text = "oz"
                    obj_LogicCalibrate.settingPage.weightsensor.changeUnit("oz");
                }
                else{
                    txt_Unit.text = "gr"
                    obj_LogicCalibrate.settingPage.weightsensor.changeUnit("gr");
                }
            }
        }
        radius: 5
    }

    Rectangle{
        id:rect_insertWeight
        x:196
        y:336
        width: 384
        height: 70
        Rectangle{
            id:input_enterEmail
            //anchors.horizontalCenter: parent.horizontalCenter
            x:2
            y: 5
            width: 124
            height: 62
            color: "white"
            radius: 5
            border.color: "#C6C5CE"
            TextInput{
                id:txt_weight
                anchors.fill: parent
                font.pixelSize: 20
                layer.enabled: true
                x:50
                verticalAlignment:  TextInput.AlignVCenter
                font.family: viewset.danaFuNumFont
                property string placeholderText: obj_LogicCalibrate.lang.txt_weight

                Text {
                    text: txt_weight.placeholderText
                    color: "#C6C5CE"
                    visible: !txt_weight.text
                    font.pixelSize: 18
                    anchors.verticalCenter: parent.verticalCenter
                    x:50
                    anchors.horizontalCenter: parent.horizontalCenter
                    font.family: viewset.danaFuNumFont
                }
            }
        }
        Text {
            text: obj_LogicCalibrate.lang.txt_Enter_Weight
            x:160
            anchors.verticalCenter: parent.verticalCenter
            font.pixelSize: 20
        }
        Image {
            //source: "../../Assets/menu.png"
            anchors.verticalCenter: parent.verticalCenter
            x:344
        }
        radius: 5
    }

    Numpad{
        anchors.right: rect_insertWeight.right
        anchors.top: rect_insertWeight.bottom
        anchors.topMargin: 10
        inputtext: txt_weight
        Rectangle{
            width: 100
            height: 50
            anchors.bottomMargin: 40
            color: white
            anchors.right: parent.left
            anchors.bottom:parent.bottom
                Text{
                    text: "."
                    anchors.verticalCenter: parent.verticalCenter
                    anchors.horizontalCenter: parent.horizontalCenter
                }
                MouseArea{
                    anchors.fill: parent
                    onClicked: {
                        var i = txt_weight.text.indexOf(".")
                        if(i === -1){
                            txt_weight.text += "."
                        }

                    }
                }
        }
    }





    Rectangle {
        width: 471
        height: 180
        color: "#F7F7F7"
        x: 612
        y: 226

        layer.enabled: true
        layer.effect: DropShadow {
            horizontalOffset: 1
            verticalOffset: 1
            radius: 10
            samples: 16
            color: "#d3d3d3"
        }

        Text {
            text: obj_LogicCalibrate.lang.txt_How_to_Calibrating
            width: 226
            height: 26
            anchors.horizontalCenter: parent.horizontalCenter
            y: 26
            color: "#6D6D6D"
            font.family: "Archivo"
            font.pixelSize: 24
            // font.bold: true
        }

        Image {
            source: "../../Assets/1.png"
            width: 30
            height: 30
            x: 51
            y: 76
        }

        Column {
            spacing: -20
            y: 116

            Text {
                text: obj_LogicCalibrate.lang.txt_Select
                width: 50
                height: 44
                x: 41
                font.family: "Archivo"
                color: "#6D6D6D"
                font.pixelSize: 16
            }

            Text {
                text: obj_LogicCalibrate.lang.txt_unit
                width: 50
                height: 44
                x: 50
                font.family: "Archivo"
                color: "#6D6D6D"
                font.pixelSize: 16
            }
        }

        Image {
            source: "../../Assets/2.png"
            width: 30
            height: 30
            x: 151.5
            y: 76
        }

        Column {
            spacing: -20
            y: 116

            Text {
                text: obj_LogicCalibrate.lang.txt_Select
                width: 50
                height: 44
                x: 140
                font.family: "Archivo"
                color: "#6D6D6D"
                font.pixelSize: 16
            }

            Text {
                text: obj_LogicCalibrate.lang.txt_weight
                width: 50
                height: 44
                x: 140
                font.family: "Archivo"
                color: "#6D6D6D"
                font.pixelSize: 16
            }
        }

        Image {
            source: "../../Assets/3.png"
            width: 30
            height: 30
            x: 268.5
            y: 76
        }

        Column {
            spacing: -20
            y: 116

            Text {
                text: obj_LogicCalibrate.lang.txt_put_weight
                width: 50
                height: 44
                x: 242
                font.family: "Archivo"
                color: "#6D6D6D"
                font.pixelSize: 16
            }

            Text {
                text: obj_LogicCalibrate.lang.txt_in_the_cart
                width: 50
                height: 44
                x: 242
                font.family: "Archivo"
                color: "#6D6D6D"
                font.pixelSize: 16
            }
        }

        Image {
            source: "../../Assets/4.png"
            width: 30
            height: 30
            x: 387.5
            y: 76
        }

        Column {
            spacing: -20
            y: 116

            Text {
                text: obj_LogicCalibrate.lang.txt_Hold_to
                width: 50
                height: 44
                x: 374
                font.family: "Archivo"
                color: "#6D6D6D"
                font.pixelSize: 16
            }

            Text {
                text: obj_LogicCalibrate.lang.txt_realize
                width: 50
                height: 44
                x: 374
                font.family: "Archivo"
                color: "#6D6D6D"
                font.pixelSize: 16
            }
        }
    }

    Button {
        id: btn_release
        x:612
        y:430
        width: 471
        height: 112
        Rectangle{
            id:hold_progress
            width: 0
            height: parent.height
            color: "#4696FA"
            opacity: 1
        }
        Text {
            text: obj_LogicCalibrate.lang.btn_Hold_to_Realize
            font.pixelSize: 24
            anchors.verticalCenter: parent.verticalCenter
            anchors.horizontalCenter: parent.horizontalCenter
            color: "white"
        }
        background: Rectangle{
            anchors.fill: parent
            color: "#4696FA"
            opacity: 0.7
        }



        Timer {
            id: longPressTimer
            property real w: 0
            interval: 200 //your press-and-hold interval here
            repeat: true
            running: false

            onTriggered: {
                if(hold_progress.width > 471){
                    longPressTimer.running = false;
                    hold_progress.width = 0
                    w = 0
                    if(root.weightedCount === 0)
                    {
                        obj_LogicCalibrate.settingPage.weightsensor.setWeightZero();
                        root.weightedCount = root.weightedCount + 1
                    }
                    else{

                        obj_LogicCalibrate.settingPage.weightsensor.setWeightW1(txt_weight.text);
                        root.weightedCount = root.weightedCount +1

                    }
                }
                else
                {
                    hold_progress.width = w

                }
                w=w+(471 /10)
            }
        }


        onPressedChanged: {
            if ( pressed ) {
                longPressTimer.running = true;
            } else {
                longPressTimer.running = false;
                hold_progress.width = 0
                longPressTimer.w = 0
            }
        }
    }


    KButton{
        id:btn_save
        width: 471
        height: 80
        x:612
        y:566
        borderRadius: 6
        text: obj_LogicCalibrate.lang.btn_Save
        onClicked: {
            obj_LogicCalibrate.settingPage.weightsensor.saveCalibration();
            obj_LogicCalibrate.settingPage.save_calibrationClicked()
            btn_save.btn_color = "#4696FA"
            stackview.pop()
        }
    }
    Label{
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.verticalCenter: parent.verticalCenter
        text: ""+obj_LogicCalibrate.settingPage.weightsensor.currentweight+" گرم"
        visible: false
    }

    TopNav{
        backvisible: true
        onBackClicked: {
            stackview.pop()
        }

    }
}










