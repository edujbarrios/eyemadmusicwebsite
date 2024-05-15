document.getElementById('copy-share-button').addEventListener('click', function() {
    const link = window.location.href;
    navigator.clipboard.writeText(link).then(() => {
        alert('Link successfully copied! 📋');
    }).catch(err => {
        console.error('Failed to copy: ', err);
    });
});
