var updateBtns = document.getElementsByClassName('add-to')

for (var i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener('click', function() {
        var nam = this.dataset.nam
        var productId = this.dataset.product
        var action = this.dataset.action
        var price = this.dataset.value
        var imageloc = this.dataset.imageloc
        var or_price = this.dataset.value

        console.log('User', user)
        if (user != 'AnonymousUser') {
            addCookieItem(nam, productId, action, price, or_price, imageloc)

        } else {
            console.log("You need to log in to continue")
        }

    })

}

function addCookieItem(nam, productId, action, price, or_price, imageloc) {

    if (action == "add") {
        if (cart[productId] == undefined) {
            cart[productId] = { 'productId': productId, 'name': nam, 'quantity': 1, 'price': Number(price), 'or_price': Number(price), "location": imageloc }
        } else {
            cart[productId]['quantity'] += 1
            cart[productId]['price'] += Number(price)
        }

        if (action == "remove") {
            cart[productId]['qunatity'] -= 1
            if (cart[productId]['quantity'] <= 0) {
                delete cart[productId]
            }
        }

        console.log('Cart', cart)
        document.cookie = "cart=" + JSON.stringify(cart) + ";domain=;path = /"
    }
    cart_tr = document.cookie.split(';')
    cart_tra = cart_tr[1].split('=')
    cart_transform = JSON.parse(cart_tra[1])
    console.log(cart_transform)

    total = 0
    for ([keys, values] of Object.entries(cart_transform)) {
        total += cart_transform[keys]['quantity']
    }

    cart_dig = document.getElementById('cart_num')
    cart_dig.innerHTML = total
    console.log(total)

}


function cart_display() {
    cart_tr = document.cookie.split(';')
    cart_tra = cart_tr[1].split('=')
    cart_transform = JSON.parse(cart_tra[1])
    console.log(cart_transform)

    var total = 0
    for ([keys, values] of Object.entries(cart_transform)) {
        total += cart_transform[keys]['quantity']
    }

    cart_dig = document.getElementById('cart_num')
    cart_dig.innerHTML = total
    console.log(total)

}

cart_display();