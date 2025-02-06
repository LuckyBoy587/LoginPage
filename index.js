document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    // Simple validation
    if (username === '' || password === '') {
        alert('Please fill in both fields.');
        return;
    }

    // Here you can add your login logic, e.g., sending data to the server
    console.log('Username:', username);
    console.log('Password:', password);

    // For demonstration, just show an alert
    alert('Login successful!');
});