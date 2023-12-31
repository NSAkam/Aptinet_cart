import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15
import QtGraphicalEffects 1.12
import QtQuick.Window 2.14
import "../Components"
import "../PopUps"
import KAST.Logic 1.0

Item{
    id: root
    visible: true
    width: 1280
    height: 800
    property Logic obj_LogicContainer

    Image {
        id: q
        source: "../../Assets/AuthenticationBackground.png"
        anchors.fill: parent
    }

    Rectangle {
        width: 672
        height: 86
        color: "white"
        x: 304
        y: 272
        layer.enabled: true
        layer.effect: DropShadow {
            horizontalOffset: 1
            verticalOffset: 1
            radius: 10
            samples: 16
            color: "#d3d3d3"
        }

        Text {
            text: obj_LogicContainer.lang.txt_Software_Version
            width: 160
            height: 22
            x: 24
            y: 32
            color: "#1D1D1D"
            font.pixelSize: 20
            font.family: "Archivo"
        }

        Text {
            text: obj_LogicContainer.settingPage.configs.appVersion
            width: 30
            height: 22
            x: 502
            y: 32
            color: "#6D6D6D"
            font.pixelSize: 20
            font.family: "Archivo"
        }
        KBorderButton{
            id:btn_update
            width: 92
            height: 38
            x: 556
            y: 24
            text: obj_LogicContainer.lang.txt_Update
            pixelSize: 20
            textColor: "#4696FA"
            bordercolor: "#4696FA"
            visible: false
            MouseArea{
                anchors.fill: parent
                onClicked: {
                    stackview.push(updatePage)

                }
            }
        }
    }

    Rectangle {
        width: 672
        height: 0.1
        x: 303
        y: 358
        color: "#9D9D9D"
    }

    Rectangle {
        width: 672
        height: 86
        color: "white"
        x: 304
        y: 360
        layer.enabled: true
        layer.effect: DropShadow {
            horizontalOffset: 1
            verticalOffset: 1
            radius: 10
            samples: 16
            color: "#d3d3d3"
        }

        Text {
            text: obj_LogicContainer.lang.txt_unit
            width: 39
            height: 22
            x: 24
            y: 32
            color: "#1D1D1D"
            font.pixelSize: 20
        }

        Text {
            text: obj_LogicContainer.settingPage.configs.quatifire
            width: 25
            height: 22
            x: 502
            y: 32
            color: "#6D6D6D"
            font.pixelSize: 20
        }

        KBorderButton{
            width: 92
            height: 38
            x: 556
            y: 24
            text: obj_LogicContainer.lang.btn_Change
            pixelSize: 20
            textColor: "#4696FA"
            bordercolor: "#4696FA"
            MouseArea{
                anchors.fill: parent
                onClicked: {
                    toggleRectangles();
                }
            }
        }


    }

    Rectangle {
        width: 672
        height: 1
        x: 303
        y: 446
        color: "#9D9D9D"
    }

    Rectangle {
        width: 672
        height: 86
        color: "white"
        x: 304
        y: 448
        layer.enabled: true
        layer.effect: DropShadow {
            horizontalOffset: 1
            verticalOffset: 1
            radius: 10
            samples: 16
            color: "#d3d3d3"
        }

        Text {
            text: obj_LogicContainer.lang.txt_Tax_Value
            width: 152
            height: 22
            x: 24
            y: 32
            color: "#1D1D1D"
            font.pixelSize: 20
        }

        Text {
            text: obj_LogicContainer.settingPage.configs.taxPercentage + " %"
            width: 107
            height: 22
            x: 502
            y: 32
            color: "#6D6D6D"
            font.pixelSize: 20
        }
        KBorderButton{
            width: 92
            height: 38
            x: 556
            y: 24
            text: obj_LogicContainer.lang.btn_Change
            pixelSize: 20
            textColor: "#4696FA"
            bordercolor: "#4696FA"
            MouseArea{
                anchors.fill: parent
                onClicked: {
                    insertPopUp.open()
                }
            }
        }

    }
    Rectangle {
        width: 672
        height: 1
        x: 303
        y: 446+86
        color: "#9D9D9D"
    }

    Rectangle {
        width: 672
        height: 86
        color: "white"
        x: 304
        y: 448+86
        layer.enabled: true
        layer.effect: DropShadow {
            horizontalOffset: 1
            verticalOffset: 1
            radius: 10
            samples: 16
            color: "#d3d3d3"
        }

        Text {
            text: obj_LogicContainer.lang.txt_Calibration_Date
            width: 152
            height: 22
            x: 24
            y: 32
            color: "#1D1D1D"
            font.pixelSize: 20
        }

        Text {
            id:txt_last_calibrate
            text: obj_LogicContainer.settingPage.lastCalibrationDate
            width: 107
            height: 22
            x: 433
            y: 32
            color: "#6D6D6D"
            font.pixelSize: 20
        }

        Text {
            id:txt_expired
            text: obj_LogicContainer.lang.txt_Expired
            width: 73
            height: 22
            x: 567
            y: 32
            color: "#F08C5A"
            font.pixelSize: 20
        }
    }

    Rectangle {
        id: rectangle2
        radius: 2
        width: 64
        height: 60
        x: 1000
        y: 361
        color: "white"
        visible: false
        layer.enabled: true
        layer.effect: DropShadow {
            horizontalOffset: 1
            verticalOffset: 1
            radius: 10
            samples: 16
            color: "#d3d3d3"
        }

        Text {
            text: "kg"
            font.pixelSize: 24
            color: "#9D9D9D"
            x: 20
            y: 16
        }
        MouseArea{
            anchors.fill: parent
            onClicked: {
                obj_LogicContainer.settingPage.select_unit("kg")
            }
        }
    }

    Rectangle {
        id: separator2
        width: 64
        height: 1
        x: 1000
        y: 420
        color: "#9D9D9D"
        visible: false
    }

    Rectangle {
        id: rectangle3
        radius: 2
        width: 64
        height: 60
        x: 1000
        y: 421
        color: "white"
        visible: false
        layer.enabled: true
        layer.effect: DropShadow {
            horizontalOffset: 1
            verticalOffset: 1
            radius: 10
            samples: 16
            color: "#d3d3d3"
        }

        Text {
            text: "lb"
            font.pixelSize: 24
            color: "#9D9D9D"
            x: 20
            y: 16
        }
        MouseArea{
            anchors.fill: parent
            onClicked: {
                obj_LogicContainer.settingPage.select_unit("lb")
            }
        }
    }

    function toggleRectangles() {
        rectangle2.visible = !rectangle2.visible;
        separator2.visible = !separator2.visible;
        rectangle3.visible = !rectangle3.visible;
    }


    Rectangle {
        id: b
        color: "white"
        width: 1280
        height: 708
        visible: true
        opacity: 0
        x: 0
        y: 92

        FastBlur {

            anchors.fill: b
            source: q
            radius: 70
        }
    }

    Component {
        id: updatePage
        SoftwareVersion{
            obj_Logic: obj_LogicContainer
        }
    }

    TopNav{
        backvisible: true
        onBackClicked: {
            stackview.pop()
        }
    }
    Connections{
        target:obj_LogicContainer.settingPage
        function onUpdateAvailableSignal(){
            btn_update.visible = true
        }
    }

    InsertPupUp{
        id:insertPopUp
        obj_settingLogicInsertPopUp: obj_LogicContainer
        title: obj_LogicContainer.lang.txt_Insert_Tax
        onClosePup: {
            insertPopUp.close()
        }
        onEnter:function (text) {
            insertPopUp.close()
            obj_LogicContainer.settingPage.change_tax(text)
        }
    }

    Connections{
        target:obj_LogicContainer.settingPage
        function onExpiredCalibrationSignal(v){
            if(v === true)
            {
                txt_expired.visible =true
                txt_last_calibrate.x =433

            }
            else{
                txt_expired.visible = false
                txt_last_calibrate.x =550
            }
        }
    }
}
