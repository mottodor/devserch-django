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


// Tag remove from project form
let tags = document.querySelectorAll('.project-tag')
for (tag of tags) {
    tag.addEventListener('click', (e) => {
        let tagId = e.target.dataset.tag
        let projectId = e.target.dataset.project
        fetch('http://127.0.0.1:8000/api/remove-tag/',
            {
                method: 'DELETE',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ 'project': projectId, 'tag': tagId })
            })
            .then(response => response.json())
            .then(data => {
                e.target.remove()
            })
    })
}