import axios from 'axios';

export const getCurrentUser = async () => {
    const token = localStorage.getItem('access_token');

    const response = await axios.get('http://localhost:8000/api/me/', {
        headers: {
            Authorization: `Bearer ${token}`
        }
    });

    return response; // or return response.data if API returns JSON object
};
