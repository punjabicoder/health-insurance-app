import React, { useState } from "react";
import axios from 'axios';
import { useNavigate } from "react-router-dom";

function Login() {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const navigate = useNavigate();

    const login = () => {
        axios.post('http://localhost:8000/api/token/', { username, password })
            .then(res => {
                localStorage.setItem('access_token', res.data.access);
                localStorage.setItem('refresh_token', res.data.refresh);
                console.log("Token saved:", res.data.access);
                navigate('/dashboard');  // ✅ Redirect after token is saved
            })
            .catch(err => {
                console.error("Login failed", err);
                alert("Invalid credentials");
            });
    };

    return (
        <div>
            <input onChange={(e) => setUsername(e.target.value)} placeholder="Username" />
            <input onChange={(e) => setPassword(e.target.value)} type="password" placeholder="Password" />
            <button onClick={login}>Login</button>
        </div>
    );
}

export default Login;
