console.log(window.location)
const searchText = `${window.location.origin}${window.location.pathname}${window.location.search}`
console.log(searchText)

const inputElement = document.getElementById('search')
// console.log(inputElement.value)

const searchForm = document.getElementById('search_form') 
function onSubmit(e) {
    e.preventDefault()
    console.log(inputElement.value)
    window.location.href =  `${window.location.origin}${window.location.pathname}?make=${inputElement.value}`
}

searchForm.addEventListener('submit', onSubmit)


// Work in Progress
jQuery(function($) {
    var path = window.location.href;

    $('ul a').each(function() {
        if(this.href === path) {
            $(this).addClass('active');
        };
    });
});