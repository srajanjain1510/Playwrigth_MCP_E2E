/**
 * Generate a random string of specified length
 * @param {number} length - Length of the random string
 * @returns {string} - Random string
 */
function generateRandomString(length = 8) {
  const chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
  let result = '';
  for (let i = 0; i < length; i++) {
    result += chars.charAt(Math.floor(Math.random() * chars.length));
  }
  return result;
}

/**
 * Generate a random email address
 * @returns {string} - Random email address
 */
function generateRandomEmail() {
  return `test.${generateRandomString(8)}@example.com`;
}

/**
 * Format date to YYYY-MM-DD format
 * @param {Date} date - Date to format
 * @returns {string} - Formatted date string
 */
function formatDate(date = new Date()) {
  const year = date.getFullYear();
  const month = String(date.getMonth() + 1).padStart(2, '0');
  const day = String(date.getDate()).padStart(2, '0');
  return `${year}-${month}-${day}`;
}

/**
 * Wait for a specified amount of time
 * @param {number} ms - Time to wait in milliseconds
 * @returns {Promise<void>}
 */
async function wait(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

module.exports = {
  generateRandomString,
  generateRandomEmail,
  formatDate,
  wait
};