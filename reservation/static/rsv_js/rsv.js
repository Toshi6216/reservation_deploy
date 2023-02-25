// document.getElementById("button").onclick = function() {
//     // ここに#buttonをクリックしたら発生させる処理を記述する
//     $('.day').click(function(){
//         $(this).css('background-color', '#ffb6c1');
//     });

//   };

$(function(){
  $('.event_card').addClass('event_hide');
  
  // $('.event_card').find('').addClass("activate_event");
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
});
// クリックした日付のクラス
  

