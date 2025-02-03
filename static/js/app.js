document.addEventListener('DOMContentLoaded', function() {
    const headers = document.querySelectorAll('.collapsible-header');

    headers.forEach(header => {
        header.addEventListener('click', function() {
            const content = this.nextElementSibling;
            const pseudoElement = this; //Сам заголовок, где у нас псевдоэлемент
            if (content.style.display === 'none' || content.style.display === '') {
                content.style.display = 'grid';
                pseudoElement.classList.add('rotate-marker');
            } else {
                content.style.display = 'none';
                pseudoElement.classList.remove('rotate-marker');
            }
        });
    });
});