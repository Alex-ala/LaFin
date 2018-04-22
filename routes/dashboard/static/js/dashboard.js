$(function () {
    $(".dashboard-grid").sortable({
      revert: true
    });
    $(".widget").resizable();
    $(".widget").each(function(index){
        $(this).load("/widgets/"+$(this).attr("widget"))
    });
});