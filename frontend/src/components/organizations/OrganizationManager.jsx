import React, { useState } from 'react';
import { organizationsAPI } from '../../utils/api';

const OrganizationManager = ({ organizations, onOrganizationCreated, onSelectOrganization }) => {
  const [formData, setFormData] = useState({ name: '' });
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError('');

    try {
      await organizationsAPI.create(formData);
      setFormData({ name: '' });
      onOrganizationCreated();
    } catch (err) {
      setError(err.response?.data?.error || 'Failed to create organization');
    } finally {
      setLoading(false);
    }
  };

  const handleChange = (e) => {
    setFormData({ name: e.target.value });
  };

  return (
    <div className="mb-4">
      <h3>Organizations</h3>

      <div className="card mb-3">
        <div className="card-header">Create Organization</div>
        <div className="card-body">
          {error && <div className="alert alert-danger">{error}</div>}

          <form onSubmit={handleSubmit}>
            <div className="form-group">
              <label>Organization Name:</label>
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
              {loading ? 'Creating...' : 'Create Organization'}
            </button>
          </form>
        </div>
      </div>

      <div className="card">
        <div className="card-header">Your Organizations</div>
        <div className="card-body">
          {organizations.length === 0 ? (
            <p className="text-muted">No organizations created yet.</p>
          ) : (
            <div className="list-group">
              {organizations.map(org => (
                <div
                  key={org._id}
                  className="list-group-item d-flex justify-content-between align-items-center"
                >
                  <span>{org.name}</span>
                  <button
                    className="btn btn-primary btn-sm"
                    onClick={() => onSelectOrganization(org._id)}
                  >
                    Manage Workflows
                  </button>
                </div>
              ))}
            </div>
          )}
        </div>
      </div>
    </div>
  );
};

export default OrganizationManager;