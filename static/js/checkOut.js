c_item = document.querySelector('#c_item')
c_item_name = document.querySelector('#c_item_name')
c_price = document.querySelector('#c_price')
c_quan = document.querySelector('#c_quan')
c_c_items = document.querySelector('#c_c_items')
c_c_price = document.querySelector('#c_c_price')


function checkOutDisplay() {
    cart_tr = document.cookie.split(';')
    cart_tra = cart_tr[1].split('=')
    cart_transform = JSON.parse(cart_tra[1])
    console.log(cart_transform)

    c_item_name.innerHTML = ''
    c_price.innerHTML = ''
    c_quan.innerHTML = ''


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

        const item = document.getElementById('c_item')

        item.appendChild(imageDiv)
        imageDiv.appendChild(image)

        c_item_name.innerHTML += '<h5 class = "it_cart" >' + cart_transform[keys]['name'] + '</h5>'
        c_price.innerHTML += '<h5 class = "it_cart" >' + cart_transform[keys]['price'] + '</h5>'
        c_quan.innerHTML += '<h5 id  = "" class = "it_cart" >' + cart_transform[keys]['quantity'] + '</h5>'

    }
}

checkOutDisplay();


function checkout_pagetotals() {
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

    c_items = document.getElementById('c_c_items')
    c_price = document.getElementById('c_c_price')

    cart_it = document.getElementById('c_c_items')
    cart_pr = document.getElementById('c_c_price')

    cart_it.innerHTML = 'Items:' + '' + total_items
    cart_pr.innerHTML = 'Total:' + '' + total_price


}

checkout_pagetotals()

cart_tr = document.cookie.split(';')
cart_tra = cart_tr[1].split('=')
cart_transform = JSON.parse(cart_tra[1])

function submitOrder() {
    var test = "Fetch Api Test"
    var cartData = cart_transform;
    console.log(cartData)

    var url = '/order_processing/'

    fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken,
            },
            body: JSON.stringify(cartData)
        })
        .then((response) => {
            return response.json();
        })

    .then((data) => {
        console.log('Data:', data)
    });

}