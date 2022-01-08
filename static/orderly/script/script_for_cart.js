const sum_output = document.querySelector('h1.cost_sum');
const names_POST = document.querySelector('input#names_arr');
const amounts_POST = document.querySelector('input#amounts_arr');
const costs_POST = document.querySelector('input#costs_sum');

const costs = document.querySelectorAll('h2.costs');
const names = document.querySelectorAll('h1.names');
const amounts = document.querySelectorAll('h2.amounts');

const arr_costs = [];
const arr_names = [];
const arr_amounts = [];

let sum = 0;

costs.forEach((e)=>{
    arr_costs.push(e.textContent);
})

names.forEach((e)=>{
    arr_names.push(e.textContent);
})

amounts.forEach((e)=>{
    arr_amounts.push(e.textContent);
})


arr_costs.forEach((e)=>{
    sum += parseFloat(e);
})

arr_amounts.forEach((e)=>{
    e = parseFloat(e);
})

sum = sum.toFixed(2)

sum_output.textContent = sum;
names_POST.value = arr_names;
amounts_POST.value = arr_amounts;
costs_POST.value = sum;
