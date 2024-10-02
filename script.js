function getColorFromUsername(username) {
    const colors = ['#FF5733', '#33FF57', '#5733FF', '#33F3FF', '#F3FF33', '#FF33F3'];
    let index = username.charCodeAt(0) % colors.length;
    return colors[index];
}

document.querySelectorAll('.profile-pic').forEach(function(pic) {
    let username = pic.getAttribute('data-username');
    pic.style.setProperty('--profile-bg-color', getColorFromUsername(username));
});
