import React, { useState, useEffect } from 'react';
import { workflowsAPI } from '../../utils/api';

const WorkflowManager = ({ organizationId, organizations }) => {
  const [workflows, setWorkflows] = useState([]);
  const [formData, setFormData] = useState({ name: '' });
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  useEffect(() => {
    if (organizationId) {
      fetchWorkflows();
    }
  }, [organizationId]);

  const fetchWorkflows = async () => {
    try {
      const response = await workflowsAPI.getAll(organizationId);
      setWorkflows(response.data);
    } catch (err) {
      setError('Failed to fetch workflows');
      console.error('Error fetching workflows:', err);
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError('');

    try {
      await workflowsAPI.create({
        ...formData,
        org_id: organizationId
      });
      setFormData({ name: '' });
      fetchWorkflows();
    } catch (err) {
      setError(err.response?.data?.error || 'Failed to create workflow');
    } finally {
      setLoading(false);
    }
  };

  const handleChange = (e) => {
    setFormData({ name: e.target.value });
  };

  const selectedOrg = organizations.find(org => org._id === organizationId);

  return (
    <div className="mt-4">
      <h4>Workflows for {selectedOrg?.name}</h4>

      <div className="card mb-3">
        <div className="card-header">Create Workflow</div>
        <div className="card-body">
          {error && <div className="alert alert-danger">{error}</div>}

          <form onSubmit={handleSubmit}>
            <div className="form-group">
              <label>Workflow Name:</label>
              <input
                type="text"
                value={formData.name}
                onChange={handleChange}
                required
                disabled={loading}
                className="form-control"
              />
            </div>

            <button
              type="submit"
              className="btn btn-primary mt-2"
              disabled={loading}
            >
              {loading ? 'Creating...' : 'Create Workflow'}
            </button>
          </form>
        </div>
      </div>

      <div className="card">
        <div className="card-header">Workflows</div>
        <div className="card-body">
          {workflows.length === 0 ? (
            <p className="text-muted">No workflows created yet.</p>
          ) : (
            <div className="list-group">
              {workflows.map(workflow => (
                <div key={workflow._id} className="list-group-item">
                  <div className="d-flex justify-content-between align-items-center">
                    <div>
                      <h6 className="mb-1">{workflow.name}</h6>
                      <small className="text-muted">
                        Status: {workflow.is_active ? 'Active' : 'Inactive'}
                      </small>
                    </div>
                    <button
                      className="btn btn-outline-primary btn-sm"
                      onClick={() => {/* Add workflow stage management */}}
                    >
                      Manage Stages
                    </button>
                  </div>
                </div>
              ))}
            </div>
          )}
        </div>
      </div>
    </div>
  );
};

export default WorkflowManager;