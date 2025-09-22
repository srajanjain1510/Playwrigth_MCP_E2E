const { BasePage } = require('./BasePage');

/**
 * Page object for the login page
 */
class LoginPage extends BasePage {
  /**
   * @param {import('@playwright/test').Page} page 
   */
  constructor(page) {
    super(page);
    this.usernameInput = page.getByLabel('Username');
    this.passwordInput = page.getByLabel('Password');
    this.submitButton = page.getByRole('button', { name: 'Login' });
    this.errorMessage = page.getByTestId('error-message');
    this.usernameValidationMessage = page.getByTestId('username-validation');
    this.passwordValidationMessage = page.getByTestId('password-validation');
  }

  /**
   * Navigate to the login page
   */
  async navigate() {
    await super.navigate('/login');
  }

  /**
   * Login with the provided credentials
   * @param {string} username - The username to use
   * @param {string} password - The password to use
   */
  async login(username, password) {
    await this.usernameInput.fill(username);
    await this.passwordInput.fill(password);
    await this.submitButton.click();
    await super.waitForNavigation();
  }

  /**
   * Check if the login page is displayed
   * @returns {Promise<boolean>} - True if the login page is displayed
   */
  async isDisplayed() {
    return await this.submitButton.isVisible();
  }
}

module.exports = { LoginPage };