import React, { useState, useEffect } from 'react';
import axios from 'axios';

const ProjectUpdate = ({ projectId }) => {
    const [name, setName] = useState('');

    useEffect(() => {
        axios.get(`http://your-backend-url/api/projects/${projectId}/`)
            .then(response => {
                setName(response.data.name);
            })
            .catch(error => {
                console.error('Error fetching project:', error);
            });
    }, [projectId]);

    const handleSubmit = (event) => {
        event.preventDefault();
        axios.put(`http://127.0.0.1:8000/api/projects/${projectId}/`, { name })
            .then(response => {
                console.log('Project updated successfully:', response.data);
                // Redirect or update state as needed
            })
            .catch(error => {
                console.error('Error updating project:', error);
            });
    };

    return (
        <div>
            <h1>Update Project</h1>
            <form onSubmit={handleSubmit}>
                <input type="text" value={name} onChange={(e) => setName(e.target.value)} />
                <button type="submit">Update</button>
            </form>
        </div>
    );
};

export default ProjectUpdate;
