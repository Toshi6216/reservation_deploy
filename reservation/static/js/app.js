//https://www.jsdelivr.com/package/npm/fullcalendar?version=6.1.4
//fullcalendar CDNひな形をもとにカスタマイズ

document.addEventListener('DOMContentLoaded', function() {
    const calendarEl = document.getElementById('calendar')
    const calendar = new FullCalendar.Calendar(calendarEl, {
      initialView: 'dayGridMonth',
      
      //日付をクリックしたイベント
      selectable: true,
      select: function (info) {
            
            //alert("selected " + info.startStr + " to " + info.endStr);

            // 入力ダイアログ
            const eventName = prompt("イベントを入力してください");

            if (eventName) {
                // イベントの追加
                calendar.addEvent({
                    title: eventName,
                    start: info.start,
                  //  end: info.end,
                    end: info.start,
                    allDay: true,
                });
            }

      },

    })
    calendar.render()
  })