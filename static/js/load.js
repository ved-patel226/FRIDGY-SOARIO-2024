document.querySelectorAll('.load-show').forEach(div => {
    div.addEventListener('click', () => {
        document.querySelector('.container').style.display = 'block';
        document.querySelector('.loading-overlay').style.display = 'block';
        document.body.style.overflow = 'hidden';
    });
});

window.onbeforeunload = function() {
    document.querySelector('.container').style.display = 'block';
    document.querySelector('.loading-overlay').style.display = 'block';
    document.body.style.overflow = 'hidden';
  };

