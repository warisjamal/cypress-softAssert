let itBlockErrors = {}; // Define an object to store errors for each 'it' block title globally
let totalFailedAssertionsByDescribe = {}; // Keep track of the total number of assertion failures for each "describe" block

Cypress.Commands.add('softAssert', { prevSubject: false }, (actualValue, expectedValue, message) => {
  return cy.wrap(null, { timeout: Cypress.config('defaultCommandTimeout') }).then(() => {
    try {
      expect(actualValue).to.equal(expectedValue, message);
    } catch (err) {
      const itBlockTitle = Cypress.currentTest.title;
      const describeBlockTitle = Cypress.currentTest.titlePath[0];
      
      // Initialize the count for the "describe" block if it doesn't exist
      totalFailedAssertionsByDescribe[describeBlockTitle] = totalFailedAssertionsByDescribe[describeBlockTitle] || 0;
      totalFailedAssertionsByDescribe[describeBlockTitle]++;

      if (!itBlockErrors[itBlockTitle]) {
        itBlockErrors[itBlockTitle] = [];
      }
      itBlockErrors[itBlockTitle].push({ message, error: err });
    }
  });
});

Cypress.Commands.add('assertAll', () => {
  const errors = itBlockErrors;
  itBlockErrors = {};

  if (Object.keys(errors).length > 0) {
    const errorMessages = Object.entries(errors).map(([title, entries], index) => {
      const errorMessage = (entries as Array<{ error: Error }>).map(({ error }) => (
        `${"=> "+error.message}`
      )).join('\n\n');

      return `${index + 1}. Test Title: ${title}\n\n${errorMessage}`;
    });

    const errorMessage = Object.entries(totalFailedAssertionsByDescribe).map(([describe, count]) => {
      return `Total assertion failures in "${describe}": ${count}`;
    }).join('\n');

    throw new Error(`Soft assertion failed: Total it block failed (${Object.keys(errors).length})\n\n${errorMessages.join('\n\n')}\n\n${errorMessage}`);
  }
});
