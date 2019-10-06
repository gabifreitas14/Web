/// <reference path="../../typings/globals/jquery/index.d.ts" />

$(function () {
    $('[data-toggle="tooltip"]').tooltip({boundary: 'window'});

    //sobrancelha

    $("#like-sobrancelha").click(function (e) {
        deuLike(e, "sobrancelha")
    })


    $("#dislike-sobrancelha").click(function (e) {
        deuDislike(e, "sobrancelha")
    })

    //limpeza

    $("#like-limpeza").click(function (e) {
        deuLike(e, "limpeza")
    })


    $("#dislike-limpeza").click(function (e) {
        deuDislike(e, "limpeza")
    })

    //massagem

    $("#like-massagem").click(function (e) {
        deuLike(e, "massagem")
    })

    $("#dislike-massagem").click(function (e) {
        deuDislike(e, "massagem")
    })


    //peeling

    $("#like-peeling").click(function (e) {
        deuLike(e, "peeling")
    })
    $("#dislike-peeling").click(function (e) {
        deuDislike(e, "peeling")
    })

    //drenagem

    $("#like-drenagem").click(function (e) {
        deuLike(e, "drenagem")
    })
    $("#dislike-drenagem").click(function (e) {
        deuDislike(e, "drenagem")
    })

    //depilacao

    $("#like-depilacao").click(function (e) {
        deuLike(e, "depilacao")
    })
    $("#dislike-depilacao").click(function (e) {
        deuDislike(e, "depilacao")
    })


    $("#id-form").submit(function (e) {
        validaTudoFunction(e)
    })


});

function deuLike(e, card) {
    e.preventDefault();
    console.log(e)
    let like = $("#like-" + card);
    let dislike = $("#dislike-" + card);
    let numeroLike = parseInt($('#label-like-' + card).data('like'));
    if (like.hasClass("far fa-thumbs-up")) {
        like.removeClass("far fa-thumbs-up");
        like.addClass("fas fa-thumbs-up");
        $('#label-like-' + card).text(numeroLike + 1);
        $('#label-like-' + card).data('like', numeroLike + 1)

        // labelLike.text(parseInt(labelLike.text()) + 1);
        if (dislike.hasClass("fas fa-thumbs-down")) {
            dislike.removeClass("fas fa-thumbs-down");
            dislike.addClass("far fa-thumbs-down");
            let numeroDislike = parseInt($('#label-dislike-' + card).data('dislike')) - 1;
            $('#label-dislike-' + card).text(numeroDislike);
            $('#label-dislike-' + card).data('dislike', numeroDislike)

            // labelDislike.text(parseInt(labelDislike.text()) - 1)
        }
    } else {
        like.removeClass("fas fa-thumbs-up");
        like.addClass("far fa-thumbs-up");
        $('#label-like-' + card).data('like', numeroLike - 1)
        $('#label-like-' + card).text(numeroLike - 1);
    }
}

function deuDislike(e, cardName) {
    e.preventDefault();
    let like = $("#like-" + cardName);
    let dislike = $("#dislike-" + cardName);
    // let labelLike = $("#label-like");
    // let labelDislike = $("#label-dislike");
    let numeroDislike = parseInt($('#label-dislike-' + cardName).data('dislike'));


    if (dislike.hasClass("far fa-thumbs-down")) {
        dislike.removeClass("far fa-thumbs-down");
        dislike.addClass("fas fa-thumbs-down");
        $('#label-dislike-' + cardName).text(numeroDislike + 1);
        $('#label-dislike-' + cardName).data('dislike', numeroDislike + 1)

        // labelDislike.text(parseInt(labelDislike.text()) + 1);
        if (like.hasClass("fas fa-thumbs-up")) {
            like.removeClass("fas fa-thumbs-up");
            like.addClass("far fa-thumbs-up");
            let numeroLike = parseInt($('#label-like-' + cardName).data('like')) - 1;
            $('#label-like-' + cardName).text(numeroLike);
            $('#label-like-' + cardName).data('like', numeroLike)

        }

    } else {
        dislike.removeClass("fas fa-thumbs-down");
        dislike.addClass("far fa-thumbs-down");
        $('#label-dislike-' + cardName).text(numeroDislike - 1);
        $('#label-dislike-' + cardName).data('dislike', numeroDislike - 1)

    }
}

function validaTudoFunction(e) {
    alert("Começando a Validação");
    e.preventDefault();

    let nome_valido = nomeValidoFunction();
    let tipo_valido = tipoValidoFunction();
    let prazo_valido = prazoValidoFunction();
    let descricao_valida = descricaoValidaFunction();
    let caminho_valido = caminhoValidoFunction();
    let forma_pagamento_valido = formaPagamentoValidaFunction();


    if (nome_valido && tipo_valido && prazo_valido && descricao_valida && caminho_valido && forma_pagamento_valido) {
        alert("Tudo Ok!")
        // $("#id-form").submit()
    } else {
        alert("Deu erro!")
    }
}

function formaPagamentoValidaFunction() {
    let credito = $("#credito");
    let debito = $("#debito");
    let boleto = $("#boleto");

    let feedback_pagamento = $("#feedback-pagamento");

    let botoes = $("input.pagamento:checked");
    if (botoes.length === 0) {
        credito.addClass("is-invalid");
        credito.removeClass("is-valid");
        debito.addClass("is-invalid");
        debito.removeClass("is-valid");
        boleto.addClass("is-invalid");
        boleto.removeClass("is-valid");
        feedback_pagamento.addClass("d-block");
        return false
    } else {
        credito.addClass("is-valid");
        credito.removeClass("is-invalid");
        debito.addClass("is-valid");
        debito.removeClass("is-invalid");
        boleto.addClass("is-valid");
        boleto.removeClass("is-invalid");
        feedback_pagamento.removeClass("d-block");
        return true
    }
}

function tipoValidoFunction() {
    let tipo = $("#tipo");

    if (tipo.val() === '') {
        tipo.addClass("is-invalid");
        tipo.removeClass("is-valid");
        return false
    } else {
        tipo.removeClass("is-invalid");
        tipo.addClass("is-valid");
        return true
    }
}

function prazoValidoFunction() {
    let curto_prazo = $("#curto-prazo");
    let longo_prazo = $("#longo-prazo");

    let prazo_feedback = $("#prazo-feedback");

    let botoes = $("input[name='prazo']:checked");
    if (botoes.length === 0) {
        curto_prazo.addClass("is-invalid");
        curto_prazo.removeClass("is-valid");
        longo_prazo.addClass("is-invalid");
        longo_prazo.removeClass("is-valid");
        prazo_feedback.addClass("d-block");
        return false
    } else {
        curto_prazo.removeClass("is-invalid");
        curto_prazo.addClass("is-valid");
        longo_prazo.removeClass("is-invalid");
        longo_prazo.addClass("is-valid");
        prazo_feedback.removeClass("d-block");
        return true
    }
}

function nomeValidoFunction() {
    let nome = $("#nome");

    if (nome.val() === '') {
        nome.addClass("is-invalid");
        nome.removeClass("is-valid");
        return false
    } else {
        nome.removeClass("is-invalid");
        nome.addClass("is-valid");
        return true
    }
}

function descricaoValidaFunction() {

    let descricao = $("#descricao");

    if (descricao.val() === '') {
        descricao.addClass("is-invalid");
        descricao.removeClass("is-valid");
        return false
    } else {
        descricao.removeClass("is-invalid");
        descricao.addClass("is-valid");
        return true
    }
}

function caminhoValidoFunction() {
    let caminho = $("#caminho-foto");

    if (caminho.val() === '') {
        caminho.addClass("is-invalid");
        caminho.removeClass("is-valid");
        return false
    } else {
        caminho.removeClass("is-invalid");
        caminho.addClass("is-valid");
        return true
    }
}