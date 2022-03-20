// Add pagination for search results
let searchForm = document.querySelector('#search-form')
let pageLinks = document.querySelectorAll('.page-link')

if (searchForm) {
    for (link of pageLinks) {
        link.addEventListener('click', function (e) {
            e.preventDefault()
            let page = this.dataset.page
            searchForm.innerHTML += `<input value=${page} name="page" hidden/>`
            searchForm.submit()
        })
    }
}
