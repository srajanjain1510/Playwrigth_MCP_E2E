const { BasePage } = require('./BasePage');

/**
 * Page object for the dashboard page
 */
class DashboardPage extends BasePage {
  /**
   * @param {import('@playwright/test').Page} page 
   */
  constructor(page) {
    super(page);
    this.welcomeMessage = page.getByTestId('welcome-message');
    this.logoutButton = page.getByRole('button', { name: 'Logout' });
    this.navigationMenu = page.getByTestId('nav-menu');
    this.profileButton = page.getByRole('button', { name: 'Profile' });
    this.settingsButton = page.getByRole('button', { name: 'Settings' });
  }

  /**
   * Navigate to the dashboard page
   */
  async navigate() {
    await super.navigate('/dashboard');
  }

  /**
   * Logout from the application
   */
  async logout() {
    await this.logoutButton.click();
    await super.waitForNavigation();
  }

  /**
   * Navigate to the profile page
   */
  async goToProfile() {
    await this.profileButton.click();
    await super.waitForNavigation();
  }

  /**
   * Navigate to the settings page
   */
  async goToSettings() {
    await this.settingsButton.click();
    await super.waitForNavigation();
  }

  /**
   * Check if the dashboard page is displayed
   * @returns {Promise<boolean>} - True if the dashboard page is displayed
   */
  async isDisplayed() {
    return await this.welcomeMessage.isVisible();
  }
}

module.exports = { DashboardPage };