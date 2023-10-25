import QtQuick 2.15
import QtQuick.Controls 2.15
import QtGraphicalEffects 1.15
import QtQuick.Window 2.0
import "../Components"
import "../Containers"
import "../Utiles"

Popup {
  id: root
  width: 1280
  height: 800
  modal: true
  focus: true

  background:
      Rectangle {
      color: "black"
      opacity: 0.4
      x: 0
      y: 0
      width: parent.width
      height: parent.height
  }

  Rectangle {
      x: 818 + 390
      y: 32
      radius: 4
      color: "white"
      width: 40
      height: 40

      Image {
          source: "../../Assets/alarm.png"
          width: 18
          height: 20
          anchors.centerIn: parent
      }
  }


  Column {
      spacing: 16
      y: 186
      x: 66 + 390/2

      Rectangle {
          id: notifrect
          width: 758
          height: 72
          radius: 4

          LinearGradient {
            anchors.fill: parent
            start: Qt.point(0, 10)
            end: Qt.point(72, 60)
            gradient: Gradient {
              GradientStop { position: 0.5417; color: "#F08C5A" }
              GradientStop { position: 1.0; color: "#F05A28" }
            }
          }

          Text {
              anchors.fill: notifrect
              text: qsTr("Are you sure to remove the products?")
              font.bold: true
              font.pixelSize: 24
              horizontalAlignment: Text.AlignHCenter
              verticalAlignment: Text.AlignVCenter
              color: "white"
          }
      }

      Rectangle {
          width: 758
          height: 268
          color: "white"
          Image {
              source: "../../Assets/product.png"
              x: 41
              y: 41
              width: 90
              height: 90
          }
          Text {
              text: qsTr("Doritos Tortilla Chips,\nTapatio, 9.75 oz")
              x: 180
              y: 40
              font.pixelSize: 24
              font.weight: Font.DemiBold
              color: "black"
              font.letterSpacing: 0.04 * 24
              lineHeight: 1.5
          }

          Text {
              text: qsTr("Qty:")
              x: 647
              y: 48
              font.pixelSize: 20
//              font.weight: Font.DemiBold
              color: "#6D6D6D"
          }

          Text {
              text: qsTr("4")
              x: 695
              y: 45
              font.pixelSize: 24
              font.weight: Font.Bold
              color: "#F08C5A"
          }

          Text {
              text: qsTr("$ 8.00")
              x: 615
              y: 102
              font.pixelSize: 24
              font.weight: Font.Bold
              color: viewset.primaryColor
          }

          KButton {
              width: 350
              height: 64
              borderRadius: 4
              y: 188
              x: 16
              text: "Cancel"
              btn_color: "#F08C5A"
              isBold: false
              fontsize: 24
          }

          KButton {
              width: 350
              height: 64
              borderRadius: 4
              y: 188
              x: 382
              text: "Confirm"
              btn_color: viewset.secondaryColor
              btn_bordercolor: viewset.secondaryColor
              isBold: false
              fontsize: 24
              font.weight: Font.DemiBold
          }

      }
  }
}



