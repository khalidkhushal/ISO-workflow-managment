import React, { useState, useEffect } from 'react';
import OrganizationManager from './organizations/OrganizationManager';
import WorkflowManager from './workflows/WorkflowManager';
import { organizationsAPI } from '../utils/api';

const Dashboard = ({ user, onLogout }) => {
  const [organizations, setOrganizations] = useState([]);
  const [selectedOrgId, setSelectedOrgId] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchOrganizations();
  }, []);

  const fetchOrganizations = async () => {
    try {
      const response = await organizationsAPI.getAll();
      setOrganizations(response.data);
    } catch (error) {
      console.error('Failed to fetch organizations:', error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <div className="d-flex justify-content-between align-items-center mb-4">
        <h2>Welcome, {user.full_name}!</h2>
        <button onClick={onLogout} className="btn btn-outline-danger">
          Logout
        </button>
      </div>

      <OrganizationManager
        organizations={organizations}
        onOrganizationCreated={fetchOrganizations}
        onSelectOrganization={setSelectedOrgId}
      />

      {selectedOrgId && (
        <WorkflowManager
          organizationId={selectedOrgId}
          organizations={organizations}
        />
      )}
    </div>
  );
};

export default Dashboard;