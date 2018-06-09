$(function () {
    $(".dashboard-grid").sortable({
      revert: true
    });
    $(".widget").each(function(index){
        $(this).load("/widgets/" + $(this).attr("widget") + "/", function () {
            $(this).resizable();
        });

    });
});

