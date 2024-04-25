// context/ProjectContext.js
import React, { createContext, useContext, useState } from 'react';

const ProjectContext = createContext();

export const useProjectContext = () => useContext(ProjectContext);

export const ProjectProvider = ({ children }) => {
  const [projects, setProjects] = useState([]);

  const fetchProjects = async () => {
    try {
      // Fetch projects from the backend API
      const response = await fetch('/api/projects/');
      const data = await response.json();
      setProjects(data);
    } catch (error) {
      console.error('Error fetching projects:', error);
    }
  };

  const addProject = async (newProject) => {
    try {
      // Send a POST request to add a new project
      const response = await fetch('/api/projects/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(newProject),
      });
      const data = await response.json();
      setProjects([...projects, data]);
    } catch (error) {
      console.error('Error adding project:', error);
    }
  };

  return (
    <ProjectContext.Provider value={{ projects, fetchProjects, addProject }}>
      {children}
    </ProjectContext.Provider>
  );
};
