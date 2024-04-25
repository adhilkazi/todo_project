import React from 'react';
import axios from 'axios';

const ProjectDelete = ({ projectId }) => {
    const handleDelete = () => {
        axios.delete(`http://127.0.0.1:8000/api/projects/${projectId}/`)
            .then(response => {
                console.log('Project deleted successfully');
                // Redirect or update state as needed
            })
            .catch(error => {
                console.error('Error deleting project:', error);
            });
    };

    return (
        <div>
            <h1>Delete Project</h1>
            <button onClick={handleDelete}>Delete</button>
        </div>
    );
};

export default ProjectDelete;
