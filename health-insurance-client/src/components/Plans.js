import React, { useEffect, useState } from 'react';
import axios from 'axios';

function Plans() {
    const [plans, setPlans] = useState([]);

    useEffect(() => {
        axios.get('http://localhost:8000/api/plans/', {
            headers: {
                Authorization: 'Bearer $(localStorage.getItem("token")}'
            }
        })
        .then(res => setPlans(res.data))
        .catch(err => console.error(err));
    }, []);


return (
    <div>
        <h2>Available Plans</h2>
        <ul>
            {plans.map(plan => (
                <li key={plan.id}>
                    {plan.name} - ${plan.premium} <br /> Coverage: {plan.coverage}
                </li>
            ))}
        </ul>
    </div>
);

}

export default Plans;