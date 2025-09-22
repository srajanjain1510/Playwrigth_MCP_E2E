/**
 * Test data for the application
 */
const testData = {
  validUser: {
    username: 'testuser',
    password: 'Password123!',
    displayName: 'Test User'
  },
  invalidUser: {
    username: 'invaliduser',
    password: 'wrongpassword',
  },
  adminUser: {
    username: 'admin',
    password: 'AdminPass123!',
    displayName: 'Administrator'
  },
  testEnvironments: {
    development: 'http://localhost:3000',
    staging: 'https://staging.mcpapp.example.com',
    production: 'https://mcpapp.example.com'
  },
  timeouts: {
    short: 5000,
    medium: 10000,
    long: 30000
  }
};

module.exports = { testData };