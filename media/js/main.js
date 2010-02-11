$(document).ready(function(){

    $("#navigation > ul > li").mouseover(function(e){
        $(this).addClass("ui-state-hover");
    });

    $("#navigation > ul > li").mouseout(function(e){
        $(this).removeClass("ui-state-hover");
    });

    $("#navigation > ul > li").click(function(e){
        target_url = $(this).find("a").attr("href");
        window.location = target_url;
    });
});
