import React, { useEffect, useState } from 'react';
import axios from 'axios';

const ProjectDetail = ({ projectId }) => {
  const [project, setProject] = useState(null);

  useEffect(() => {
    const fetchProject = async () => {
      try {
        const response = await axios.get(`/api/projects/${projectId}/`);
        setProject(response.data);
      } catch (error) {
        console.error('Error fetching project details:', error);
      }
    };

    fetchProject();
  }, [projectId]);

  if (!project) {
    return <div>Loading...</div>;
  }

  return (
    <div>
      <h2>Project Details</h2>
      <p>Title: {project.title}</p>
      {/* Add more project details here */}
    </div>
  );
};

export default ProjectDetail;
