let productList = [];
let currentId = 0;
document
    .querySelectorAll(".featuredItem")
    .forEach(el => {
        let productName = el.querySelector(".featuredData > .featuredName").innerText;
        let productPrice = +el.querySelector(".featuredData > .featuredPrice").innerText.substr(1);
        el.querySelector(".featuredData").setAttribute("productId", currentId);
        productList[currentId] = [productName, productPrice];
        currentId++;

        el.addEventListener("click", event => {
            if (event.target === el.querySelector(".featuredImgWrap > .featuredImgDark > button")){
                cart[el.querySelector(".featuredData").getAttribute("productId")] += 1;
                updateCartCount();
            }
        });
});

const cartEl = document.querySelector(".basket");
document.querySelector(".cartIconWrap").addEventListener("click", () => {
    cartEl.classList.toggle("hidden");
});

let cart = new Array(productList.length).fill(0);
const cartTotalEl = cartEl.querySelector(".basketTotal");

const cartCounterEl = document.querySelector(".cartIconWrap > span");
const updateCartCount = function() {
    let cartSum = 0;
    cart.forEach(el => {cartSum += el});
    if (cartSum === 0) {
        cartCounterEl.style.display = "none";
    }
    else {
        cartCounterEl.style.display = "block";
        cartCounterEl.innerText = cartSum;
    }
    cartEl.querySelectorAll(".basketProduct").forEach(el => {el.remove()});
    let totalPrice = 0;
    for(let i=0; i<cart.length; i++) {
        if (cart[i] > 0) {
            let childEl = document.createElement("div");
            childEl.classList.add("basketRow", "basketProduct");
            let name = document.createElement("div");
            let amount = document.createElement("div");
            let price = document.createElement("div");
            let total = document.createElement("div");
            name.innerText = productList[i][0];
            amount.innerText = cart[i];
            price.innerText = "$" + productList[i][1].toFixed(2);
            total.innerText = "$" + (cart[i] * productList[i][1]).toFixed(2);
            childEl.appendChild(name);
            childEl.appendChild(amount);
            childEl.appendChild(price);
            childEl.appendChild(total);
            cartEl.insertBefore(childEl, cartTotalEl);

            totalPrice += cart[i] * productList[i][1];
        };
    }
    cartTotalEl.innerText = "$" + totalPrice.toFixed(2);
};


updateCartCount();