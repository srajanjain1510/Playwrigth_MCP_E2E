/**
 * Base Page Object that all other page objects will extend
 */
class BasePage {
  /**
   * @param {import('@playwright/test').Page} page 
   */
  constructor(page) {
    this.page = page;
  }

  /**
   * Navigate to a specific URL
   * @param {string} url - The URL to navigate to
   */
  async navigate(url) {
    await this.page.goto(url);
  }

  /**
   * Wait for navigation to complete
   */
  async waitForNavigation() {
    await this.page.waitForLoadState('networkidle');
  }

  /**
   * Get page title
   * @returns {Promise<string>} - The page title
   */
  async getTitle() {
    return await this.page.title();
  }

  /**
   * Take a screenshot
   * @param {string} name - Name for the screenshot file
   */
  async takeScreenshot(name) {
    await this.page.screenshot({ path: `./screenshots/${name}.png` });
  }
}

module.exports = { BasePage };