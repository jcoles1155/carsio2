// console.log(window.location)
const searchText = `${window.location.origin}${window.location.pathname}${window.location.search}`
// console.log(searchText)

const inputElement = document.getElementById('model')
const carModel = document.getElementById('model')
const make = document.getElementById('make')
const year = document.getElementById('year')
const color = document.getElementById('color')
// console.log(inputElement.value)

const searchForm = document.getElementById('search_form') 
function onSubmit(e) {
    e.preventDefault()
    window.location.href =  `${window.location.origin}${window.location.pathname}?make=${make.value.toLowerCase()}&color=${color.value.toLowerCase()}`
    // if(make.value !== '' && color.value !== '') {
    //     console.log(inputElement.value);
    //     window.location.href =  `${window.location.origin}${window.location.pathname}?make=${make.value.toLowerCase()}&color=${color.value.toLowerCase()}`
    // } else {
    //     console.log('null');
    //     window.location.href = `${window.location.origin}${window.location.pathname}${window.location.search}`
    // }
    // console.log(inputElement)
    // window.location.href =  `${window.location.origin}${window.location.pathname}?make=${inputElement.value.toLowerCase()}`
}

searchForm.addEventListener('submit', onSubmit)

