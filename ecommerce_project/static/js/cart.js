let cart = [];

function addToCart(productId) {
    fetch(`/api/products/${productId}/`)
        .then(response => response.json())
        .then(product => {
            const existingItem = cart.find(item => item.id === product.id);
            if (existingItem) {
                existingItem.quantity += 1;
            } else {
                cart.push({...product, quantity: 1});
            }
            updateCartDisplay();
            saveCartToLocalStorage();
        });
}

function updateCartDisplay() {
    const cartItems = document.getElementById('cart-items');
    const cartTotal = document.getElementById('cart-total');
    
    if (cartItems) {
        cartItems.innerHTML = '';
        let total = 0;

        cart.forEach(item => {
            const itemElement = document.createElement('div');
            itemElement.className = 'cart-item';
            itemElement.innerHTML = `
                
                <span class="details">
                    <p>${item.name}</p>
                    <p>Quantity: ${item.quantity}</p>
                </span>
                <p>$${(item.price * item.quantity).toFixed(2)}</p>
                <button onclick="removeFromCart(${item.id})">Remove</button>
            `;
            cartItems.appendChild(itemElement);
            total += item.price * item.quantity;
        });

        if (cartTotal) {
            cartTotal.textContent = `Total: $${total.toFixed(2)}`;
        }
    }

    updateCartIcon();
}

function removeFromCart(productId) {
    const index = cart.findIndex(item => item.id === productId);
    if (index !== -1) {
        if (cart[index].quantity > 1) {
            cart[index].quantity -= 1;
        } else {
            cart.splice(index, 1);
        }
        updateCartDisplay();
        saveCartToLocalStorage();
    }
}

function saveCartToLocalStorage() {
    localStorage.setItem('cart', JSON.stringify(cart));
}

function loadCartFromLocalStorage() {
    const savedCart = localStorage.getItem('cart');
    if (savedCart) {
        cart = JSON.parse(savedCart);
        updateCartDisplay();
    }
}

function updateCartIcon() {
    const cartIcon = document.getElementById('cart-icon');
    if (cartIcon) {
        const uniqueItemCount = cart.length;
        const totalItemCount = cart.reduce((total, item) => total + item.quantity, 0);
        cartIcon.textContent = `(${uniqueItemCount} unique, ${totalItemCount} total)`;
        cartIcon.setAttribute('aria-label', `Cart with ${uniqueItemCount} unique items and ${totalItemCount} total items`);
    }
}

document.addEventListener('DOMContentLoaded', () => {
    loadCartFromLocalStorage();

    const addToCartButtons = document.querySelectorAll('.add-to-cart');
    addToCartButtons.forEach(button => {
        button.addEventListener('click', () => addToCart(parseInt(button.dataset.id)));
    });

    const checkoutButton = document.getElementById('checkout');
    if (checkoutButton) {
        checkoutButton.addEventListener('click', () => {
            // Here you would typically send the cart data to the server
            console.log('Checkout clicked', cart);
            alert('Thank you for your order!');
            cart = [];
            updateCartDisplay();
            saveCartToLocalStorage();
        });
    }
});

