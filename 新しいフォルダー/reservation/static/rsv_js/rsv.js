$(function(){
    
  $('td').on('click',
  function(){
    // $(this).css('background-color', '#ffb6c1');
    // alert('クリックイベントが取得できていれば表示されます。');
    $('.rsv_day').removeClass('table-danger active');
    $('.active_event').addClass('event_hide');
    $('.active_event').removeClass('active_event');
    $(this).addClass('table-danger active');
    
    var active_date = $(this).find('.active').text()
    console.log(active_date);

    // $(active_date).addClass("active_event");
    $('.'+active_date).addClass("active_event");

    // alert(active_date)
    // $('.event_card').find(active_date).show();

  },

  );
  
  $(window).scroll(function () {
    if($(window).scrollTop() > 20) {
      $('nav').addClass('sticky-top');
    } else {
      $('nav').removeClass('sticky-top');
    }
  });
});
// クリックした日付のクラス
  

