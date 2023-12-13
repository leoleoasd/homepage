$(".header").click(function () {

    $header = $(this);
    //getting the next element
    $content = $header.next();
    //open up the content needed - toggle the slide- if visible, slide up, if not slidedown.
    $content.slideToggle(500, function () {
        //execute this after slideToggle is done
        //change text of header based on visibility of content div
        $header.text(function () {
            //change text based on condition
            return $content.is(":visible") ? "Collapse" : "Expand";
        });
    });

});

$(document).ready(function () {
    if ($("a.abstract").click(function () {
        $(this).parent().parent().find(".abstract.hidden").toggleClass("open"),
            $(this).parent().parent().find(".bibtex.hidden.open").toggleClass("open")
    }),
        $("a.bibtex").click(function () {
            $(this).parent().parent().find(".bibtex.hidden").toggleClass("open"),
                $(this).parent().parent().find(".abstract.hidden.open").toggleClass("open")
        }),
        $("a").removeClass("waves-effect waves-light"),
        $("#toc-sidebar").length) {
        var e = "#toc-sidebar"
            , t = $(e);
        Toc.init(t),
            $("body").scrollspy({
                target: e
            })
    }
});
