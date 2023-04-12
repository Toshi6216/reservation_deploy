//https://www.jsdelivr.com/package/npm/fullcalendar?version=6.1.4
//fullcalendar CDNひな形をもとにカスタマイズ
// CSRF対策
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"
axios.defaults.xsrfCookieName = "csrftoken"

document.addEventListener('DOMContentLoaded', function() {
    const calendarEl = document.getElementById('calendar')
    const calendar = new FullCalendar.Calendar(calendarEl, {
      initialView: 'dayGridMonth',
      

    });
    calendar.render();
  });