console.log("side_nav connected...")

document.querySelectorAll('.side-nav-collapsible').forEach(button => {
    button.addEventListener('click', () => {
        const accordionContent = button.nextElementSibling;

        button.classList.toggle('side-nav-collapsible--active');

        if (button.classList.contains('side-nav-collapsible--active')) {
            accordionContent.style.maxHeight = accordionContent.scrollHeight + 'px';
        } else {
            accordionContent.style.maxHeight = 0;
        }
    });
});