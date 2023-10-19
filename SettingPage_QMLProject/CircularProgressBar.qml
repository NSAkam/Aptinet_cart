import QtQuick 2.9

Item {
    id: root

    property color maincolor: "#F4AE8B"
    property color secondcolor: "#F08C5A"
    property real value: 0
    property alias degree: canv.degree

    width: 176
    height: 176


    Canvas {
        id: canv

        property real degree: 0

        anchors.fill: parent
        antialiasing: true

        onDegreeChanged: requestPaint()

//        property int archx: root.width / 2
//        property int archy: root.height / 2
//        property int radius: 70
//        property int startAngle: (Math.PI/180) * 270
//        property int endAngle: (Math.PI/180) * (270 + 360)
//        property real progressAngle: (Math.PI/180) * (270 + (degree * 360))


        onPaint: {

            var ctx = canv.getContext('2d')
            var archx = root.width / 2
            var archy = root.height / 2
            var radius = (176 / 2) - 15
            var startAngle = (Math.PI / 180) * 270
            var endAngle = (Math.PI / 180) * (270 + 360)
            var progressAngle = (Math.PI / 180) * (270 + (degree * 360))

            ctx.reset()

            ctx.lineCap = 'butt' // "round" is better
            ctx.lineWidth = 20

            ctx.beginPath()
//            ctx.arc(canv.archx, canv.archy, canv.radius, canv.startAngle, canv.endAngle)
            ctx.arc(archx, archy, radius, startAngle, endAngle)
            ctx.strokeStyle = maincolor
            ctx.stroke()

            ctx.beginPath()
            ctx.arc(archx, archy, radius, startAngle, progressAngle)
//            ctx.arc(canv.archx, canv.archy, canv.radius, canv.startAngle, canv.progressAngle)
            ctx.strokeStyle = secondcolor
            ctx.stroke()

        }

        Behavior on degree {
            NumberAnimation {
                duration: 100000
                from: 0
                to: degree
                running: true

            }
        }

    }

}


