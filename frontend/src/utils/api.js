import axios from 'axios';

const API_BASE_URL = '/api';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Request interceptor for adding auth token if available
api.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('authToken');
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => Promise.reject(error)
);

// Response interceptor for handling errors
api.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      localStorage.removeItem('authToken');
      localStorage.removeItem('user');
      window.location.href = '/login';
    }
    return Promise.reject(error);
  }
);

export const authAPI = {
  login: (credentials) => api.post('/users/login', credentials),
  register: (userData) => api.post('/users/register', userData),
};

export const organizationsAPI = {
  getAll: () => api.get('/organizations'),
  create: (orgData) => api.post('/organizations', orgData),
  getById: (id) => api.get(`/organizations/${id}`),
  update: (id, data) => api.put(`/organizations/${id}`, data),
  delete: (id) => api.delete(`/organizations/${id}`),
};

export const workflowsAPI = {
  getAll: (orgId) => api.get(`/workflows${orgId ? `?organization_id=${orgId}` : ''}`),
  create: (workflowData) => api.post('/workflows', workflowData),
  getStages: (workflowId) => api.get(`/workflows/${workflowId}/stages`),
  addStage: (workflowId, stageData) => api.post(`/workflows/${workflowId}/stages`, stageData),
};

export const applicationsAPI = {
  getAll: (params) => api.get('/applications', { params }),
  create: (appData) => api.post('/applications', appData),
  advance: (appId, data) => api.post(`/applications/${appId}/advance`, data),
  getHistory: (appId) => api.get(`/applications/${appId}/history`),
};

export default api;