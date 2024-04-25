import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { AuthProvider } from './context/AuthContext';
import Login from './components/Auth/LoginForm';
import ProjectDetail from './components/project/ProjectDetails';
import ProjectList from './components/project/ProjectList';
import RegistrationForm from './components/Auth/RegistrationForm';
import ProjectCreate from './components/project/ProjectCreate'; // Import the ProjectCreate component

function App() {
  return (
    <AuthProvider>
      <Router>
        <div className="App">
          <Routes>
            <Route path="/login" element={<Login />} />
            <Route path="/registration" element={<RegistrationForm />} />
            <Route path="/projects/create" element={<ProjectCreate />} /> {/* Route for creating a new project */}
            <Route path="/projects/:id" element={<ProjectDetail />} />
            <Route path="/" element={<ProjectList />} />
          </Routes>
        </div>
      </Router>
    </AuthProvider>
  );
}

export default App;
