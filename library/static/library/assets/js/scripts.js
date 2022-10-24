
(function($) {
    "use strict";

    /*================================
    API
    ==================================*/

    /*================================
    Preloader
    ==================================*/
    var preloader = $('#preloader');
    $(window).on('load', function() {
        setTimeout(function() {
            preloader.fadeOut('slow', function() { $(this).remove(); });
        }, 300)
    
    });

    
    /*================================
    sidebar collapsing
    ==================================*/
    if (window.innerWidth <= 1364) {
        $('.page-container').addClass('sbar_collapsed');
    }
    $('.nav-btn').on('click', function() {
        $('.page-container').toggleClass('sbar_collapsed');
    });

    /*================================
    Start Footer resizer
    ==================================*/
    var e = function() {
        var e = (window.innerHeight > 0 ? window.innerHeight : this.screen.height) - 5;
        (e -= 67) < 1 && (e = 1), e > 67 && $(".main-content").css("min-height", e + "px")
    };
    $(window).ready(e), $(window).on("resize", e);

    /*================================
    sidebar menu
    ==================================*/
    $("#menu").metisMenu();

    /*================================
    slimscroll activation
    ==================================*/
    $('.menu-inner').slimScroll({
        height: 'auto'
    });
    $('.nofity-list').slimScroll({
        height: '435px'
    });
    $('.timeline-area').slimScroll({
        height: '500px'
    });
    $('.recent-activity').slimScroll({
        height: 'calc(100vh - 114px)'
    });
    $('.settings-list').slimScroll({
        height: 'calc(100vh - 158px)'
    });

    /*================================
    stickey Header
    ==================================*/
    $(window).on('scroll', function() {
        var scroll = $(window).scrollTop(),
            mainHeader = $('#sticky-header'),
            mainHeaderHeight = mainHeader.innerHeight();

        // console.log(mainHeader.innerHeight());
        if (scroll > 1) {
            $("#sticky-header").addClass("sticky-menu");
        } else {
            $("#sticky-header").removeClass("sticky-menu");
        }
    });

    /*================================
    form bootstrap validation
    ==================================*/
    $('[data-toggle="popover"]').popover()

    /*------------- Start form Validation -------------*/
    window.addEventListener('load', function() {
        // Fetch all the forms we want to apply custom Bootstrap validation styles to
        var forms = document.getElementsByClassName('needs-validation');
        // Loop over them and prevent submission
        var validation = Array.prototype.filter.call(forms, function(form) {
            form.addEventListener('submit', function(event) {
                if (form.checkValidity() === false) {
                    event.preventDefault();
                    event.stopPropagation();
                }
                form.classList.add('was-validated');
            }, false);
        });
    }, false);


    /*================================
    datatable active
    ==================================*/
    let table = $('#dataTable').DataTable({
    processing: true,
    serverSide: true,
    'ajax': {
        'url':'/api/v1/emprestimos/?format=datatables',
        'type': 'GET',
    },

    'columns': [
        {'data': 'id'},
        {'data': 'aluno.nome'},
        {'data': 'livro.titulo'},
        {'data': 'data_criacao'},
        {
            'data': 'situacao',
            "render": function (data, type, row, meta) {
                if (type==='display'){
                    if (data==='fechado'){
                        return '<td><span class="status-p bg-warning">'+data+'</span></td>' 
                    }
                    else {
                        return '<td><span class="status-p bg-success">'+data+'</span></td>' 
                    };
                }
                else {
                    return data
                }
            }
        },
        {
            "data":null,
            "defaultContent": '<button type="button" class="btn btn-info" id="btn-edit">Edit</button>'
        }
    ],
    });

    /*================================
    EDIT ACTION 
    ==================================*/
    let id = 0;
    let type =  ""
    $('#dataTable tbody').on('click', 'button', function (e) {
        let data = table.row($(this).parents('tr')).data();
        let class_name = $(this).attr('class');
        console.log(data)
  
        // EDIT
        if ("btn btn-info" == class_name){
            // PREENCHER O FORMS 
            $('#aluno').val(data.aluno.matricula);
            $('#livro').val(data.livro.titulo);
            $('#situacao').val(data.situacao);
            type = "edit";
            $('#modal-title').text(`EDIT Empréstimo - ${data.id}`);
            $("#myModal").modal();
        }
        id = data.id;
    })
    $('#btn-new').on('click', function (e){
        // REMOVE DEA
        // RESET FORM
        $('#aluno').val("");
        $('#livro').val("");
        $('#situacao').val("aberto");
        $('#situacao').attr("disabled", "disabled");
        type="new";
        $('#modal-title').text(`NEW Empréstimo`);
        $("#myModal").modal();
    })
        
    
    /*================================
    GET CSRF TOKEN
    ==================================*/
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }


    
    /*================================
    PUT, POST on SUBMIT FORM
    ==================================*/
    $('form').on('submit', function (e) {
        e.preventDefault();
        const $form = $(this);
        let method = "";
        let url = "/api/v1/emprestimos/";
        
        console.log(type)
        if (type==="edit"){
            method = "PUT";
            url = url+id+"/"
        }
        else if (type==="new"){
            method = "POST";
        }

        const data = $form.serialize();
        const csrftoken = getCookie('csrftoken')
        console.log(data)
        $.ajax({
            type: method,
            url: url,
            headers: {'X-CSRFToken': csrftoken},
            mode: 'same-origin',
            data: data,
            
            success: function (response) {
                $("#myModal").modal("hide");
                table.ajax.reload()
            },

            error: function(response){
                console.log(response)
                alert('Erro ao se conectar');
              }
        });
        
    });

    /*================================
    Slicknav mobile menu
    ==================================*/
    $('ul#nav_menu').slicknav({
        prependTo: "#mobile_menu"
    });

    /*================================
    login form
    ==================================*/
    $('.form-gp input').on('focus', function() {
        $(this).parent('.form-gp').addClass('focused');
    });
    $('.form-gp input').on('focusout', function() {
        if ($(this).val().length === 0) {
            $(this).parent('.form-gp').removeClass('focused');
        }
    });

    /*================================
    slider-area background setting
    ==================================*/
    $('.settings-btn, .offset-close').on('click', function() {
        $('.offset-area').toggleClass('show_hide');
        $('.settings-btn').toggleClass('active');
    });

    /*================================
    Owl Carousel
    ==================================*/
    function slider_area() {
        var owl = $('.testimonial-carousel').owlCarousel({
            margin: 50,
            loop: true,
            autoplay: false,
            nav: false,
            dots: true,
            responsive: {
                0: {
                    items: 1
                },
                450: {
                    items: 1
                },
                768: {
                    items: 2
                },
                1000: {
                    items: 2
                },
                1360: {
                    items: 1
                },
                1600: {
                    items: 2
                }
            }
        });
    }
    slider_area();

    /*================================
    Fullscreen Page
    ==================================*/

    if ($('#full-view').length) {

        var requestFullscreen = function(ele) {
            if (ele.requestFullscreen) {
                ele.requestFullscreen();
            } else if (ele.webkitRequestFullscreen) {
                ele.webkitRequestFullscreen();
            } else if (ele.mozRequestFullScreen) {
                ele.mozRequestFullScreen();
            } else if (ele.msRequestFullscreen) {
                ele.msRequestFullscreen();
            } else {
                console.log('Fullscreen API is not supported.');
            }
        };

        var exitFullscreen = function() {
            if (document.exitFullscreen) {
                document.exitFullscreen();
            } else if (document.webkitExitFullscreen) {
                document.webkitExitFullscreen();
            } else if (document.mozCancelFullScreen) {
                document.mozCancelFullScreen();
            } else if (document.msExitFullscreen) {
                document.msExitFullscreen();
            } else {
                console.log('Fullscreen API is not supported.');
            }
        };

        var fsDocButton = document.getElementById('full-view');
        var fsExitDocButton = document.getElementById('full-view-exit');

        fsDocButton.addEventListener('click', function(e) {
            e.preventDefault();
            requestFullscreen(document.documentElement);
            $('body').addClass('expanded');
        });

        fsExitDocButton.addEventListener('click', function(e) {
            e.preventDefault();
            exitFullscreen();
            $('body').removeClass('expanded');
        });
    }
    

})(jQuery);

