var item = document.querySelector('#item')
var item_name = document.querySelector('#item_name')
var price = document.querySelector('#price')
var quan = document.querySelector('#quan')
var total = document.querySelector('#total')

function shoppingCart() {
    cart_tr = document.cookie.split(';')
    cart_tra = cart_tr[1].split('=')
    cart_transform = JSON.parse(cart_tra[1])
    console.log(cart_transform)

    item.innerHTML = ''
    price.innerHTML = ''
    quan.innerHTML = ''
    total.innerHTML = ''

    cart_size = Object.keys(cart_transform)

    for (var [keys, values] of Object.entries(cart_transform)) {
        const image = document.createElement('img');
        var imageDiv = document.createElement('div')
        imageDiv.setAttribute('id', 'imageDiv');

        image.setAttribute('height', 100)
        image.setAttribute('width', 120)

        image.style.margin = '0px 0px 2px 0px'


        image.onerror = function handleError() {
            console.log('image could not be loaded')
        }

        image.onload = function handleImageload() {
            console.log('image loaded successfully')
        }

        image.src = cart_transform[keys]['location']

        const item = document.getElementById('item')

        item.appendChild(imageDiv)
        imageDiv.appendChild(image)

        item_name.innerHTML += '<h5 class = "it_cart" >' + cart_transform[keys]['name'] + '</h5>'
        price.innerHTML += '<h5 class = "it_cart" >' + cart_transform[keys]['price'] + '</h5>'
        quan.innerHTML += '<h5 id  = "" class = "it_cart" >' + cart_transform[keys]['quantity'] +
            '<span class = "del" onclick = "addItems( ' + cart_transform[keys]['productId'] + ')">+</span>' + ' ' +
            '<span class = "del" onclick = "removeItems( ' + cart_transform[keys]['productId'] + ')">-</div>' + '</button></h5>'

    }
}

shoppingCart();

function addItems(n) {

    cart_tr = document.cookie.split(";")
    cart_tra = cart_tr[1]
    cart_trans = cart_tra.split("=")
    cart_transform = JSON.parse(cart_trans[1])

    item_name.innerHTML = ''
    price.innerHTML = ''
    quan.innerHTML = ''
    total.innerHTML = ''

    console.log(n)

    cart_transform[n]['quantity'] += 1
    cart_transform[n]['price'] += cart_transform[n]['or_price']

    document.cookie = 'cart=' + JSON.stringify(cart_transform) + ";domain=;path = /"

    shoppingCart();
    cart_pagetotals();
    cart_display();

}

function removeItems(n) {

    cart_tr = document.cookie.split(";")
    cart_tra = cart_tr[1]
    cart_trans = cart_tra.split("=")
    cart_transform = JSON.parse(cart_trans[1])

    item_name.innerHTML = ''
    price.innerHTML = ''
    quan.innerHTML = ''
    total.innerHTML = ''

    console.log(n)

    cart_transform[n]['quantity'] -= 1
    cart_transform[n]['price'] -= cart_transform[n]['or_price']

    if (cart_transform[n]['quantity'] <= 0) {
        delete cart_transform[n]
    }

    document.cookie = 'cart=' + JSON.stringify(cart_transform) + ";domain=;path = /"

    shoppingCart();
    cart_pagetotals();
    cart_display();
}

function cart_pagetotals() {
    cart_tr = document.cookie.split(';')
    cart_tra = cart_tr[1].split('=')
    cart_transform = JSON.parse(cart_tra[1])
    console.log(cart_transform)

    var total_items = 0;
    var total_price = 0;
    for ([keys, values] of Object.entries(cart_transform)) {
        total_items += cart_transform[keys]['quantity']
        total_price += cart_transform[keys]['price']
    }

    c_items = document.getElementById('c_items')
    c_price = document.getElementById('c_price')

    cart_it = document.getElementById('c_items')
    cart_pr = document.getElementById('c_price')

    cart_it.innerHTML = 'Items:' + '' + total_items
    cart_pr.innerHTML = 'Total:' + '' + total_price

    console.log(total_items)
    console.log(total_price)
    console.log(total)
}

cart_pagetotals()