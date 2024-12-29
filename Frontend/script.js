document.getElementById('search').addEventListener('click', () => {
    const username = document.getElementById('username').value;
    fetch('http://127.0.0.1:8001/users/${username}')
        .then(response => {
            if (!response.ok) throw new Error('User not found');
            return response.json();
        })
        .then(data => {
            localStorage.setItem('userData', JSON.stringify(data));
            window.location.href = 'user.html';
        })
        .catch(err => {
            console.error(err);
            alert(err.message);
        });
});

if (window.location.pathname.endsWith('user.html')) {
    const userData = JSON.parse(localStorage.getItem('userData'));
    const userInfoDiv = document.getElementById('user-info');
    userInfoDiv.innerHTML = `<pre>${JSON.stringify(userData, null, 2)}</pre>`;
    document.getElementById('back').addEventListener('click', () => {
        window.location.href = 'index.html';
    });
}

if (window.location.pathname.endsWith('repo.html')) {
    const repoData = JSON.parse(localStorage.getItem('repoData'));
    const repoInfoDiv = document.getElementById('repo-info');
    repoInfoDiv.innerHTML = `<pre>${JSON.stringify(repoData, null, 2)}</pre>`;
    document.getElementById('back').addEventListener('click', () => {
        window.location.href = 'user.html';
    });
}