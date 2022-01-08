const amount = document.querySelector('input#amount');
const price = document.querySelector('h1#price_h1');
const hidden_price = document.querySelector('input#price_overall');
const price_start = hidden_price.value;

amount.addEventListener('input', ()=>{
    let scale = (price_start * amount.value).toFixed(2);
    price.textContent = scale;
    hidden_price.value = scale;
})


