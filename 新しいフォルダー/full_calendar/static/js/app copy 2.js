//https://www.jsdelivr.com/package/npm/fullcalendar?version=6.1.4
//fullcalendar CDNひな形をもとにカスタマイズ
// CSRF対策
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"
axios.defaults.xsrfCookieName = "csrftoken"

document.addEventListener('DOMContentLoaded', function() {
    const calendarEl = document.getElementById('calendar')
    const calendar = new FullCalendar.Calendar(calendarEl, {
      initialView: 'dayGridMonth',
      
      //日付をクリックしたイベント
      selectable: true,
      select: function (info) {
      //eventClick: function(info) {

            // 入力ダイアログ
            const eventName = prompt("イベントを入力してください");

            if (eventName) {
              //登録処理の呼び出し
              axios
                .post("cldr/event_add/", {
                  event_title: eventTitle,
                  event_detail: eventDetail,
                })
                .then(() => {
                  // イベントの追加
                  calendar.addEvent({
                      title: eventName,
                      detail: eventDetail,
                      //event_date: info.start,
                      //end: info.end,
                      allDay: true,
                  });
                })
                .catch(() => {
                  //バリデーションエラーなど
                  alert("登録に失敗しました");
                });
            }

      },

    })
    calendar.render()
  })