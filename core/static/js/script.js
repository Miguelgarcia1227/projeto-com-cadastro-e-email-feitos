document.addEventListener('DOMContentLoaded', function() {
    const bt3 = document.getElementById('bt3');
    const modal_id = document.getElementById('modal_id');
    const timeDuration = 5000;

    bt3.addEventListener('click', function(event) {
        event.preventDefault();
        modal_id.style.display = modal_id.style.display === 'block' ? 'none' : 'block';
    
        if (modal_id.style.display === 'block') {
            setTimeout(function() {
                modal_id.style.display = 'none';
            }, timeDuration )
        }
    
    });
});


document.addEventListener('click', function(event) {
    if (!bt3.contains(event.target) && !modal_id.contains(event.target)) {
        modal_id.style.display = 'none';
    }
});




const menu = document.getElementById('menu');
const imgHeader = document.getElementById('img_principal');
const height = document.getElementById('menu')

function fixarMenu() {
    if (window.scrollY > menu.offsetTop) {
        menu.classList.add('fixed');
        imgHeader.style.display = 'none';
    } else {
        menu.classList.remove('fixed');
        imgHeader.style.display = 'block';
    }
}

window.addEventListener('scroll', fixarMenu);

document.addEventListener('DOMContentLoaded', function() {
    const bt_logar = document.getElementById('id_bt_logar');
    const id_modal = document.getElementById('id_Login');
    const timeDuration = 5000;

    bt_logar.addEventListener('click', function(event) {
        event.preventDefault();
        id_modal.style.display = id_modal.style.display === 'block' ? 'none' : 'block';
    
        if (id_modal.style.display === 'block') {
            setTimeout(function() {
                id_modal.style.display = 'none';
            }, timeDuration )
        }
    
    });
});

document.addEventListener('click', function(event) {
    if (!bt_logar.contains(event.target) && !id_modal.contains(event.target)) {
        id_modal.style.display = 'none';
    }
});




const btPreco = document.getElementById('bt_agendar_modal');
const modalPreco = document.getElementById('container__modal');
const bt_fechar = document.getElementById('bt_fechar');

btPreco.addEventListener('click', function(event) {
    event.preventDefault();
    modalPreco.style.display = modalPreco.style.display === 'block' ? 'none' : 'block';

    if (modalPreco.style.display ===   'block') {
        setTimeout(function() {
            modalPreco.style.display = 'none';
        }, timeDuration)
    }
});

bt_fechar.addEventListener('click', function(event) {
    event.preventDefault();
    modalPreco.style.display = 'none';
})

document.addEventListener('click', function(event) {
    if(!btPreco.contains(events.target) && !modalPreco.contains(event.target)) {
        modalPreco.style.display = 'none';
    }
});
