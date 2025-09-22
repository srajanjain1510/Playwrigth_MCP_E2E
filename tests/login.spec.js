const { test, expect } = require('@playwright/test');
const { LoginPage } = require('../pages/LoginPage');
const { DashboardPage } = require('../pages/DashboardPage');
const { testData } = require('../utils/testData');

test.describe('Login Functionality', () => {
  let loginPage;
  let dashboardPage;

  test.beforeEach(async ({ page }) => {
    loginPage = new LoginPage(page);
    dashboardPage = new DashboardPage(page);
    await loginPage.navigate();
  });

  test('should login with valid credentials', async ({ page }) => {
    await loginPage.login(testData.validUser.username, testData.validUser.password);
    await expect(dashboardPage.welcomeMessage).toBeVisible();
    await expect(dashboardPage.welcomeMessage).toContainText(`Welcome, ${testData.validUser.displayName}`);
  });

  test('should show error with invalid credentials', async ({ page }) => {
    await loginPage.login(testData.invalidUser.username, testData.invalidUser.password);
    await expect(loginPage.errorMessage).toBeVisible();
    await expect(loginPage.errorMessage).toContainText('Invalid username or password');
  });

  test('should require username and password', async ({ page }) => {
    await loginPage.submitButton.click();
    await expect(loginPage.usernameValidationMessage).toBeVisible();
    await expect(loginPage.passwordValidationMessage).toBeVisible();
  });
});