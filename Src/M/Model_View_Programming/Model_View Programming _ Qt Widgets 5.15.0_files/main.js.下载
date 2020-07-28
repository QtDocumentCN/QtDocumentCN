"use strict";
var $sidebar;
var sticky = false;

function createCookie(name, value, days, root) {
    var params = "";
    if (days) {
        var date = new Date();
        date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
        params = "; expires=" + date.toGMTString();
    }
    if (root)
        params += "; path=/";
    document.cookie = escape(name) + "=" + escape(value) + params;
}

function readCookie(name) {
    var nameEQ = escape(name) + "=";
    var ca = document.cookie.split(';');
    for (var i = 0; i < ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0) === ' ') c = c.substring(1, c.length);
        if (c.indexOf(nameEQ) === 0) return unescape(c.substring(nameEQ.length, c.length));
    }
    return null;
}

$(document).ready(function($) {
    $sidebar = $('div.sidebar:first');
    sticky = $sidebar.css('position') == 'sticky';
    if (sticky)
        $sidebar.css({transition: '0.2s ease-out'});
    $(window).scroll(function() {
        oneQt.stickySidebar();
        oneQt.stickyHeader();
    });

    oneQt.stickySidebar();
    $(window).resize(function() {
        setTimeout(function(){oneQt.stickySidebar();}, 80);
    });
    $("#navbar").load("/style/qt-header.html");
    $("#sidebar-content").load("style/qt5-sidebar.html");
    $.get('.exclude-promos').fail(function() {
        $.get("/style/qt-sidebar.html", function(d) {
            if (document.getElementById("sidebar-content")) {
                var content = $(d).filter('div');
                $("#sidebar-content").before(content);
                $("#footer").load("/style/qt-footer-clean.html");
            } else {
                $("#footer").load("/style/qt-footer.html");
            }
        }).fail(function() {
            $("#footer").load("/style/qt-footer.html");
        });
    }).done(function() {
        $("#footer").load("/style/qt-footer-clean.html");
    });
});

var oneQt = {
    stickySidebar: function() {
        if ($sidebar.length && $sidebar.outerHeight() > 20) {
            var $win = $(window);
            var $sidebarContainer = $sidebar.parent();
            var headerHeight = 0;
            if ($('#navbar').css('position') == 'fixed')
                headerHeight = $('#navbar').outerHeight();
            if ($win.outerWidth() > 980
                && $win.scrollTop() + headerHeight > $sidebarContainer.offset().top) {
                var newTop = 16 + headerHeight + $win.scrollTop() - $sidebarContainer.offset().top;
                var overflow = $sidebar.innerHeight() - $win.outerHeight() + headerHeight;
                if (overflow > 0) {
                    newTop -= overflow;
                    if (sticky) {
                        $sidebar.css('top', headerHeight - overflow + 'px');
                        return;
                    }
                }
                if (newTop + $sidebar.innerHeight() > $sidebarContainer.innerHeight()) {
                    newTop = $sidebarContainer.innerHeight() - $sidebar.innerHeight();
                }
                if (newTop < 0)
                    newTop = 0;
                if (sticky)
                    $sidebar.css({top: '66px'});
                else
                    $sidebar.css({top: newTop + 'px'});
            } else {
                $sidebar.css({top: '0'})
            }
        }
    },
    stickyHeader: function () {
        var originalHeaderHeight = 79;
        $('#navbar').toggleClass('fixed', $(window).scrollTop() > originalHeaderHeight);
    }
}
