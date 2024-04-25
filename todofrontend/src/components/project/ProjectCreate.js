// ProjectCreate.js

import React, { useState } from 'react';
import axios from 'axios';

const ProjectCreate = () => {
    const [name, setName] = useState('');
    const [date, setDate] = useState('');
    const [time, setTime] = useState('');
    const [error, setError] = useState(null);

    const handleSubmit = async (event) => {
        event.preventDefault();
        
        try {
            const response = await axios.post('http://127.0.0.1:8000/api/projects/', {
                name,
                date,
                time
            });
            console.log('Project created successfully:', response.data);
            // Redirect or handle success as needed
        } catch (error) {
            setError(error.message); // Capture error message
            console.error('Error creating project:', error);
        }
    };

    return (
        <div>
            <h1>Create Project</h1>
            {error && <div>Error: {error}</div>} {/* Display error message if present */}
            <form onSubmit={handleSubmit}>
                <input type="text" value={name} onChange={(e) => setName(e.target.value)} placeholder="Project Name" />
                <input type="date" value={date} onChange={(e) => setDate(e.target.value)} placeholder="Date" />
                <input type="time" value={time} onChange={(e) => setTime(e.target.value)} placeholder="Time" />
                <button type="submit">Create</button>
            </form>
        </div>
    );
};

export default ProjectCreate;
