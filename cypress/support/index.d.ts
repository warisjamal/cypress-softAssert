declare namespace Cypress {
  interface Chainable<Subject> {
    softAssert(actualValue: any, expectedValue: any, message: string): Chainable<any>;
    assertAll(): Chainable<any>;
  }
}