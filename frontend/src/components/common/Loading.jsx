import React from 'react';

const Loading = ({ message = 'Loading...' }) => (
  <div style={{
    display: 'flex',
    justifyContent: 'center',
    alignItems: 'center',
    height: '100px',
    flexDirection: 'column'
  }}>
    <div className="spinner-border text-primary" role="status">
      <span className="visually-hidden">Loading...</span>
    </div>
    <p className="mt-2 text-muted">{message}</p>
  </div>
);

export default Loading;