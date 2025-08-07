import React, { useEffect, useState } from "react";
import { getCurrentUser } from '../api/user';

import AdminDashboard from "../components/dashboards/AdminDashboard";
import AgentDashboard from "../components/dashboards/AgentDashboard";
import CustomerDashboard from "../components/dashboards/CustomerDashboard";
import DoctorDashboard from "../components/dashboards/DoctorDashboard";

const Dashboard = () => {
    const[role, setRole] = useState(null);

    useEffect(() => {
        getCurrentUser().then(user => {
            setRole(user.role);
        }).catch(error => {
            console.error("Failed to fetch user:", error);
        });
    }, []);

    if (!role) return <div>Loading...</div>;

    switch (role) {
        case 'admin': return <AdminDashboard />;
        case 'agent': return <AgentDashboard />;
        case 'customer': return <CustomerDashboard />;
        case 'doctor': return <DoctorDashboard />;
        default: return <div>Invalid role</div>;
    }
};

export default Dashboard;